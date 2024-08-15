from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Load the trained machine learning model
model = joblib.load('MachineLearning/car_price_model.pkl')

# Configure the database connection using an absolute path
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data/vehicles.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the database model
class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.Float, nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    engine_capacity = db.Column(db.Float, nullable=False)
    transmission = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Car {self.make} {self.model} {self.year}>'

# Endpoint to retrieve vehicles from the database
@app.route('/api/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Car.query.limit(10).all()  # Limit response to 10 entries for testing
    return jsonify([{
        'id': v.id,
        'price': v.price,
        'year': v.year,
        'mileage': v.mileage,
        'fuel_type': v.fuel_type,
        'engine_capacity': v.engine_capacity,
        'transmission': v.transmission,
        'location': v.location,
        'make': v.make,
        'model': v.model
    } for v in vehicles])

# Endpoint to predict car prices
@app.route('/api/predict', methods=['POST'])
def predict_price():
    data = request.json
    
    # Convert input data to DataFrame
    input_data = pd.DataFrame([data])
    
    # Perform the same encoding as during training
    input_data = pd.get_dummies(input_data, columns=['fuel_type', 'transmission', 'location', 'make', 'model'])
    
    # Ensure the input data has the same columns as the training data
    input_data = input_data.reindex(columns=model.feature_names_in_, fill_value=0)
    
    # Make prediction
    predicted_price = model.predict(input_data)[0]
    
    # Return the prediction as a JSON response
    return jsonify({'predicted_price': predicted_price})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure the database tables are created
        app.run(debug=True)

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import joblib
import pandas as pd


app = Flask(__name__)

# Configure the database connection
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data/car_prices.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Load the trained machine learning model
model = joblib.load(os.path.join(basedir, 'MachineLearning', 'car_price_model.pkl'))

# Define the database model
# Define the database model
class CleanedVehicle(db.Model):
    __tablename__ = 'cars'  # Explicitly map to the 'cars' table
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
        return f'<CleanedVehicle {self.make} {self.model} {self.year}>'

# Validation function
def validate_search(make, model):
    matching_make = CleanedVehicle.query.filter(CleanedVehicle.make.ilike(f"%{make}%")).first()
    matching_model = CleanedVehicle.query.filter(CleanedVehicle.model.ilike(f"%{model}%")).first()

    if not matching_make or not matching_model:
        return False, "No matching entries found for the given make or model."
    
    return True, ""

# Endpoint to retrieve vehicles from the database with pagination and search functionality
@app.route('/api/vehicles', methods=['GET'])
def get_vehicles():
    page = int(request.args.get('page', 1))
    make = request.args.get('make', '').strip()
    model = request.args.get('model', '').strip()
    filter_type = request.args.get('filter', '').strip()

    is_valid, message = validate_search(make, model)
    if not is_valid:
        return jsonify({'error': message}), 400

    query = CleanedVehicle.query

    if make:
        query = query.filter(CleanedVehicle.make.ilike(f"%{make}%"))
    if model:
        query = query.filter(CleanedVehicle.model.ilike(f"%{model}%"))

    # Apply filtering based on filter_type
    if filter_type == "price_asc":
        query = query.order_by(CleanedVehicle.price.asc())
    elif filter_type == "price_desc":
        query = query.order_by(CleanedVehicle.price.desc())
    elif filter_type == "year_asc":
        query = query.order_by(CleanedVehicle.year.asc())
    elif filter_type == "year_desc":
        query = query.order_by(CleanedVehicle.year.desc())

    # Pagination for vehicle details
    pagination = query.paginate(page=page, per_page=9, error_out=False)
    vehicles = pagination.items

    # Query for price trend data (all entries for the specific make and model)
    if make and model:
        price_trend = CleanedVehicle.query.filter_by(make=make, model=model).order_by(CleanedVehicle.id).all()
        trend_data = [{'id': v.id, 'price': v.price, 'year': v.year} for v in price_trend]
    else:
        trend_data = []

    return jsonify({
        'vehicles': [{
            'id': v.id,
            'price': v.price,
            'year': v.year,
            'mileage': v.mileage,
            'fuel_type': v.fuel_type,
            'engine_capacity': v.engine_capacity,
            'transmission': v.transmission,
            'location': v.location,
            'make': v.make,
            'model': v.model,
            'price_display': f"PKR {v.price:,.2f}"
        } for v in vehicles],
        'pages': pagination.pages,
        'trend_data': trend_data
    })


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

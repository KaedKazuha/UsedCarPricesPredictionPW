from flask import Flask, jsonify
from models import db, CleanedVehicle  # Import your models from models.py
import os

app = Flask(__name__)

# Simplified database URI
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data/vehicles.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Ensure that the 'data' directory exists
os.makedirs('data', exist_ok=True)

@app.route('/api/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = CleanedVehicle.query.limit(10).all()
    return jsonify([{
        'name': v.name,
        'year': v.year,
        'price': v.price,
        'price_display': v.price_display,
        'mileage': v.mileage,
        'fuel_type': v.fuel_type,
        'engine_capacity': v.engine_capacity,
        'transmission': v.transmission,
        'location': v.location,
        'url': v.url,
        'image_url': v.image_url,
        'id': v.id
    } for v in vehicles])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
        app.run()

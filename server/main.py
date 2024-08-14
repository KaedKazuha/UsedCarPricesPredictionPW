from flask import Flask, jsonify
from models import db, CleanedVehicle
import os

app = Flask(__name__)

# Use the existing car_prices.db
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data/car_prices.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/api/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = CleanedVehicle.query.all()
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
        'model': v.model,
        'price_display': f"PKR {v.price:,.2f}"
    } for v in vehicles])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
        app.run(debug=True)

import json
from main import app, db, CleanedVehicle  # Adjust import as needed

# Load the cleaned data from the JSON file
with open('used_car_data.json', 'r') as f:
    cleaned_data = json.load(f)

# Ensure the database is fresh
with app.app_context():
    db.drop_all()  # Drop existing tables
    db.create_all()  # Create new tables

    for vehicle_data in cleaned_data:
        vehicle = CleanedVehicle(
            id=vehicle_data['id'],
            name=vehicle_data['name'],
            year=vehicle_data['year'],
            price=vehicle_data['price'],
            price_display=vehicle_data['price_display'],
            mileage=vehicle_data['mileage'],
            fuel_type=vehicle_data['fuel_type'],
            engine_capacity=vehicle_data['engine_capacity'],
            transmission=vehicle_data['transmission'],
            location=vehicle_data['location'],
            url=vehicle_data['url'],
            image_url=vehicle_data['image_url']
        )
        db.session.add(vehicle)
    
    db.session.commit()

print("Cleaned vehicle data loaded successfully.")

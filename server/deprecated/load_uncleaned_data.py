from models import db, UncleanedVehicle, app
import json

# Load uncleaned data from JSON
with open('used_car_data.json', 'r') as f:
    data = json.load(f)

# Ensure that the operations are performed within an application context
with app.app_context():
    # Insert data into the UncleanedVehicle table
    for item in data:
        vehicle = UncleanedVehicle(
            name=item['name'],
            price=item['price'],
            year=int(item['year']),
            mileage=item['mileage'],
            fuel_type=item['fuel_type'],
            engine_capacity=item['engine_capacity'],
            transmission=item['transmission'],
            location=item['location'],
            url=item['url'],
            image_url=item['image_url']
        )
        db.session.add(vehicle)

    db.session.commit()
    print("Uncleaned data loaded successfully.")

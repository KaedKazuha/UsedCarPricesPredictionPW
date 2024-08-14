import json
from models import db, Vehicle

# Load data from JSON file
with open('car_data.json') as f:
    car_data = json.load(f)

# Insert data into the database
for car in car_data:
    vehicle = Vehicle(
        make=car['make'],
        model=car['model'],
        year=int(car['year']),
        price=float(car['price'].replace('PKR ', '').replace(',', '')),
        price_display=car['price_display'],
        mileage=float(car['mileage'].replace(' km', '').replace(',', '')),
        fuel_type=car['fuel_type'],
        engine_capacity=car['engine_capacity'],
        transmission=car['transmission'],
        location=car['location'],
        url=car['url'],
        image_url=car['image_url']
    )
    db.session.add(vehicle)

db.session.commit()
print("Data loaded successfully!")

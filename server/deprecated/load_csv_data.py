import pandas as pd
from models import db, CleanedVehicle
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    df = pd.read_csv('data/better_cleaned_cars_data.csv')

    for _, row in df.iterrows():
        vehicle = CleanedVehicle(
            name=row['name'],
            price=row['price'],
            price_display=row['price_display'],
            year=row['year'],
            mileage=row['mileage'],
            fuel_type=row['fuel_type'],
            engine_capacity=row['engine_capacity'],
            transmission=row['transmission'],
            location=row['location'],
            url=row['url'],
            image_url=row['image_url']
        )
        db.session.add(vehicle)

    db.session.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()

# Model for uncleaned data
class UncleanedVehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.String(50), nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    engine_capacity = db.Column(db.String(50), nullable=False)
    transmission = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<UncleanedVehicle {self.name} {self.year}>'

# Model for cleaned vehicle data
class CleanedVehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    price_display = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.Float, nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    engine_capacity = db.Column(db.String(50), nullable=False)
    transmission = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<CleanedVehicle {self.name} {self.year}>'

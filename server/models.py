from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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


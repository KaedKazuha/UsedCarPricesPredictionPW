import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load the CSV file into a DataFrame
df = pd.read_csv('better_cleaned_cars_data.csv')

# Define the SQLite database and create an engine
engine = create_engine('sqlite:///car_prices.db', echo=True)
Base = declarative_base()

# Define the Car model based on your CSV columns
class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    price = Column(Float)
    mileage = Column(Float)
    fuel_type = Column(String)
    engine_capacity = Column(Float)
    transmission = Column(String)
    location = Column(String)

# Create the table
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into the table
for index, row in df.iterrows():
    car = Car(
        make=row['make'],
        model=row['model'],
        year=int(row['year']),
        price=float(row['price']),
        mileage=float(row['mileage']),
        fuel_type=row['fuel_type'],
        engine_capacity=float(row['engine_capacity']),
        transmission=row['transmission'],
        location=row['location']
    )
    session.add(car)

# Commit the session
session.commit()

# Close the session
session.close()

print("CSV data has been loaded into the SQLite database successfully.")

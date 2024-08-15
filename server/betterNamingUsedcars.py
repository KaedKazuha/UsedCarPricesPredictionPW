# latest one used
import pandas as pd
import re

# Load the dataset
df = pd.read_json('used_car_data.json')

# Function to clean car names
def clean_name(name):
    # Check for a year in the name and split before the year
    year_pattern = re.compile(r'\b(19|20)\d{2}\b')
    match = year_pattern.search(name)
    
    if match:
        # Special case handling for models like "Peugeot 2008"
        if 'Peugeot 2008' in name:
            return 'Peugeot 2008'
        # Otherwise, split before the year
        return name[:match.start()].strip()
    else:
        return name

# Apply the cleaning function to the name column
df['clean_name'] = df['name'].apply(clean_name)

# Split the cleaned name into make and model
df['make'] = df['clean_name'].apply(lambda x: x.split()[0])
df['model'] = df['clean_name'].apply(lambda x: ' '.join(x.split()[1:]) if len(x.split()) > 1 else '')

# Convert price to numeric
df['price'] = df['price'].replace({'PKR ': '', ',': ''}, regex=True).astype(float)

# Clean and convert engine capacity to numeric, handling empty strings or non-numeric values
df['engine_capacity'] = df['engine_capacity'].replace({'cc': ''}, regex=True)
df['engine_capacity'] = pd.to_numeric(df['engine_capacity'], errors='coerce')  # Convert to float, replace errors with NaN

# Clean and convert mileage to numeric, handling empty strings or non-numeric values
df['mileage'] = df['mileage'].replace({' km': '', ',': ''}, regex=True)
df['mileage'] = pd.to_numeric(df['mileage'], errors='coerce')  # Convert to float, replace errors with NaN

# Convert year to numeric
df['year'] = pd.to_numeric(df['year'], errors='coerce')

# Standardize categorical fields
df['transmission'] = df['transmission'].str.lower().str.capitalize()
df['fuel_type'] = df['fuel_type'].str.lower().str.capitalize()
df['location'] = df['location'].str.lower().str.capitalize()

# Drop irrelevant columns
df = df.drop(columns=['name', 'url', 'image_url', 'clean_name'])

# Handle missing data: fill or drop as needed
df = df.dropna()  # Drop rows with missing values

# Save the cleaned dataset
df.to_csv('better_cleaned_cars_data.csv', index=False)

print("Data cleaning complete. Saved to 'cleaned_cars_data.csv'")

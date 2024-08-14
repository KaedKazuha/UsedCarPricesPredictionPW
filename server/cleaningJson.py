# import pandas as pd
# import json

# # Load the JSON data
# with open('used_car_data.json', 'r') as f:
#     data = json.load(f)

# # Convert the JSON data to a DataFrame
# df = pd.DataFrame(data)

# # Remove 'LAC' from prices and convert them to decimal
# df['price'] = df['price'].replace({'PKR ': '', 'LAC': '00000', ',': ''}, regex=True).astype(float)

# # Format the price for display with commas and currency symbol
# df['price_display'] = df['price'].apply(lambda x: f"PKR {x:,.2f}")

# # Clean the 'mileage' column to remove ' km' and commas, then convert to numeric
# df['mileage'] = df['mileage'].replace({' km': '', ',': ''}, regex=True).astype(float)

# # Modify the 'name' column to only contain the first two words (make and model)
# df['name'] = df['name'].apply(lambda x: ' '.join(x.split()[:2]))

# # Group cars by the modified name and year
# grouped_df = df.groupby(['name', 'year']).agg({
#     'price': 'mean',
#     'price_display': 'first',  # Use the first formatted price for display
#     'mileage': 'mean',
#     'fuel_type': 'first',
#     'engine_capacity': 'first',
#     'transmission': 'first',
#     'location': 'first',
#     'url': 'first',
#     'image_url': 'first'
# }).reset_index()

# # Maintain the original ids by using the earliest id for each group
# grouped_df['id'] = df.groupby(['name', 'year'])['id'].min().values

# # Prepare the data to save back to JSON
# grouped_df['price'] = grouped_df['price'].round(2)
# grouped_df['mileage'] = grouped_df['mileage'].round(2)

# # Convert the DataFrame back to a dictionary
# cleaned_data = grouped_df.to_dict(orient='records')

# # Save the cleaned data to a new JSON file
# with open('cleaned_used_car_data.json', 'w') as f:
#     json.dump(cleaned_data, f, indent=4)

# print("Data cleaning and formatting complete. Saved to 'cleaned_used_car_data.json'")

import pandas as pd
import json

# Load the JSON data
with open('used_car_data.json', 'r') as f:
    data = json.load(f)

# Convert the JSON data to a DataFrame
df = pd.DataFrame(data)

# Remove 'PKR', 'LAC', and commas from prices and convert them to decimal
df['price'] = df['price'].replace({'PKR ': '', 'LAC': '00000', ',': ''}, regex=True).astype(float)

# Format the price for display with commas and currency symbol
df['price_display'] = df['price'].apply(lambda x: f"PKR {x:,.2f}")

# Clean the 'mileage' column to remove ' km' and commas, then convert to numeric
df['mileage'] = df['mileage'].replace({' km': '', ',': ''}, regex=True).astype(float)

# Modify the 'name' column to only contain the first two words (make and model)
df['name'] = df['name'].apply(lambda x: ' '.join(x.split()[:2]))

# No grouping or altering of IDs; just format and clean data as specified

# Convert the DataFrame back to a dictionary
cleaned_data = df.to_dict(orient='records')

# Save the cleaned data to a new JSON file
with open('cleaned_used_car_data.json', 'w') as f:
    json.dump(cleaned_data, f, indent=4)

print("Data cleaning and formatting complete. Saved to 'cleaned_used_car_data.json'")

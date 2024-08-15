import requests
from bs4 import BeautifulSoup
import json

# Base URL without the page number
base_url = 'https://www.pakwheels.com/new-cars/search/make_any/model_any/price_any_any/?sortby=price+ASC&page={}'

# Total number of pages to scrape
total_pages = 40

# List to store all car details
car_data = []

# ID counter for unique IDs
car_id = 1

# Loop through all pages
for page in range(1, total_pages + 1):
    # Create the full URL with the current page number
    url = base_url.format(page)
    
    # Send a request to fetch the HTML content of the current page
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the car listings on the current page
        car_listings = soup.find_all('div', class_='new-car-box')
        
        # Iterate over each car listing and extract details
        for car in car_listings:
            # Extract details
            car_name = car.find('a', class_='car-name').text.strip()
            price_details = car.find('div', class_='price-details').text.strip()
            engine_details = car.find('div', class_='generic-gray mt10').text.strip()
            
            # Split engine details to extract transmission and fuel type separately
            details_parts = engine_details.split('|')
            transmission = details_parts[0].strip() if len(details_parts) > 0 else "Unknown"
            fuel_type = details_parts[1].strip() if len(details_parts) > 1 else "Unknown"
            engine_capacity = details_parts[2].strip() if len(details_parts) > 2 else "Unknown"
            
            car_url = car.find('a', class_='car-name')['href']
            image_tag = car.find('div', class_='img-box').find('img')
            image_url = image_tag['src'] if image_tag else None
            rating = car.find('span', class_='rating').text.strip() if car.find('span', class_='rating') else 'No rating'
            
            # Construct a dictionary for each car
            car_details = {
                "id": car_id,
                "name": car_name,
                "price": price_details,
                "engine_capacity": engine_capacity,
                "transmission": transmission,
                "fuel_type": fuel_type,
                "url": f"https://www.pakwheels.com{car_url}",
                "image_url": image_url,
                "rating": rating
            }
            
            # Add the car details to the main list
            car_data.append(car_details)
            
            # Increment the car ID for the next car
            car_id += 1
    else:
        print(f"Failed to retrieve page {page}")

# Convert the list of car data to JSON
car_data_json = json.dumps(car_data, indent=4)

# Save to a JSON file or print to console
with open('car_data.json', 'w') as json_file:
    json_file.write(car_data_json)

print(car_data_json)

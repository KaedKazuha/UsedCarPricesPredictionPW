import requests
from bs4 import BeautifulSoup
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

# Base URL without the page number
base_url = 'https://www.pakwheels.com/used-cars/search/-/?page={}'

# Total number of pages to scrape
total_pages = 2477

# List to store all car details
car_data = []

# ID counter for unique IDs
car_id = 1

# Function to scrape a single page
def scrape_page(page):
    global car_id
    url = base_url.format(page)
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        car_listings = soup.find_all('li', class_='classified-listing')
        page_data = []
        
        for car in car_listings:
            json_script = car.find('script', type='application/ld+json')
            if json_script:
                json_data = json_script.string
                car_info = json.loads(json_data)
                
                car_name = car_info.get("name", "No name available")
                price = car_info.get("offers", {}).get("price", "No price available")
                currency = car_info.get("offers", {}).get("priceCurrency", "No currency available")
                price = f"{currency} {price:,}"
                car_url = car_info.get("offers", {}).get("url", "No URL available")
                image_url = car_info.get("image", "No image available")
                engine_capacity = car_info.get("vehicleEngine", {}).get("engineDisplacement", "No engine capacity available")
                fuel_type = car_info.get("fuelType", "No fuel type available")
                transmission = car_info.get("vehicleTransmission", "No transmission available")
                mileage = car_info.get("mileageFromOdometer", "No mileage available")
                location = car.find('ul', class_='search-vehicle-info').find('li').text.strip() if car.find('ul', class_='search-vehicle-info') else "No location available"
                year = car.find('ul', class_='search-vehicle-info-2').find_all('li')[0].text.strip() if car.find('ul', class_='search-vehicle-info-2') else "No year available"

                car_details = {
                    "id": car_id,
                    "name": car_name,
                    "price": price,
                    "year": year,
                    "mileage": mileage,
                    "fuel_type": fuel_type,
                    "engine_capacity": engine_capacity,
                    "transmission": transmission,
                    "location": location,
                    "url": car_url,
                    "image_url": image_url
                }
                
                page_data.append(car_details)
                car_id += 1
            else:
                print(f"Warning: JSON data not found for a listing on page {page}. Skipping this listing.")
        
        return page_data
    else:
        print(f"Failed to retrieve page {page}")
        return []

# Function to handle threading
def scrape_all_pages_concurrently():
    with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust `max_workers` to control the level of concurrency
        future_to_page = {executor.submit(scrape_page, page): page for page in range(1, total_pages + 1)}
        
        for future in as_completed(future_to_page):
            page = future_to_page[future]
            try:
                data = future.result()
                car_data.extend(data)
                print(f"Completed scraping page {page}")
            except Exception as exc:
                print(f"Page {page} generated an exception: {exc}")

# Scrape all pages concurrently
scrape_all_pages_concurrently()

# Convert the list of car data to JSON
car_data_json = json.dumps(car_data, indent=4)

# Save to a JSON file
with open('used_car_data.json', 'w') as json_file:
    json_file.write(car_data_json)

print("Scraping completed.")

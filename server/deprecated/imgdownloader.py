import os
import json
import requests
from urllib.parse import urlparse

# Load the JSON data
with open('cleaned_used_car_data.json', 'r') as f:
    data = json.load(f)

# Create a directory to save the images
image_folder = 'vehicle_images'
os.makedirs(image_folder, exist_ok=True)

# Function to download an image
def download_image(url, folder):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Extract the image name from the URL
        image_name = os.path.basename(urlparse(url).path)
        image_path = os.path.join(folder, image_name)

        # Save the image to the specified folder
        with open(image_path, 'wb') as f:
            f.write(response.content)

        return image_path
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None

# Update the JSON data with local paths
for vehicle in data:
    image_url = vehicle.get('image_url')
    if image_url:
        local_image_path = download_image(image_url, image_folder)
        if local_image_path:
            vehicle['image_url'] = local_image_path

# Save the updated JSON data
with open('cleaned_used_car_data_with_local_images.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Images downloaded and JSON updated successfully.")

import os
import csv
import requests
from concurrent.futures import ThreadPoolExecutor
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def download_image(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response:
                file.write(chunk)

def process_row(row, index, total):
    url = row['image_link']
    filename = os.path.join('images', os.path.basename(url))
    download_image(url, filename)
    logging.info(f"Downloaded {index + 1}/{total}")

def main():
    # Create the images directory if not exists
    os.makedirs('images', exist_ok=True)

    with open('vogue_image_data - all.csv', 'r') as file:
        # Use DictReader to automatically read header
        reader = csv.DictReader(file)
        rows = list(reader)  # Convert iterator to list to get the length
        total = len(rows)
        logging.info(f"Total images to download: {total}")
        with ThreadPoolExecutor(max_workers=4) as executor:
            # Use enumerate to get the index (i) along with the row
            for i, row in enumerate(rows):
                executor.submit(process_row, row, i, total)

if __name__ == "__main__":
    main()

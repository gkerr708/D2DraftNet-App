import os
import time
import requests
from bs4 import BeautifulSoup

# Liquipedia URL containing hero icons
CATEGORY_URL = 'https://liquipedia.net/commons/Category:Dota_2_hero_icons'
BASE_URL = 'https://liquipedia.net'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

# Directory to save images
SAVE_DIR = 'hero_icons'
os.makedirs(SAVE_DIR, exist_ok=True)

def get_hero_icon_links():
    """Scrapes the category page to find all hero icon URLs."""
    response = requests.get(CATEGORY_URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    image_elements = soup.select('.gallerytext a')
    return [BASE_URL + img['href'] for img in image_elements]

def download_hero_icon(hero_page_url):
    """Extracts and downloads the hero icon from its specific page."""
    response = requests.get(hero_page_url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tag = soup.find('div', class_='fullImageLink')
    if img_tag and img_tag.a:
        img_url = BASE_URL + img_tag.a['href']
        img_name = img_url.split('/')[-1]
        
        img_data = requests.get(img_url).content
        with open(os.path.join(SAVE_DIR, img_name), 'wb') as img_file:
            img_file.write(img_data)
            print(f'Downloaded {img_name}')
        
        time.sleep(1)  # Delay to avoid hitting the server too quickly

def main():
    print("Fetching hero icons...")
    hero_links = get_hero_icon_links()
    
    for hero_link in hero_links:
        download_hero_icon(hero_link)
    
    print("All hero icons downloaded.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import os

# Define headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# URL of the page to scrape
url = 'https://www.transfermarkt.com/some-team/squad'

# Send request to the page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all player links
player_links = soup.find_all('a', class_='spielprofil_tooltip')

# Create directory to save images
if not os.path.exists('player_images'):
    os.makedirs('player_images')

for player in player_links:
    player_url = 'https://www.transfermarkt.com' + player['href']
    player_page = requests.get(player_url, headers=headers)
    player_soup = BeautifulSoup(player_page.content, 'html.parser')

    # Find player image
    img_tag = player_soup.find('img', class_='bilderrahmen-fixed')
    img_url = img_tag['src']

    # Save the image
    img_data = requests.get(img_url, headers=headers).content
    player_name = player.text.strip().replace(" ", "_")
    with open(f'player_images/{player_name}.jpg', 'wb') as handler:
        handler.write(img_data)

print("Images saved successfully.")


# In[2]:


import requests
from bs4 import BeautifulSoup
import os

# Define headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# URL of the page to scrape
url = 'https://www.transfermarkt.com/some-team/squad'

# Send request to the page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all player links
player_links = soup.find_all('a', class_='spielprofil_tooltip')

# Define the path to the Downloads directory
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'player_images')

# Create directory to save images if it doesn't exist
if not os.path.exists(downloads_path):
    os.makedirs(downloads_path)

for player in player_links:
    player_url = 'https://www.transfermarkt.com' + player['href']
    player_page = requests.get(player_url, headers=headers)
    player_soup = BeautifulSoup(player_page.content, 'html.parser')

    # Find player image
    img_tag = player_soup.find('img', class_='bilderrahmen-fixed')
    if img_tag:
        img_url = img_tag['src']
        print(f"Image URL: {img_url}")  # Debugging line

        # Save the image
        img_data = requests.get(img_url, headers=headers).content
        player_name = player.text.strip().replace(" ", "_")
        with open(os.path.join(downloads_path, f'{player_name}.jpg'), 'wb') as handler:
            handler.write(img_data)
    else:
        print(f"No image found for {player.text.strip()}")

print("Images saved successfully in Downloads directory.")


# In[3]:


import requests
from bs4 import BeautifulSoup
from os.path  import basename


# In[4]:


headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


# In[2]:


import requests
from bs4 import BeautifulSoup
import os

# URL of the website (example)
url = "https://www.premierleague.com/players"

# Create a directory to save images
if not os.path.exists('player_images'):
    os.makedirs('player_images')

# Sending a request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Finding all player image tags
players = soup.find_all('div', class_='playerOverviewCard')

# Loop through players and extract image URLs
for player in players:
    img_tag = player.find('img')
    if img_tag:
        img_url = img_tag['src']
        player_name = player.find('h4').text.strip()
        # Downloading the image
        img_data = requests.get(img_url).content
        with open(f'player_images/{player_name}.jpg', 'wb') as handler:
            handler.write(img_data)
        print(f"Downloaded image for {player_name}")

print("Images are saved in the 'player_images' directory.")


# In[4]:


import requests
from bs4 import BeautifulSoup
import os

# URL of the website (example)
url = "https://www.premierleague.com/players"

# Define the path to the Downloads directory
downloads_path = r"C:\Users\jeyar\Downloads\player_images"

# Create a directory to save images in Downloads
if not os.path.exists(downloads_path):
    os.makedirs(downloads_path)

# Sending a request to the website
response = requests.get(url)
if response.status_code == 200:
    print("Successfully fetched the webpage")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")

soup = BeautifulSoup(response.text, 'html.parser')

# Finding all player image tags
players = soup.find_all('div', class_='playerOverviewCard')
print(f"Found {len(players)} player cards")

# Check if player cards were found
if not players:
    print("No player cards found. Please check the structure of the webpage.")

# Loop through players and extract image URLs
for player in players:
    img_tag = player.find('img')
    if img_tag:
        img_url = img_tag['src']
        player_name = player.find('h4').text.strip()
        print(f"Found image for {player_name} at {img_url}")
        # Downloading the image
        img_data = requests.get(img_url).content
        with open(os.path.join(downloads_path, f'{player_name}.jpg'), 'wb') as handler:
            handler.write(img_data)
        print(f"Downloaded image for {player_name}")
    else:
        print("No image tag found for a player card")

print(f"Images are saved in the '{downloads_path}' directory.")


# In[10]:


len(playerLinks)


# In[ ]:





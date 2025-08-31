
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string

url = "https://www.example.com"
title = scrape_website(url)
print("Website Title:", title)

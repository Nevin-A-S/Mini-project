import requests
from bs4 import BeautifulSoup
import random
import re

def scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find(id="firstHeading")
    title = 'None'

    # all_links = soup.find(id="bodyContent").find_all("a")
    # random.shuffle(all_links)
    # link_to_scrape = set()
    
    paragraphs = soup.find_all("p")
    content = []
    for para in paragraphs:
        content.append(para.get_text())
    
    content_cleaned = [re.sub(r'\[\d+\]', '', para) for para in content]
    
    
    # for link in all_links:
        
    #     if 'href' not in link.attrs:
    #         continue
        
    #     if link['href'].find("/wiki/") == -1: 
    #         continue

    #     link_to_scrape.add(link['href'])

    return content_cleaned
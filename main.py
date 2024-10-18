import requests
from bs4 import BeautifulSoup


URL = 'https://www.theguardian.com/technology/2024/oct/15/oura-ring-4-review-best-smart-ring-battery-upgrade'

r = requests.get(URL)

soup = BeautifulSoup(r.text, 'html.parser')
text = soup.get_text()
print(text)
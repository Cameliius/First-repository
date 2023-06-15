import requests
from bs4 import BeautifulSoup

response = requests.get('https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets')
response = response.content
html = BeautifulSoup(response, 'html.parser')
computers = html.find_all('div', class_='row ecomerce-items ecomerce-items-ajax')
for computer in computers:
    print(computer.attrs['data-items'])

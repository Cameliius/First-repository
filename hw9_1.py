import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.columbia.edu/~fdc/sample.html')
response = response.content
html = BeautifulSoup(response, 'html.parser')
result = []
headers = html.find_all('h3')
for header in headers:
    for content in header.contents:
        result.append(content)
print(result)

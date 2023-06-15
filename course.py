import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

payload = {"date_req": today}

response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, 'html.parser')

money = {'EUR': 'R01239', 'USD': 'R01235', 'AUD': 'R01010', 'GBP': 'R01035', 'BYR': 'R01090', 'DKK': 'R01215',
         "ISK": 'R01310', 'KZT': 'R01335'}


def get_course(currency):
    currency = currency.upper()
    if currency in money:
        return str(xml.find("valute", {'id': money.get(currency)}).value.text)

import requests
from bs4 import BeautifulSoup


def Course_in_year(id, year):
    url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=31/12/' + year
    responce = requests.get(url)
    xml = BeautifulSoup(responce.content, 'html.parser')
    return xml.find('valute', {'id': id}).value.text


year = input('Введите год: ')
print(Course_in_year('R01235', year), 'рублей за 1 доллар в', year)
print(Course_in_year('R01820', year), 'рублей за 1 иен в', year)
print(Course_in_year('R01350', year), 'рублей за 1 канадский доллар в', year)

year = input('Введите год: ')
print(Course_in_year('R01235', year), 'рублей за 1 доллар в', year)
print(Course_in_year('R01820', year), 'рублей за 1 иен в', year)
print(Course_in_year('R01350', year), 'рублей за 1 канадский доллар в', year)

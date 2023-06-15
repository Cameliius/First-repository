import requests
from bs4 import BeautifulSoup


def getValutes():
    valutes = dict()
    url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=29/01/2023'
    responce = requests.get(url)
    xml = BeautifulSoup(responce.content, 'html.parser')
    for valute in xml.findAll('valute'):
        valuteId = valute.attrs.get('id')
        valuteCharCode = valute.find('charcode').text
        valutes[valuteCharCode] = valuteId

    return valutes


def getCourse(id):
    url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=29/01/2023'
    responce = requests.get(url)
    xml = BeautifulSoup(responce.content, 'html.parser')
    result = xml.find('valute', {'id': id}).value.text
    result = result.replace(',', '.')
    return float(result)


def course(valute_from, valute_to, amount):
    valutes = getValutes()
    if valute_from == 'RUR':
        course_from = 1
    else:
        course_from = getCourse(valutes.get(valute_from))

    if valute_to == 'RUR':
        course_to = 1
    else:
        course_to = getCourse(valutes.get(valute_to))
    result = course_from * amount / course_to

    return result


print(course(valute_from=input('Введите код валюты из которой перевести: '),
             valute_to=input('Введите код валюты, в которую перевести: '),
             amount=int(input('Введите сумму, которую хотите сконвертировать: '))))

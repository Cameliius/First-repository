from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime

window = Tk()
window.title('Курс валют')
window.geometry('400x400')
window['bg'] = 'misty rose'

url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='


def getCourse(id):
    response = requests.get(url)
    xml = BeautifulSoup(response.content, 'html.parser')
    valute = xml.find('valute', {'id': id})
    return valute.value.text


title = Label(window, text='Курс валют\nMAXIMUM Банк', bg='salmon1', fg='black', font='Arial 22')
title.place(x=170, y=25)

today = datetime.today()
today = today.strftime('%d.%m.%Y')
date_info = Label(window, text='Курс на ' + today, bg='salmon1', font='Arial 15')
date_info.place(x=105, y=170)

usd_course = Label(window, text='USD ' + getCourse('R01235'), bg='salmon1', font='Arial 25')
usd_course.place(y=220, x=100)

eur_course = Label(window, text='EUR ' + getCourse('R01239'), bg='salmon1', font='Arial 25')
eur_course.place(y=270, x=100)

cny_course = Label(window, text='CNY ' + getCourse('R01375'), bg='salmon1', font='Arial 25')
cny_course.place(y=320, x=100)

img_logo = PhotoImage(file='logo.png')
logo = Label(window, bg='salmon1', image=img_logo)
logo.place(y=0, x=0)

window.resizable(False, False)
window.mainloop()

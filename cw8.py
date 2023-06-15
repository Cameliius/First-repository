from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime

window = Tk()
window.title('Курс валют')
window.geometry('400x400')

url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='

def getCourse(id):
    response = requests.get(url)
    xml = BeautifulSoup(response.content, 'html.parser')
    valute = xml.find('valute', {'id': id})
    return valute.value.text

title = Label(window, text='Курс валют\nMAXIMUM Банк', bg='orange', fg='black', font='Arial 22')
title.place(x=150, y=25)


today = datetime.today()
today = today.strftime('%d.%m.%Y')
date_info = Label(window, text='Курс на ' + today, font='Arial 15')
date_info.place(x=105, y=160)



usd_course = Label(window, text='USD'+getCourse('R01235'), font='Arial 25')
usd_course.place(y=200, x=100)

eur_course = Label(window, text='EUR'+getCourse('R01239'), font='Arial 25')
eur_course.place(y=250, x=100)

img_logo = PhotoImage(file='logo.png')
logo = Label(window, image=img_logo)
logo.place(y=0, x=0)


print(getCourse('R01235'))
window.mainloop()









# count = 0
#
# def click():
#     global count
#     count = count + 1
#     label['text'] = count
#
# label = Label(window, text='Здесь что-то написано', bg='#FF6666', fg='gold', font='20')
# label.place(x=200, y=100)
#
# btn = Button(window, text='Нажми на меня', background='#555', font='20', command=click)
# btn.place(x=200, y=220)

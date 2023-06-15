from tkinter import *
import random
import requests
from bs4 import BeautifulSoup
from tkhtmlview import HTMLLabel

window = Tk()
window.title('Котики и аниме')
window.geometry('700x600')


def draw_menu():
    clear()
    label_title = Label(text='Что бы вы хотели сделать?', font=('Arial', 24), fg='white', bg='orange')
    label_title.place(width=700, height=50, x=0, y=0)
    b_1 = Button(text='Посмотреть новое аниме', font=('Arial', 18), fg='black', command=get_anime)
    b_1.place(x=25, y=75, width=300)

    b_2 = Button(text='Посмотреть на котиков', font=('Arial', 18), fg='black', command=get_img)
    b_2.place(x=375, y=75, width=300)


def get_anime():
    clear()
    reponse = requests.get('https://animego.org/anime')
    reponse = reponse.content
    html = BeautifulSoup(reponse, 'html.parser')
    anime = html.find_all(class_='h5')
    result = []
    for one_anime in anime:
        if one_anime.a:
            url = one_anime.a.attrs['href']
            name = one_anime.text
            result.append([name, url])
    ani = random.choice(result)
    label = HTMLLabel(html=f'<a href="{ani[1]}">{ani[0]}</a>')
    label.place(x=20, y=300)
    draw_home_button()


def get_img():
    clear()
    photo1 = PhotoImage(file='cat1.png')
    l1 = Label(image=photo1)
    l1.image = photo1
    l1.place(x=10, y=100)

    photo2 = PhotoImage(file='cat3.png')
    l2 = Label(image=photo2)
    l2.image = photo2
    l2.place(x=350, y=100)


def clear():
    all_widgets = window.place_slaves()
    for l in all_widgets:
        l.destroy()
    draw_home_button()


def draw_home_button():
    b = Button(text='Домой', font=('Arial', 24), fg='black', command=draw_menu)
    b.place(x=25, y=500, width=150)


draw_menu()

window.mainloop()

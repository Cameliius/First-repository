from tkinter import *
from random import randint

window = Tk()
window.geometry('600x600')


class Fire:
    image = PhotoImage(file='free-icon-fire-9509865.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay
        elif isinstance(other, Wind):
            return Aroma


class Wind:
    image = PhotoImage(file='wind.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Dust
        elif isinstance(other, Fire):
            return Aroma


class Earth:
    image = PhotoImage(file='ground.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay
        elif isinstance(other, Wind):
            return Dust


class Water:
    image = PhotoImage(file='free-icon-water-drop-4246703.png').subsample(4, 4)


class Clay:
    image = PhotoImage(file='free-icon-pottery-7942410.png').subsample(4, 4)


class Dust:
    image = PhotoImage(file='free-icon-dust-2396941.png').subsample(4, 4)


class Aroma:
    image = PhotoImage(file='aroma.png').subsample(4, 4)


canvas = Canvas(window, width=600, height=600)
canvas.pack()

elements = [Fire(), Earth(), Wind(), Water()]

for elem in elements:
    img = canvas.create_image(randint(50, 550), randint(50, 550), image=elem.image)


def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    if len(images_id) == 2:
        element_1 = elements[images_id[0] - 1]
        element_2 = elements[images_id[1] - 1]
        new_element = element_1 + element_2
        print(new_element)
        if new_element:
            if new_element not in elements:
                canvas.create_image(event.x, event.y, image=new_element.image)
                elements.append(new_element)

    canvas.coords(images_id, event.x, event.y)

    print(images_id)


window.bind('<B1-Motion>', move)
window.mainloop()

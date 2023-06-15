from tkinter import *

window = Tk()
window.geometry('800x600')

canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack()


canvas.create_rectangle(10, 10, 300, 300, fill='yellow', outline='')
canvas.create_rectangle(10, 10, 200, 200, fill='red', outline='')
canvas.create_rectangle(10, 10, 100, 100, fill='pink', outline='')
canvas.create_polygon(10, 180, 60, 120, 110, 180, fill='green', outline='')

class Figure:
    def __init__(self, name, color):
        self.name = name
        self.color = color

# figure_1 = Figure('Rectangle', 'Yellow')
# figure_2 = Figure('Rectangle', 'Red')
# figure_3 = Figure('Rectangle', 'Pink')
# figure_4 = Figure('Triangle', 'Green')
window.mainloop()
# from tkinter import *
#
# window = Tk()
# window.geometry('800x600')
#
#
# class Figure:
#     def __init__(self, window, color1, color2, color3, color4):
#         self.canvas = Canvas(window, width=800, height=600, bg='white')
#         self.canvas.pack()
#         self.canvas.create_rectangle(10, 10, 300, 300, fill=color1, outline='')
#         self.canvas.create_rectangle(10, 10, 200, 200, fill=color2, outline='')
#         self.canvas.create_rectangle(10, 10, 100, 100, fill=color3, outline='')
#         self.canvas.create_polygon(10, 180, 60, 120, 110, 180, fill=color4, outline='')
#
#
# figurka = Figure(window=window, color1='yellow', color2='red', color3='purple', color4='black')
# window.mainloop()


import random
a = random.randint(1,10)

print(a)
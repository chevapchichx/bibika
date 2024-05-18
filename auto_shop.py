import sqlite3
import tkinter as tk

from tkinter import *
from PIL import Image, ImageTk
import auto_manager
import auto_bibiki

con = sqlite3.connect("auto_shop.db")

window_main = Tk()
window_main.title("bibika.ru")
window_main.geometry('850x600')
window_main.resizable(False, False)  # Make the window non-resizable

frame = Frame(
   window_main,
   padx=10,
   pady=10
)
frame.pack(expand=True)

# image = Image.open("main_photo.jpg")
# photo = ImageTk.PhotoImage(image)
# label = Label(window, image=photo)
# label.pack()

path = 'main_photo.jpg'

image = Image.open(path)
width = 850
height = 600
image = ImageTk.PhotoImage(image)

canvas = tk.Canvas(window_main, width=width, height=height)
canvas.pack(side="top", fill="both", expand="no")
canvas.create_image(0, 0, anchor="nw", image=image)

auto_go_btn = Button(
   window_main,
   text="Выбрать бибику",
   command=auto_bibiki.bibiki_contents_window,
   bg="#CDAA7D",
   fg="#6E7B8B",
   font=("comic sans", 16),
   relief="flat",
   borderwidth=0,
)
canvas.create_window((90, 500), anchor="nw", window=auto_go_btn)

manager_go_btn = Button(
   window_main,
   text="Личный кабинет",
   command=auto_manager.auth_lk_window,
   bg="#CDAA7D",
   fg="#6E7B8B",
   font=("comic sans", 11),
   relief="flat",
   borderwidth=0,
)
canvas.create_window((30, 10),anchor="nw", window=manager_go_btn, width=97, height=25)

window_main.mainloop()






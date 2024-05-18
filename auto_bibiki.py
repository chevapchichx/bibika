import sqlite3
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


def bibiki_contents_window():
    bibiki = get_bibiki()
    window_bibiki_cont = Tk()
    window_bibiki_cont.title("bibiki")
    window_bibiki_cont.geometry('250x125')
    # window_bibiki_cont.configure(bg='#6E7B8B')

    frame = Frame(
        window_bibiki_cont,
        padx=10,
        pady=10
    )
    frame.pack(expand=True)

    for i in range(0, len(bibiki)):
        bibiki_lb = Button(
            frame,
            text=f"{bibiki[i][1]} {bibiki[i][2]}",
            font=("comic sans", 14),
            bg="#CDAA7D",
            fg="#6E7B8B",
            borderwidth=0,
            width=12,
            height=1,
            command=lambda i=i: bibika_window(bibiki[i]),
        )
        bibiki_lb.grid(row=i, column=0, columnspan=3)

    window_bibiki_cont.mainloop()


def get_bibiki():
    with sqlite3.connect("auto_shop.db") as BD:
        cursor = BD.cursor()
        cursor.execute("SELECT ID_A, Brand, Model, Price, Photo, Description FROM auto")
        bibiki = cursor.fetchall()
        return bibiki


def bibika_window(bibiki):
    bibiki = get_bibiki()
    window_bibika = Tk()
    window_bibika.title(f"{bibiki[1]} {bibiki[2]}")
    window_bibika.geometry('250x125')
    window_bibika.resizable(False, False)

    frame = Frame(
        window_bibika,
        padx=10,
        pady=10
    )
    frame.pack(expand=True)

    # image = Image.open(bibiki[4])
    # photo = ImageTk.PhotoImage(image)
    #
    # label = Label(frame, image=photo)
    # label.image = photo
    # label.pack()
gggg





# bibiki_contents_window()
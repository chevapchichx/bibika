import sqlite3
import tkinter as tk
from tkinter import Tk, Toplevel, Frame, Button
from io import BytesIO
from PIL import Image, ImageTk
from tkinter import messagebox


def bibiki_contents_window():
    bibiki = get_bibiki()
    window_bibiki_cont = Toplevel()
    window_bibiki_cont.title("bibiki")
    window_bibiki_cont.geometry('850x600')
    window_bibiki_cont.grab_set()
    window_bibiki_cont.resizable(False, False)

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
        cursor.execute("SELECT ID_A, Brand, Model, Price, Description FROM auto")
        bibiki = cursor.fetchall()
        return bibiki


def get_image_from_db(bibiki):
    conn = sqlite3.connect('auto_shop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Photo FROM auto WHERE ID_A = ?", (bibiki[0],))
    image_data = cursor.fetchone()[0]
    conn.close()
    return image_data


def bibika_window(bibiki):
    window_bibika = Toplevel()
    window_bibika.grab_set()
    window_bibika.title(f"{bibiki[1]} {bibiki[2]}")
    window_bibika.geometry('850x600')
    window_bibika.configure(bg='#696969')
    window_bibika.resizable(False, False)

    frame = Frame(
        window_bibika,
        padx=0,
        pady=0
    )
    frame.grid(sticky='n')

    image_data = get_image_from_db(bibiki)
    image_data_io = BytesIO(image_data)
    image = Image.open(image_data_io)
    photo = ImageTk.PhotoImage(image)

    bibiki_photo = tk.Label(
        frame,
        image=photo,
        width=850,
        height=500,
        borderwidth=0
    )
    bibiki_photo.image = photo
    bibiki_photo.grid()

    phone_man_lb = tk.Label(
        frame,
        text="Номер телефона",
        bg='#6E7B8B'
    )
    phone_man_lb.grid(row=3, column=1)





bibiki_contents_window()



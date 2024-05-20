import sqlite3
import tkinter as tk
from tkinter import Tk, Toplevel, Frame, Button, Label
from io import BytesIO
from PIL import Image, ImageTk
from tkinter import messagebox


def bibiki_contents_window(parent_frame, main_window_open, main_window_func):
    parent_frame.title("bibiki")
    parent_frame.grab_set()

    bibiki = get_bibiki()

    frame = Frame(
        parent_frame,
        padx=0,
        pady=0,
    )
    frame.pack(expand=True)

    def open_bibika_window(i):
        for widget in parent_frame.winfo_children():
            widget.destroy()
        bibika_window(parent_frame, bibiki[i], bibiki_contents_window, main_window_func)

    for i in range(0, len(bibiki)):
        bibiki_btn = Button(
            frame,
            text=f"{bibiki[i][1]} {bibiki[i][2]}",
            font=("comic sans", 14),
            fg="#6E7B8B",
            borderwidth=0,
            width=20,
            height=2,
            command=lambda i=i: open_bibika_window(i),
        )
        bibiki_btn.pack(pady=10)

    def go_back_1():
        parent_frame.destroy()
        main_window_func()

    back_btn = Button(
        frame,
        text="Назад",
        command=go_back_1,
        bg="#CDAA7D",
        fg="#6E7B8B",
        font=("comic sans", 11),
        relief="flat",
        borderwidth=0,
        width=6,
        height=1,
    )
    back_btn.pack(side="bottom", pady=10)


def get_bibiki():
    with sqlite3.connect("db/auto_shop.db") as BD:
        cursor = BD.cursor()
        cursor.execute("SELECT ID_A, Brand, Model, Price, Description FROM auto")
        bibiki = cursor.fetchall()
        return bibiki


def get_image_from_db(bibiki):
    conn = sqlite3.connect('db/auto_shop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Photo FROM auto WHERE ID_A = ?", (bibiki[0],))
    image_data = cursor.fetchone()[0]
    conn.close()
    return image_data


def bibika_window(parent_frame, bibiki, bibiki_c_window_open, main_window_func):
    parent_frame.title(f"{bibiki[1]} {bibiki[2]}")
    parent_frame.geometry('850x600')
    parent_frame.grab_set()
    parent_frame.resizable(False, False)

    frame = Frame(
        parent_frame,
        padx=0,
        pady=0,
    )
    frame.pack()

    image_data = get_image_from_db(bibiki)
    image_data_io = BytesIO(image_data)
    image = Image.open(image_data_io)
    photo = ImageTk.PhotoImage(image)

    bibika_photo = Label(
        frame,
        image=photo,
        width=850,
        height=500,
        borderwidth=0,
    )
    bibika_photo.image = photo
    bibika_photo.pack()

    bibika_price_lb = Label(
        frame,
        text=f"Цена: {str(bibiki[3])} рублей",
        fg='#FFF5EE',
        font=("comic sans", 16),
        wraplength=800,
        justify="left",

    )
    bibika_price_lb.pack(pady=10)

    bibika_desc_lb = Label(
        frame,
        text=f"{str(bibiki[4])}",
        fg='#FFF5EE',
        font=("comic sans", 16),
        wraplength=800,
        justify="left"
    )
    bibika_desc_lb.pack(pady=10)

    def go_back_2():
        for widget in parent_frame.winfo_children():
            widget.destroy()
        bibiki_c_window_open(parent_frame, bibiki_c_window_open, main_window_func)

    back_btn = Button(
        frame,
        text="Назад",
        command=go_back_2,
        bg="#CDAA7D",
        fg="#6E7B8B",
        font=("comic sans", 11),
        relief="flat",
        borderwidth=0,
        width=6,
        height=1,
    )
    back_btn.place(x=750, y=555)


def bibiki_change_window(window_bibiki_change, main_window_func):
    window_bibiki_change.title('my bibikas')
    window_bibiki_change.geometry('850x600')
    window_bibiki_change.resizable(False, False)

    frame = Frame(
        window_bibiki_change,
        padx=0,
        pady=0,
    )
    frame.pack()

    def go_back_3():
        window_bibiki_change.destroy()
        main_window_func()

    back_btn = Button(
        window_bibiki_change,
        text="Назад",
        command=go_back_3,
        bg="#CDAA7D",
        fg="#6E7B8B",
        font=("comic sans", 11),
        relief="flat",
        borderwidth=0,
        width=6,
        height=1,
    )
    back_btn.place(x=750, y=555)
    back_btn.lift()

# bibiki_contents_window(parent_frame=tk.Tk())

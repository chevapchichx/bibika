import tkinter as tk
import sqlite3
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Button

import auto_bibiki
import auto_manager

global window_main, canvas


def add_my_bibiki_button(window_main, canvas, login, password):
    user = auto_manager.get_auth(login, password)
    if user:
        my_bibiki_btn = Button(
            window_main,
            text=f"{user[2]}",
            command=lambda: auto_manager.info_man_window(user),
            fg="#6E7B8B",
            font=("comic sans", 11),
            relief="flat",
            borderwidth=0,
        )
        canvas.create_window((820, 10), anchor="ne", window=my_bibiki_btn, width=120, height=25)


def main_window():
    window_main = Tk()
    window_main.title("bibika.ru")
    window_main.geometry('850x600')
    window_main.resizable(False, False)

    frame = Frame(window_main, padx=0, pady=0)
    frame.pack(expand=True, fill="both")

    path = 'photos/main_photo.jpg'

    image = Image.open(path)
    image = ImageTk.PhotoImage(image)

    canvas = tk.Canvas(window_main, width=850, height=600)
    canvas.pack(side="top", fill="both", expand="no")
    canvas.create_image(0, 0, anchor="nw", image=image)

    def open_bibiki_contents_window():
        for widget in window_main.winfo_children():
            widget.destroy()
        auto_bibiki.bibiki_contents_window(window_main, open_bibiki_contents_window, main_window)

    auto_go_btn = Button(
        window_main,
        text="Выбрать бибику",
        command=open_bibiki_contents_window,
        fg="#6E7B8B",
        font=("comic sans", 16),
        relief="flat",
        borderwidth=0,
    )
    canvas.create_window((90, 500), anchor="nw", window=auto_go_btn)

    manager_go_btn = Button(
        window_main,
        text="Личный кабинет",
        command=lambda: auto_manager.auth_lk_window(
            lambda login, password: add_my_bibiki_button(window_main, canvas, login, password)),
        fg="#6E7B8B",
        font=("comic sans", 11),
        relief="flat",
        borderwidth=0,
    )
    canvas.create_window((30, 10), anchor="nw", window=manager_go_btn, width=115, height=25)

    window_main.mainloop()


main_window()

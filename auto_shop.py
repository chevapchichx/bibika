import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Button

import auto_bibiki
import auto_manager


def add_info_man_button(window_main, canvas, login, password):
    user = auto_manager.get_auth(login, password)
    if user:
        global info_man_go_btn
        info_man_go_btn = Button(
            window_main,
            text=f"{user[2]}",
            command=lambda: auto_manager.info_man_window(user, main_window, window_main),
            fg="#6E7B8B",
            font=("comic sans", 11),
            relief="flat",
            borderwidth=0,
        )
        canvas.create_window((30, 10), anchor="nw", window=info_man_go_btn, width=115, height=25)


def open_bibiki_change_window():
    for widget in window_main.winfo_children():
        widget.destroy()
    auto_bibiki.bibiki_change_window(window_main, main_window)


def add_bibiki_change_button(window_main, canvas):
    global bibiki_change_go_btn
    bibiki_change_go_btn = Button(
        window_main,
        text="Добавить бибику",
        command=open_bibiki_change_window,
        fg="#6E7B8B",
        font=("comic sans", 10),
        relief="flat",
        borderwidth=0,
    )
    canvas.create_window((708, 10), anchor="nw", window=bibiki_change_go_btn, width=115, height=25)


def main_window():
    global manager_go_btn, window_main, canvas, show_delete_btn
    window_main = Tk()
    window_main.title("bibika.ru")
    window_main.geometry('850x600')
    window_main.resizable(False, False)

    window_main.show_delete_btn = False

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
        auto_bibiki.bibiki_contents_window(window_main, main_window)

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
            lambda login, password: add_info_man_button(window_main, canvas, login, password), add_bibiki_change_button,
            window_main, canvas),
        fg="#6E7B8B",
        font=("comic sans", 11),
        relief="flat",
        borderwidth=0,
    )
    canvas.create_window((30, 10), anchor="nw", window=manager_go_btn, width=115, height=25)

    window_main.mainloop()


main_window()

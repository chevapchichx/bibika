import sqlite3
import tkinter as tk
from tkinter import Frame, Button, BOTH
from PIL import Image, ImageTk

import auto_bibiki
import auto_manager

def show_main_frame():
    for widget in frame.winfo_children():
        widget.destroy()
    canvas = tk.Canvas(frame, width=window_width, height=window_height)
    canvas.pack(side="top", fill="both", expand="no")
    canvas.create_image(0, 0, anchor="nw", image=image)

    auto_go_btn = Button(
        frame,
        text="Выбрать бибику",
        command=lambda: auto_bibiki.bibiki_contents_window(frame, show_main_frame),
        bg="#CDAA7D",
        fg="#6E7B8B",
        font=("comic sans", 16),
        relief="flat",
        borderwidth=0,
    )
    canvas.create_window((90, 500), anchor="nw", window=auto_go_btn)

    manager_go_btn = Button(
        frame,
        text="Личный кабинет",
        command=lambda: auto_manager.auth_lk_window(window_main, add_my_bibiki_button),
        bg="#CDAA7D",
        fg="#6E7B8B",
        font=("comic sans", 11),
        relief="flat",
        borderwidth=0,
    )
    canvas.create_window((30, 10), anchor="nw", window=manager_go_btn, width=97, height=25)

con = sqlite3.connect("auto_shop.db")

window_main = tk.Tk()
window_main.title("bibika.ru")

window_width = 850
window_height = 600
window_main.geometry(f'{window_width}x{window_height}')
window_main.resizable(False, False)

frame = Frame(window_main, padx=10, pady=10)
frame.pack(expand=True, fill=BOTH)

path = 'main_photo.jpg'
image = Image.open(path)
image = ImageTk.PhotoImage(image)

show_main_frame()

my_bibiki_btn = None

def add_my_bibiki_button(user):
    global my_bibiki_btn
    if my_bibiki_btn is not None:
        my_bibiki_btn.destroy()
    my_bibiki_btn = Button(
        window_main,
        text="Мои бибики",
        command=lambda: auto_bibiki.manager_bibiki_contents_window(frame, user, show_main_frame),
        bg="#CDAA7D",
        fg="#6E7B8B",
        font=("comic sans", 11),
        relief="flat",
        borderwidth=0,
    )
    my_bibiki_btn.pack(side="top", anchor="ne", pady=10, padx=10)

def bibika_window(bibiki, parent_frame, previous_callback):
    for widget in parent_frame.winfo_children():
        widget.destroy()

    frame = Frame(parent_frame, padx=10, pady=10)
    frame.pack(expand=True, fill=BOTH)

    image = Image.open(bibiki[4])
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(frame, image=photo, width=200, height=200)
    label.image = photo
    label.pack()

    add_my_bibiki_button(None)  # Вызов функции для добавления кнопки "Мои бибики"

    back_btn = Button(
        frame,
        text="Назад",
        command=previous_callback,
        bg="#CDAA7D",
        fg="#6E7B8B",
        font=("comic sans", 14),
        borderwidth=0,
        width=12,
        height=2,
    )
    back_btn.pack(side="top", anchor="nw", pady=20, padx=20)

window_main.mainloop()

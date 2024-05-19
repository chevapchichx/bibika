import sqlite3
import tkinter as tk
from tkinter import Frame, Button, BOTH
from PIL import Image, ImageTk

def bibiki_contents_window(parent_frame, back_callback):
    bibiki = get_bibiki()

    for widget in parent_frame.winfo_children():
        widget.destroy()

    frame = Frame(parent_frame, padx=10, pady=10)
    frame.pack(expand=True, fill=BOTH)

    back_btn = Button(
        parent_frame,
        text="Назад",
        command=back_callback,
        bg="#CDAA7D",
        fg="#6E7B8B",
        font=("comic sans", 14),
        borderwidth=0,
        width=12,
        height=2,
    )
    back_btn.pack(side="top", anchor="ne", pady=10, padx=10)

    buttons_frame = Frame(frame)
    buttons_frame.pack(expand=True)

    for i in range(len(bibiki)):
        bibiki_lb = Button(
            buttons_frame,
            text=f"{bibiki[i][1]} {bibiki[i][2]}",
            font=("comic sans", 14),
            bg="#CDAA7D",
            fg="#6E7B8B",
            borderwidth=0,
            width=20,
            height=2,
            command=lambda i=i: bibika_window(bibiki[i], frame, lambda: bibiki_contents_window(parent_frame, back_callback)),
        )
        bibiki_lb.pack(pady=10)

def manager_bibiki_contents_window(parent_frame, user, back_callback):
    manager_bibiki = get_manager_bibiki(user)

    for widget in parent_frame.winfo_children():
        widget.destroy()

    frame = Frame(parent_frame, padx=10, pady=10)
    frame.pack(expand=True, fill=BOTH)

    back_btn = Button(
        parent_frame,
        text="Назад",
        command=back_callback,
        bg="#CDAA7D",
        fg="#6E7B8B",
        font=("comic sans", 14),
        borderwidth=0,
        width=12,
        height=2,
    )
    back_btn.pack(side="top", anchor="ne", pady=10, padx=10)

    buttons_frame = Frame(frame)
    buttons_frame.pack(expand=True)

    for i in range(len(manager_bibiki)):
        bibiki_lb = Button(
            buttons_frame,
            text=f"{manager_bibiki[i][1]} {manager_bibiki[i][2]}",
            font=("comic sans", 14),
            bg="#CDAA7D",
            fg="#6E7B8B",
            borderwidth=0,
            width=20,
            height=2,
            command=lambda i=i: bibika_window(manager_bibiki[i], frame, lambda: manager_bibiki_contents_window(parent_frame, user, back_callback)),
        )
        bibiki_lb.pack(pady=10)

def get_bibiki():
    with sqlite3.connect("auto_shop.db") as BD:
        cursor = BD.cursor()
        cursor.execute("SELECT ID_A, Brand, Model, Price, Photo, Description FROM auto")
        bibiki = cursor.fetchall()
        return bibiki

def get_manager_bibiki(user):
    with sqlite3.connect("auto_shop.db") as BD:
        cursor = BD.cursor()
        cursor.execute("SELECT ID_A, Brand, Model, Price, Photo, Description FROM auto WHERE Manager=?", (user[2],))
        manager_bibiki = cursor.fetchall()
        return manager_bibiki

def bibika_window(bibiki, parent_frame, back_callback):
    for widget in parent_frame.winfo_children():
        widget.destroy()

    frame = Frame(parent_frame, padx=10, pady=10)
    frame.pack(expand=True, fill=BOTH)

    image = Image.open(bibiki[4])
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(frame, image=photo, width=200, height=200)
    label.image = photo
    label.pack()

    back_btn = Button(
        frame,
        text="Назад",
        command=back_callback,
        bg="#CDAA7D",
        fg="#6E7B8B",
        font=("comic sans", 14),
        borderwidth=0,
        width=12,
        height=2,
    )
    back_btn.pack(side="top", anchor="nw", pady=20, padx=20)

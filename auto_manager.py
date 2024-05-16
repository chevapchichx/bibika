import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox


def toggle_password(password_entry, show_password):
    if show_password.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


def auth_lk():
    window_lk = Tk()
    window_lk.title("lk")
    window_lk.geometry('350x150')

    frame = Frame(
        window_lk,
        padx=10,
        pady=10
    )
    frame.pack(expand=True)

    login_lb = Label(
        frame,
        text="Логин менеджера"
    )
    login_lb.grid(row=3, column=1)

    password_lb = Label(
        frame,
        text="Пароль менеджера"
    )
    password_lb.grid(row=4, column=1)

    login_tf = Entry(
        frame,
    )
    login_tf.grid(row=3, column=2)

    password_entry = Entry(
        frame,
        show="*",
    )
    password_entry.grid(row=4, column=2)

    show_password = tk.BooleanVar()
    show_password.set(False)

    show_password_checkbox = tk.Checkbutton(frame, text="Показать пароль", variable=show_password, command=lambda: toggle_password(password_entry, show_password))
    show_password_checkbox.grid(row=5, column=2)

    ent_btn = Button(
        frame,
        text="Войти",
        command=lambda: get_auth(login_tf.get(), password_entry.get(), window_lk)
    )
    ent_btn.grid(row=6, column=2)

    window_lk.mainloop()


def get_auth(login, password, window_lk):
    with sqlite3.connect("auto_shop.db") as BD:
        cursor = BD.cursor()
        cursor.execute("SELECT Login, Password FROM manager WHERE Login=? AND Password=?", (login, password))
        user = cursor.fetchone()
        if user:
            messagebox.showinfo('Успешно!', 'Авторизация успешно прошла')
            window_lk.destroy()
        else:
            messagebox.showinfo('Ошибка', 'Неверный логин или пароль')
# auth_lk()


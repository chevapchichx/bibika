import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox


def toggle_password(password_entry):
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
    else:
        password_entry.config(show='')


def auth_lk_window():
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

    login_entry = Entry(
        frame,
    )
    login_entry.grid(row=3, column=2)

    password_entry = Entry(
        frame,
        show="*",
    )
    password_entry.grid(row=4, column=2)

    show_pass_checkbox = tk.Checkbutton(frame, text="Показать пароль", command=lambda: toggle_password(password_entry))
    show_pass_checkbox.grid(row=5, column=2)

    ent_btn = Button(
        frame,
        text="Войти",
        command=lambda: get_auth(login_entry, password_entry, window_lk)
    )
    ent_btn.grid(row=6, column=2)

    window_lk.mainloop()


def get_auth(login_entry, password_entry, window_lk):
    login = login_entry.get()
    password = password_entry.get()
    with sqlite3.connect("auto_shop.db") as BD:
        cursor = BD.cursor()
        cursor.execute("SELECT FIO, Phone_num, Login, Password FROM manager WHERE Login=? AND Password=?", (login, password))
        user = cursor.fetchone()
        if user:
            info_man_window(user)
            window_lk.destroy()

        else:
            messagebox.showinfo('Ошибка', 'Неверный логин или пароль')


def info_man_window(user):
    window_info_man = Tk()
    window_info_man.title("info manager")
    window_info_man.geometry('420x400')

    frame = Frame(
        window_info_man,
        padx=10,
        pady=10
    )
    frame.pack(expand=True)

    info_man_lb = Label(
        frame,
        text="Информация о менеджере",
        font=("comic sans", 16),
        anchor="s"
    )
    info_man_lb.grid(row=0, column=1)

    fio_man_lb = Label(
        frame,
        text="ФИО",
        # foreground="CDAA7D",
    )
    fio_man_lb.grid(row=1, column=0)

    fio_man_db = Label(
        frame,
        text=user[0],
        # foreground="CDAA7,
    )
    fio_man_db.grid(row=1, column=1)

    phone_man_lb = Label(
        frame,
        text="Номер телефона",
        # foreground="CDAA7D",
    )
    phone_man_lb.grid(row=2, column=0)

    phone_man_db = Label(
        frame,
        text=user[1],
        # foreground="CDAA7,
    )
    phone_man_db.grid(row=2, column=1)


# auth_lk_window()



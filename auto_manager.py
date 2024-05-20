import sqlite3
from tkinter import Tk, Toplevel, Frame, Label, Entry, Button, messagebox
import tkinter as tk


def toggle_password(password_entry):
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
    else:
        password_entry.config(show='')


def auth_lk_window(my_bibiki_button):
    window_lk = Toplevel()
    window_lk.title("lk")
    window_lk.geometry('360x140')
    window_lk.grab_set()
    window_lk.resizable(False, False)

    frame = Frame(
        window_lk,
        padx=0,
        pady=0
    )
    frame.pack(expand=True)

    login_lb = Label(
        frame,
        text="Логин менеджера",
        fg='#FFF5EE'

    )
    login_lb.grid(row=3, column=1)

    password_lb = Label(
        frame,
        text="Пароль менеджера",
        fg='#FFF5EE',
    )
    password_lb.grid(row=4, column=1)

    login_entry = Entry(
        frame,
    )
    login_entry.grid(row=3, column=2)

    password_entry = Entry(
        frame,
        show="*",
        fg='#FFF5EE'
    )
    password_entry.grid(row=4, column=2)

    show_pass_checkbox = tk.Checkbutton(frame, text="Показать пароль", command=lambda: toggle_password(password_entry))
    show_pass_checkbox.grid(row=5, column=2)

    def open_info_man_window():
        get_auth(login_entry, password_entry, window_lk, my_bibiki_button)

    ent_btn = Button(
        frame,
        text="Войти",
        command=open_info_man_window,
        bg='#FFF5EE',
        fg='#6E7B8B'

    )
    ent_btn.grid(row=6, column=2)

    window_lk.mainloop()


def get_auth(login_entry, password_entry, window_lk, my_bibiki_button):
    login = login_entry.get()
    password = password_entry.get()
    with sqlite3.connect("db/auto_shop.db") as BD:
        cursor = BD.cursor()
        cursor.execute("SELECT FIO, Phone_num, Login, Password FROM manager WHERE Login=? AND Password=?",
                       (login, password))
        user = cursor.fetchone()
        if user:
            for widget in window_lk.winfo_children():
                widget.destroy()
            info_man_window(window_lk, user, my_bibiki_button)
        else:
            messagebox.showinfo('Ошибка', 'Неверный логин или пароль')


def info_man_window(window_lk, user, my_bibiki_button):
    window_lk.title("info manager")
    window_lk.geometry('360x140')
    window_lk.grab_set()
    window_lk.resizable(False, False)

    frame = Frame(
        window_lk,
        padx=0,
        pady=0,
    )
    frame.pack(expand=True)

    info_man_lb = Label(
        frame,
        text="Информация о менеджере",
        font=("comic sans", 16),
        anchor="center",
        fg='#FFF5EE'
    )
    info_man_lb.grid(row=0, column=0, columnspan=3, sticky=tk.W + tk.E + tk.N)

    space_lb = Label(frame, text="", fg='#FFF5EE')
    space_lb.grid(row=1, column=0, columnspan=3)

    fio_man_lb = Label(
        frame,
        text="ФИО",
        fg='#FFF5EE'
    )
    fio_man_lb.grid(row=2, column=0, columnspan=1, sticky=tk.W)

    fio_man_db = Label(
        frame,
        text=user[0],
        fg='#FFF5EE'
    )
    fio_man_db.grid(row=2, column=1, columnspan=1, sticky=tk.E)

    phone_man_lb = Label(
        frame,
        text="Номер телефона",
        fg='#FFF5EE'
    )
    phone_man_lb.grid(row=3, column=0, columnspan=1, sticky=tk.W)

    phone_man_db = Label(
        frame,
        text=user[1],
        fg='#FFF5EE'
    )
    phone_man_db.grid(row=3, column=1, columnspan=1, sticky=tk.E)

    my_bibiki_button()

# auth_lk_window()

import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def toggle_password(password_entry):
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
    else:
        password_entry.config(show='*')

def auth_lk_window(main_window, add_my_bibiki_button):
    window_lk = Toplevel(main_window)
    window_lk.title("lk")
    window_lk.geometry('350x150')
    window_lk.grab_set()
    window_lk.resizable(False, False)

    frame = Frame(window_lk, padx=10, pady=10)
    frame.pack(expand=True)

    login_lb = Label(frame, text="Логин менеджера")
    login_lb.grid(row=3, column=1)

    password_lb = Label(frame, text="Пароль менеджера")
    password_lb.grid(row=4, column=1)

    login_entry = Entry(frame)
    login_entry.grid(row=3, column=2)

    password_entry = Entry(frame, show="*")
    password_entry.grid(row=4, column=2)

    show_pass_checkbox = tk.Checkbutton(frame, text="Показать пароль", command=lambda: toggle_password(password_entry))
    show_pass_checkbox.grid(row=5, column=2)

    ent_btn = Button(frame, text="Войти", command=lambda: get_auth(login_entry, password_entry, window_lk, add_my_bibiki_button))
    ent_btn.grid(row=6, column=2)

    window_lk.mainloop()

def get_auth(login_entry, password_entry, window_lk, add_my_bibiki_button):
    login = login_entry.get()
    password = password_entry.get()
    with sqlite3.connect("auto_shop.db") as BD:
        cursor = BD.cursor()
        cursor.execute("SELECT FIO, Phone_num, Login, Password FROM manager WHERE Login=? AND Password=?", (login, password))
        user = cursor.fetchone()
        if user:
            add_my_bibiki_button(user)
            info_man_window(user)
            window_lk.destroy()
        else:
            messagebox.showinfo('Ошибка', 'Неверный логин или пароль')

def info_man_window(user):
    window_info_man = Toplevel()
    window_info_man.title("info manager")
    window_info_man.geometry('450x125')
    window_info_man.configure(bg='#6E7B8B')
    window_info_man.grab_set()
    window_info_man.resizable(False, False)

    frame = Frame(window_info_man, padx=10, pady=10, bg='#6E7B8B')
    frame.pack(expand=True)

    info_man_lb = Label(frame, text="Информация о менеджере", font=("comic sans", 16), anchor="center", bg='#6E7B8B')
    info_man_lb.grid(row=0, column=2, columnspan=3)

    space_lb = Label(frame, text="", bg='#6E7B8B')
    space_lb.grid(row=1, column=0, columnspan=3)

    fio_man_lb = Label(frame, text="ФИО", bg='#6E7B8B')
    fio_man_lb.grid(row=2, column=1)

    fio_man_db = Label(frame, text=user[0], bg='#6E7B8B')
    fio_man_db.grid(row=2, column=3)

    phone_man_lb = Label(frame, text="Номер телефона", bg='#6E7B8B')
    phone_man_lb.grid(row=3, column=1)

    phone_man_db = Label(frame, text=user[1], bg='#6E7B8B')
    phone_man_db.grid(row=3, column=3)

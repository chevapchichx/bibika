import sqlite3
from tkinter import Toplevel, Frame, Label, Entry, Button, messagebox
import tkinter as tk


def toggle_password(password_entry):
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
    else:
        password_entry.config(show='')


def auth_lk_window(add_info_man_go_button, add_bibiki_change_button, window_main, canvas):
    window_lk = Toplevel()
    window_lk.title("lk")
    window_lk.geometry('360x140+100+125')
    window_lk.grab_set()
    window_lk.resizable(False, False)

    frame = Frame(window_lk, padx=0, pady=0)
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

    ent_btn = Button(frame, text="Войти", fg="#6E7B8B",
                     command=lambda: [add_info_man_go_button(login_entry.get(), password_entry.get()),
                                      window_lk.destroy()] and add_bibiki_change_button(window_main, canvas))
    ent_btn.grid(row=6, column=2)


def get_auth(login, password):
    with sqlite3.connect("db/auto_shop.db") as BD:
        cursor = BD.cursor()
        cursor.execute("SELECT FIO, Phone_num, Login, Password FROM manager WHERE Login=? AND Password=?",
                       (login, password))
        user = cursor.fetchone()
        if user:
            return user
        else:
            messagebox.showinfo('Ошибка', 'Неверный логин или пароль')
            return None


def info_man_window(user, main_window, window_main):
    window_info_man = Toplevel()
    window_info_man.title("info manager")
    window_info_man.geometry('380x140+100+125')
    window_info_man.resizable(False, False)

    frame = Frame(window_info_man, padx=5, pady=5)
    frame.pack(expand=True, fill="both")

    info_man_lb = Label(frame, text="Информация о менеджере", font=("comic sans", 16), anchor="center")
    info_man_lb.grid(row=0, column=0, columnspan=4, sticky=tk.W + tk.E + tk.N)

    space_lb = Label(frame, text="")
    space_lb.grid(row=1, column=0, columnspan=4)

    fio_man_lb = Label(frame, text="ФИО")
    fio_man_lb.grid(row=2, column=1)

    fio_man_db = Label(frame, text=user[0])
    fio_man_db.grid(row=2, column=3, )

    phone_man_lb = Label(frame, text="Номер телефона")
    phone_man_lb.grid(row=3, column=1)

    phone_man_db = Label(frame, text=user[1])
    phone_man_db.grid(row=3, column=3, )

    def exit_btn():
        window_info_man.destroy()
        window_main.destroy()
        main_window()

    exit_btn = Button(frame, text="Выход", command=exit_btn, fg="#6E7B8B", font=("comic sans", 11), relief="flat")
    exit_btn.grid(row=4, column=3, sticky=tk.SE, padx=5, pady=5)

    frame.grid_rowconfigure(4, weight=1)
    frame.grid_columnconfigure(3, weight=1)




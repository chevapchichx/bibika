import sqlite3

import tkinter as tk
from tkinter import *
from tkinter import messagebbbb

from PIL import Image, ImageTk


def clck_lk():
   auth_lk()


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

    login_tf = Entry(
       frame,
    )
    login_tf.grid(row=3, column=2)

    password_lb = Label(
       frame,
       text="Пароль менеджера"
    )
    password_lb.grid(row=4, column=1)

    password_tf = Entry(
       frame,
    )
    password_tf.grid(row=4, column=2)

    ent_btn = Button(
       frame,
       text="Войти",
    )
    ent_btn.grid(row=5, column=2)

    window_lk.mainloop()


with sqlite3.connect("auto_shop.db") as BD:
    cursor = BD.cursor()
    cursor.execute("SELECT ID_M, FIO, Phone_num, Login FROM manager WHERE Login =  ")
    users = cursor.fetchall()
    for user in users:
        if Login == str(users[0]):
            if Password == str(users[1]):
                messagebox.showinfo('Успешно!', 'Авторизация успешно прошла')


        messagebox.showinfo('Ошибка', 'Неверный логин или пароль')





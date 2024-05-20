import sqlite3
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Tk, Toplevel, Frame, Button, Label

# import auto_bibiki
import auto_bibiki
import auto_manager


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
      bg="#CDAA7D",
      fg="#6E7B8B",
      font=("comic sans", 16),
      relief="flat",
      borderwidth=0,
      )
   canvas.create_window((90, 500), anchor="nw", window=auto_go_btn)

   manager_go_btn = Button(
      window_main,
      text="Личный кабинет",
      command=auto_manager.auth_lk_window,
      bg="#CDAA7D",
      fg="#6E7B8B",
      font=("comic sans", 11),
      relief="flat",
      borderwidth=0,
      )
   canvas.create_window((30, 10),anchor="nw", window=manager_go_btn, width=97, height=25)


   window_main.mainloop()


main_window()

# my_bibiki_btn = None

# def add_my_bibiki_button(user):
#    global my_bibiki_btn
#    if my_bibiki_btn is not None:
#       my_bibiki_btn.destroy()
#    my_bibiki_btn = Button(
#       frame,
#       text="Мои бибики",
#       command=open_bibiki_contents_window,
#       bg="#CDAA7D",
#       fg="#6E7B8B",
#       font=("comic sans", 11),
#       relief="flat",
#       borderwidth=0,
#    )
#    canvas.create_window((750, 10), anchor="ne", window=my_bibiki_btn, width=97, height=25)
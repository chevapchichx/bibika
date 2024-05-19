import sqlite3
import tkinter as tk
from PIL import Image, ImageTk
import auto_manager
import auto_bibiki

con = sqlite3.connect("auto_shop.db")

window_main = tk.Tk()
window_main.title("bibika.ru")

window_main.geometry('850x600')
window_main.resizable(False, False)

frame = tk.Frame(
   window_main,
   padx=0,
   pady=0
)
frame.pack(expand=True)

path = 'main_photo.jpg'

image = Image.open(path)
image = ImageTk.PhotoImage(image)

canvas = tk.Canvas(window_main, width=850, height=600)
canvas.pack(side="top", fill="both", expand="no")
canvas.create_image(0, 0, anchor="nw", image=image)

auto_go_btn = tk.Button(
   window_main,
   text="Выбрать бибику",
   command=auto_bibiki.bibiki_contents_window,
   bg="#CDAA7D",
   fg="#6E7B8B",
   font=("comic sans", 16),
   relief="flat",
   borderwidth=0,
)
canvas.create_window((90, 500), anchor="nw", window=auto_go_btn)

manager_go_btn = tk.Button(
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
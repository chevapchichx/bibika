import sqlite3
from tkinter import Frame, Button, Label, Entry, Text, filedialog, messagebox
from io import BytesIO
from PIL import Image, ImageTk


def get_bibiki():
    with sqlite3.connect("db/auto_shop.db") as BD:
        cursor = BD.cursor()
        cursor.execute("SELECT ID_A, Brand, Model, Price, Description FROM auto")
        bibiki = cursor.fetchall()
        return bibiki


def get_image_from_db(bibiki):
    conn = sqlite3.connect('db/auto_shop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Photo FROM auto WHERE ID_A = ?", (bibiki[0],))
    image_data = cursor.fetchone()[0]
    conn.close()
    return image_data


def bibiki_contents_window(parent_frame, main_window_func):
    parent_frame.title("bibiki")
    parent_frame.grab_set()

    bibiki = get_bibiki()

    frame = Frame(parent_frame, padx=0, pady=0)
    frame.pack(expand=True)

    def open_bibika_window(i):
        for widget in parent_frame.winfo_children():
            widget.destroy()
        bibika_window(parent_frame, bibiki[i], bibiki_contents_window, main_window_func)

    for i in range(0, len(bibiki)):
        bibiki_btn = Button(frame, text=f"{bibiki[i][1]} {bibiki[i][2]}", font=("comic sans", 14), fg="#6E7B8B",
                            borderwidth=0, width=20, height=2, command=lambda i=i: open_bibika_window(i))
        bibiki_btn.pack(pady=10)

    def go_back_1():
        parent_frame.destroy()
        main_window_func()

    back_btn = Button(parent_frame, text="Назад", command=go_back_1, fg="#6E7B8B", font=("comic sans", 12),
                      relief="flat", borderwidth=0, width=6, height=1)
    back_btn.place(x=750, y=555)


def bibika_window(parent_frame, bibiki, bibiki_c_window_open, main_window_func):
    parent_frame.title(f"{bibiki[1]} {bibiki[2]}")
    parent_frame.geometry('850x600')
    parent_frame.grab_set()
    parent_frame.resizable(False, False)

    frame = Frame(parent_frame, padx=0, pady=0)
    frame.pack()

    image_data = get_image_from_db(bibiki)
    image_data_io = BytesIO(image_data)
    image = Image.open(image_data_io)
    photo = ImageTk.PhotoImage(image)

    bibika_photo = Label(frame, image=photo, width=850, height=500, borderwidth=0)
    bibika_photo.image = photo
    bibika_photo.pack()

    bibika_price_lb = Label(frame, text=f"Цена: {str(bibiki[3])} руб.", font=("comic sans", 15), wraplength=800,
                            justify="left")
    bibika_price_lb.pack(pady=10)

    bibika_desc_lb = Label(frame, text=f"{str(bibiki[4])}", font=("comic sans", 15), wraplength=800,
                           justify="left")
    bibika_desc_lb.pack(pady=10)

    def delete_bibika():
        if messagebox.askyesno("Подтверждение", "Вы уверены, что хотите удалить бибику?", icon="warning"):
            with sqlite3.connect("db/auto_shop.db") as BD:
                cursor = BD.cursor()
                cursor.execute("DELETE FROM auto WHERE ID_A = ?", (bibiki[0],))
                BD.commit()
            messagebox.showinfo("Удалено", "Бибика успешно удалена!")
            for widget in parent_frame.winfo_children():
                widget.destroy()
            bibiki_c_window_open(parent_frame, main_window_func)

    delete_btn = Button(parent_frame, text="Удалить", command=delete_bibika, fg="#6E7B8B", font=("comic sans", 12),
                        relief="flat", borderwidth=0, width=10, height=1)
    if parent_frame.show_delete_btn:
        delete_btn.place(x=20, y=555)
    else:
        delete_btn.place_forget()

    def go_back_2():
        for widget in parent_frame.winfo_children():
            widget.destroy()
        bibiki_c_window_open(parent_frame, main_window_func)

    back_btn = Button(parent_frame, text="Назад", command=go_back_2, fg="#6E7B8B", font=("comic sans", 12),
                      relief="flat", borderwidth=0, width=6, height=1)
    back_btn.place(x=750, y=555)

    parent_frame.delete_btn = delete_btn


def bibiki_change_window(window_bibiki_change, main_window_func):
    window_bibiki_change.title('create bibika')
    window_bibiki_change.geometry('850x600')
    window_bibiki_change.grab_set()
    window_bibiki_change.resizable(False, False)

    frame = Frame(window_bibiki_change, padx=10, pady=10)
    frame.pack(expand=True, fill="both")

    center_frame = Frame(frame)
    center_frame.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    Label(center_frame, text="Марка", font=("comic sans", 11)).grid(row=0, column=0, padx=5, pady=5, sticky='w')
    brand_entry = Entry(center_frame, width=30)
    brand_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

    Label(center_frame, text="Модель", font=("comic sans", 11)).grid(row=1, column=0, padx=5, pady=5, sticky='w')
    model_entry = Entry(center_frame, width=30)
    model_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

    Label(center_frame, text="Цена", font=("comic sans", 11)).grid(row=2, column=0, padx=5, pady=5, sticky='w')
    price_entry = Entry(center_frame, width=30)
    price_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')

    Label(center_frame, text="Описание", font=("comic sans", 11)).grid(row=3, column=0, padx=5, pady=5, sticky='nw')
    description_entry = Text(center_frame, width=39, height=5, font=("comic sans", 11))
    description_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

    photo_label = Label(center_frame, text="Фото", relief="solid", width=35, height=8, borderwidth=1)
    photo_label.place(x=500, y=50)
    photo_label.grid(row=0, column=2, rowspan=4, padx=10, pady=5, sticky='nsew')
    photo_label.grid_propagate(False)

    photo_path = ""

    def upload_photo():
        nonlocal photo_path
        file_path = filedialog.askopenfilename()
        if file_path:
            photo_path = file_path
            image = Image.open(file_path)
            image.thumbnail(size=(300, 300))
            photo = ImageTk.PhotoImage(image)
            photo_label.config(image=photo, width=319, height=8, borderwidth=0)
            photo_label.image = photo

    upload_btn = Button(center_frame, text="Загрузить фото", command=upload_photo, fg="#6E7B8B",
                        font=("comic sans", 12))
    upload_btn.grid(row=4, column=2, padx=10, pady=5, sticky='e')

    def save_bibika():
        brand = brand_entry.get()
        model = model_entry.get()
        price = price_entry.get()
        description = description_entry.get("1.0", "end-1c")
        if not (brand and model and price and photo_path and description):
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены!", icon='warning')
            return
        try:
            price = float(price)
        except ValueError:
            messagebox.showerror("Ошибка", "Цена должна состоять из цифр!", icon='warning')
            return

        photo_data = open(photo_path, 'rb').read()

        with sqlite3.connect("db/auto_shop.db") as BD:
            cursor = BD.cursor()
            cursor.execute("INSERT INTO auto (Brand, Model, Price, Photo, Description) VALUES (?, ?, ?, ?, ?)",
                           (brand, model, price, photo_data, description))
            BD.commit()

        messagebox.showinfo("Успешно", "Бибика успешно сохранена!")
        if messagebox.askyesno("Продолжить", "Хотите добавить еще одну бибику?", icon="question"):
            brand_entry.delete(0, 'end')
            model_entry.delete(0, 'end')
            price_entry.delete(0, 'end')
            description_entry.delete("1.0", "end")
            photo_label.config(image="", relief="solid", width=35, height=8, borderwidth=1)
        else:
            window_bibiki_change.destroy()
            main_window_func()

    ok_btn = Button(window_bibiki_change, text="ОК", command=save_bibika, fg="#6E7B8B", font=("comic sans", 12),
                    relief="flat", borderwidth=0, width=2, height=1)
    ok_btn.place(x=690, y=555)

    def go_back_3():
        window_bibiki_change.destroy()
        main_window_func()

    back_btn = Button(window_bibiki_change, text="Отмена", command=go_back_3, fg="#6E7B8B", font=("comic sans", 12),
                      relief="flat", borderwidth=0, width=5, height=1)
    back_btn.place(x=750, y=555)

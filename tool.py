#-*- coding: utf-8 -*-
import psycopg2 as psy
try:    import tkinter as tk
except: import Tkinter as tk

# --- Заглавное окно ---
master = tk.Tk()
master.title('База импортного инструмента')

okno1 = tk.LabelFrame(master)
okno1.grid()

# --- Кнопка ввода нового инструмента ---
knopka_vvod = tk.Button(okno1,
                        text = 'Ввести новый инструмент')
knopka_vvod.grid(row  = 1,
                 padx = 50,
                 pady = 50)

okno1.mainloop()


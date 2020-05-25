#-*- coding: utf-8 -*-
import psycopg2 as psy
try:    import tkinter as tk
except: import Tkinter as tk

# --- Заглавное окно ---
master = tk.Tk()
master.title('База импортного инструмента')
master.minsize(390,250)
master.maxsize(390,250)

okno1 = tk.LabelFrame(master)
okno1.pack(padx = 10,
           pady = 10,
           ipadx = 50)

# --- Кнопка перехода в окно учёта поступления инструмента ---
knopka_vvod = tk.Button(okno1,
                        width = 20,
                        height = 2,
                        text = 'Ввести инструмент')
knopka_vvod.pack(padx = 30,
                 pady = 20)

# --- Кнопка перехода в окно учёта выдачи инструмента ---
knopka_vydacha = tk.Button(okno1,
                           width = 20,
                           height = 2,
                           text = 'Выдать инструмент')
knopka_vydacha.pack(padx = 30,
                    pady = 0)

# --- Кнопка перехода к информации о программе ---
knopka_info = tk.Button(okno1,
                        width = 20,
                        height = 2,
                        text = 'О программе...')
knopka_info.pack(padx = 30,
                 pady = 20)

okno1.mainloop()


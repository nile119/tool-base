#-*- coding: utf-8 -*-
import psycopg2 as psy
try:    import tkinter as tk
except: import Tkinter as tk


master = tk.Tk()
master.title('База импортного инструмента')
master.minsize(390,340)
master.maxsize(390,340)

# --- Заглавное окно ---
okno0 = tk.LabelFrame(master)
okno0.pack(padx = 10,
           pady = 10,
           ipadx = 50)

# --- Окно справки --- 
okno3 = tk.LabelFrame(master)

###               Заглавное окно               ###

# --- Кнопка перехода в окно учёта поступления инструмента ---
knopka_vvod = tk.Button(okno0,
                        width = 20,
                        height = 2,
                        text = 'Ввести инструмент')
knopka_vvod.pack(padx = 30,
                 pady = 20)

# --- Кнопка перехода в окно учёта выдачи инструмента ---
knopka_vydacha = tk.Button(okno0,
                           width = 20,
                           height = 2,
                           text = 'Выдать инструмент')
knopka_vydacha.pack(padx = 30,
                    pady = 0)

# --- Кнопка перехода к информации о программе ---
def infoo():
    okno0.pack_forget()
   
    okno3.pack(padx = 10,
               pady = 10,
               ipadx = 50)

knopka_info = tk.Button(okno0,
                        width = 20,
                        height = 2,
                        text = 'О программе...',
                        command=infoo)
knopka_info.pack(padx = 30,
                 pady = 20)

# --- Кнопка выхода ---
def vyhod():
    okno0.quit()

knopka_vihod = tk.Button(okno0,
                         width = 20,
                         height = 2,
                         text = 'Выход',
                         command=vyhod)
knopka_vihod.pack(padx = 30,
                  pady = 20)

###                  Окно справки                  ###    
tk.Label(okno3,text='- - -').pack(pady=15,anchor='center')
for i in open('info.txt'):
    tk.Label(okno3,
             text=i.rstrip()).pack(anchor='sw',
                                   padx=15)
tk.Label(okno3,text='- - -').pack(pady=15,anchor='center')

# --- Кнопка выхода ---
def nazad():
    okno3.pack_forget()
    okno0.pack(padx = 10,
               pady = 10,
               ipadx = 30)

knopka_nazad = tk.Button(okno3,
                         width = 20,
                         height = 2,
                         text = 'Назад',
                         command=nazad)
knopka_nazad.pack(padx = 30,
                  pady = 20)

tk.mainloop()

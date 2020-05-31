#-*- coding: utf-8 -*-
import psycopg2 as psy
try:    import tkinter as tk
except: import Tkinter as tk


master = tk.Tk()
master.title('База импортного инструмента')
#master.minsize(640,420)
#master.maxsize(640,420)

def okno(a):
    a.pack(fill='both',
           padx = 20,
           pady = 20,
           ipadx = 50,
           expand=1)
           
####################################
###   Заглавное окно ("Окно 0")  ###
####################################

okno0 = tk.LabelFrame(master)
okno(okno0)

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
    okno(okno3)

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
knopka_vihod.pack(side='bottom',
                  padx = 30,
                  pady = 20)

###################################
###   Окно справки ("Окно 3")   ###
###################################

okno3 = tk.LabelFrame(master)

# --- Справочный текст ---

tekst3=tk.Frame(okno3)
tekst3.pack(pady=25)

for i in open('info.txt'):
    tk.Label(tekst3,
             text=i.rstrip()).pack(anchor='w',
                                   padx=5)

# --- Кнопка выхода ---

def nazad():
    okno3.pack_forget()
    okno(okno0)

knopka_nazad = tk.Button(okno3,
                         width = 10,
                         height = 2,
                         text = 'Назад',
                         command=nazad)
knopka_nazad.pack(side='bottom',
                  anchor='w',
                  padx=30,
                  pady=20)

tk.mainloop()

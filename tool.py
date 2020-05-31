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
           ipadx = 40,
           expand=1)
           
####################################
###   Заглавное окно ("Окно 0")  ###
####################################

okno0 = tk.LabelFrame(master)
okno(okno0)

# --- Кнопка перехода в окно учёта поступления инструмента ---
def vvod_tool():
    okno0.pack_forget()
    okno(okno1)

knopka_vvod = tk.Button(okno0,
                        width = 20,
                        height = 2,
                        text = 'Ввести инструмент',
                        command=vvod_tool)
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

############################################
###   Окно ввода инструмента ("Окно 1")  ###
############################################

'''
|   Фреза   |   Резец   |   Пластина   |   Другое  |
|                  Характеристика                  |
|                   Наименование                   |
|   Радиус  | 


'''

okno1 = tk.LabelFrame(master)

# --- Ввод типа инструмента ---
forma1=tk.Frame(okno1)
forma1.pack(pady=25)

tip_text = tk.Label(forma1,
                    width = 25,
                    text = 'Тип:',
                    anchor = 'w')
tip_text.grid(row = 1,
              column = 1,
              pady = 2)

tip_vvod = tk.Entry(forma1,
                    width = 20)
tip_vvod.grid(row = 1,
              column = 2)

# --- Наименование инструмента ---
name_text = tk.Label(forma1,
                     width = 25,
                     text = 'Наименование:',
                     anchor = 'w').grid(row = 2,
                                        column = 1,
                                        pady = 2)
name_vvod = tk.Entry(forma1,
                     width = 20).grid(row = 2,
                                      column = 2)

# --- Производитель/Стандарт ---
brand_text = tk.Label(forma1,
                     width = 25,
                     text = 'Производитель (или ГОСТ):',
                     anchor = 'w').grid(row = 3,
                                        column = 1,
                                        pady = 2)
brand_vvod = tk.Entry(forma1,
                     width = 20).grid(row = 3,
                                      column = 2)

# --- Кнопка выхода ---
def back_b(a):
    def nazad():
        a.pack_forget()
        okno(okno0)

    knopka_nazad = tk.Button(a,
                             width = 10,
                             height = 2,
                             text = 'Назад',
                             command=nazad)
    knopka_nazad.pack(side='bottom',
                      anchor='w',
                      padx=30,
                      pady=20)
back_b(okno1)

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
def back_b(a):
    def nazad():
        a.pack_forget()
        okno(okno0)

    knopka_nazad = tk.Button(a,
                             width = 10,
                             height = 2,
                             text = 'Назад',
                             command=nazad)
    knopka_nazad.pack(side='bottom',
                      anchor='w',
                      padx=30,
                      pady=20)
back_b(okno3)

tk.mainloop()

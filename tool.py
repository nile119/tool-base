#-*- coding: utf-8 -*-

#---------------------

import datetime as dt
try:   
    import tkinter as tk
    from tkinter import messagebox
except: 
    import Tkinter as tk
    import tkMessageBox as messagebox
try:       
    import psycopg2 as psy
except:   
    messagebox.showerror("Ошибка", 'Для открытия файла необходимо установить модуль psycopg2')

#--------------------

def okno(a):             # Функция "Отобразить окно"
    a.pack(fill='both', padx = 20, pady = 20, ipadx = 40, expand=1)

def back_b(a,b):         # Кнопка "Назад"
    def nazad():
        a.pack_forget()
        okno(b)
    knopka_nazad = tk.Button(a, width = 10, height = 2, text = 'Назад', command=nazad)
    knopka_nazad.pack(side='left', anchor='w', padx=30, pady=20, expand=1)

def forw_b(a,b):         # Кнопка "Далее"
    def nazad():
        a.pack_forget()
        okno(b)
    knopka_nazad = tk.Button(a, width = 10, height = 2, text = 'Далее', command=nazad)
    knopka_nazad.pack(side='right', anchor='e', padx=30, pady=20, expand=1)
           
####################################
###   Заглавное окно ("Окно 0")  ###
####################################

master = tk.Tk()
master.title('База импортного инструмента')
master.minsize(640,20)
#master.maxsize(640,420)

okno0 = tk.LabelFrame(master)
okno(okno0)

# --- Кнопка перехода в окно учёта поступления инструмента ---

def vvod_tool():
    okno0.pack_forget()
    okno(okno1_1)

knopka_vvod = tk.Button(okno0, width = 20, height = 2, text = 'Ввести инструмент', command=vvod_tool)
knopka_vvod.pack(padx = 30, pady = 20)

# --- Кнопка перехода в окно учёта выдачи инструмента ---

knopka_vydacha = tk.Button(okno0, width = 20, height = 2, text = 'Выдать инструмент')
knopka_vydacha.pack(padx = 30, pady = 0)

# --- Кнопка перехода к информации о программе ---

def infoo():
    okno0.pack_forget()
    okno(okno3)

knopka_info = tk.Button(okno0, width = 20, height = 2, text = 'О программе...', command=infoo)
knopka_info.pack(padx = 30, pady = 20)

# --- Кнопка выхода ---

def vyhod():
    okno0.quit()

knopka_vihod = tk.Button(okno0, width = 20, height = 2, text = 'Выход', command=vyhod)
knopka_vihod.pack(side='bottom', padx = 30, pady = 20)

############################################
###   Окно ввода инструмента ("Окно 1")  ###
############################################

### Окно 1_1 Шаг 1: Выберите тип инструмента ###

okno1_1 = tk.LabelFrame(master)

forma1_1=tk.Frame(okno1_1)
forma1_1.pack(pady=15)

shag_1 = tk.Label(forma1_1, text = 'Шаг 1: Выберите тип инструмента', anchor = 'w')
shag_1.pack(pady = 20)

# --- Ввод типа инструмента ---

tip_text = tk.Label(forma1_1, width = 25, text = 'Тип:')
tip_text.pack(pady = 2)

var1=tk.StringVar(master)
var1.set('')

tip_vvod = tk.OptionMenu(forma1_1,
                         var1,
                         'Вращающийся инструмент',
                         'Токарный инструмент',
                         'Пластины',
                         'Вспомогательный инструмент',
                         'Другое')
tip_vvod.pack(pady=2)

# --- Кнопка выхода ---

back_b(okno1_1,okno0)

### Окно 1_2 Шаг 2: Введите данные инструмента ###

okno1_2 = tk.LabelFrame(master)

# --- Кнопка далее ---

def forw():         # Кнопка "Далее"
    if var1.get() == u'Вращающийся инструмент':
        diam_text.grid(row=6,column=1,pady=2)
        diam_vvod.grid(row=6,column=2,pady=2)
    elif var1.get() == u'Пластины':
        material_text.grid(row=4,column=1,pady=2)
        material_vvod.grid(row=4,column=2,pady=2)
  #  posle_shag_2['text']=str(var1.get())
    okno1_1.pack_forget()
    okno(okno1_2)

def switchButtonState(*args):
    if (var1.get()==''):
        knopka_vpered['state'] = tk.DISABLED
    else:
        knopka_vpered['state'] = tk.NORMAL
knopka_vpered = tk.Button(okno1_1, state=tk.DISABLED, width = 10, height = 2, text = 'Далее', command=forw)
knopka_vpered.pack(side='right', anchor='e', padx=30, pady=20, expand=1)

var1.trace("w",switchButtonState)

# ---

forma1_2=tk.Frame(okno1_2)
forma1_2.pack(pady=15)


shag_2 = tk.Label(forma1_2, text = 'Шаг 2: Введите данные инструмента', anchor = 'w')
shag_2.grid(row = 0, column = 1, columnspan=2, pady = 5)

posle_shag_2 = tk.Label(forma1_2, textvariable = var1, anchor = 'w')
posle_shag_2.grid(row = 1, column = 1, columnspan=2, pady = 10)

# --- Наименование инструмента ---
name_text = tk.Label(forma1_2, width = 35, text = 'Наименование:',anchor = 'w')
name_vvod = tk.Entry(forma1_2, width = 35)

# --- Номер инструмента ---
nomer_text = tk.Label(forma1_2, width = 35, text = 'Номер по каталогу / ГОСТу / заводской:',anchor = 'w')
nomer_vvod = tk.Entry(forma1_2, width = 35)

# --- Материал ---
material_text = tk.Label(forma1_2, width = 35, text = 'Материал:',anchor = 'w')
material_vvod = tk.Entry(forma1_2, width = 35)

# --- Производитель/Стандарт ---
brand_text = tk.Label(forma1_2, width = 35, text = 'Производитель (или ГОСТ):', anchor = 'w')
brand_vvod = tk.Entry(forma1_2, width = 35)

# --- Диаметр ---
diam_text = tk.Label(forma1_2, width = 35, text = 'Диаметр, мм:', anchor = 'w')
diam_vvod = tk.Entry(forma1_2, width = 35)

# --- Количество ---
kolichestvo_text = tk.Label(forma1_2, width = 35, text = 'Количество, шт:', anchor = 'w')
kolichestvo_vvod = tk.Entry(forma1_2, width = 35)

# --- Комментарий ---
comment_text = tk.Label(forma1_2, width = 35, text = 'Комментарий:', anchor = 'w')
comment_vvod = tk.Entry(forma1_2, width = 35)

# --- Дата ---
date_text = tk.Label(forma1_2, width = 35, text = 'Дата:', anchor = 'w')
date_vvod = tk.Frame(forma1_2)
date_sep_0 = tk.Label(date_vvod, text = 'День: ')
date_vvod_d = tk.Entry(date_vvod, width = 2)
date_sep_1 = tk.Label(date_vvod, text = ',   Месяц: ')
date_vvod_m = tk.Entry(date_vvod, width = 2)
date_sep_2 = tk.Label(date_vvod, text = ',   Год: ')
date_vvod_y = tk.Entry(date_vvod, width = 4)

date_vvod_d.insert(0,str(dt.date.today().day))
date_vvod_m.insert(0,str(dt.date.today().month))
date_vvod_y.insert(0,str(dt.date.today().year))

# --- Вывод на экран ---

name_text.grid(row=2,column=1,pady=2)
name_vvod.grid(row=2,column=2,pady=2)
nomer_text.grid(row=3,column=1,pady=2)
nomer_vvod.grid(row=3,column=2,pady=2)
brand_text.grid(row=5,column=1,pady=2)
brand_vvod.grid(row=5,column=2,pady=2)
kolichestvo_text.grid(row=7,column=1,pady=2)
kolichestvo_vvod.grid(row=7,column=2,pady=2)
comment_text.grid(row=8,column=1,pady=2)
comment_vvod.grid(row=8,column=2,pady=2)
date_text.grid(row=9,column=1,pady=2)
date_vvod.grid(row=9,column=2,pady=2,sticky='w')

date_sep_0.grid(row=1,column=0,pady=2)
date_vvod_d.grid(row=1,column=1,pady=2)
date_sep_1.grid(row=1,column=2,pady=2)
date_vvod_m.grid(row=1,column=3,pady=2)
date_sep_2.grid(row=1,column=4,pady=2)
date_vvod_y.grid(row=1,column=5,pady=2)

# --- Кнопка ввода значений в базу ---

def v_bazu():

    '''
    Собираем информацию из полей ввода и заносим их в таблицу инструмента
    '''

    try:       
        conn = psy.connect("dbname='test' user=Alex")
    except:   
        messagebox.showerror("Ошибка", 'Не удаётся открыть базу данных')

    cur = conn.cursor()

    table1 = ['tip',
              'name',
              'nomer',
              'brand',
              'kolichestvo',
              'comment',
              'date']

    data1 = [var1.get(),
             name_vvod.get(),
             nomer_vvod.get(),
             brand_vvod.get(),
             kolichestvo_vvod.get(),
             comment_vvod.get(),
             dt.date(int(date_vvod_y.get()),
                     int(date_vvod_m.get()),
                     int(date_vvod_d.get()))]

    polya = [name_vvod,
             nomer_vvod,
             brand_vvod,
             kolichestvo_vvod,
             comment_vvod,
             material_vvod,
             diam_vvod]

    if var1.get()=='Вращающийся инструмент':
        try:
            float(diam_vvod.get())
        except:
            messagebox.showerror("Ошибка",
                                 'Введите число в поле "Диаметр инструмента"')
            return 1
        data1.append(diam_vvod.get())
        table1.append('diam')

    try:
       int(kolichestvo_vvod.get())
    except:
        messagebox.showerror("Ошибка", 'Введите целое число в поле "Количество"')
        return 1

    if var1.get()=='Пластины':
        data1.append(material_vvod.get())
        table1.append('material')
    if comment_vvod.get() == '':
        comment_vvod.insert(0,' ')
    if brand_vvod.get() == '':
        brand_vvod.insert(0,' ')

    kol=[]
    for i in range(len(data1)):
        kol.append('%s')
    
    stroka = "INSERT INTO instrument (%s) VALUES (%s)" % (','.join(table1), 
                                                          ','.join(kol)) 
    try:
        cur.execute(stroka, data1) 
        conn.commit()
        cur.close()
        conn.close()
        var1.set('')
        for i in polya:
            i.delete(0,"end")
        messagebox.showinfo('Готово!','Инструмент внесён в базу!')
        okno1_2.pack_forget()
        okno(okno0)
    except:
        messagebox.showerror("Ошибка", 'Заполните все поля')
   
knopka_v_bazu = tk.Button(okno1_2, width = 10, height = 2, text = 'В базу', command=v_bazu)
knopka_v_bazu.pack(side='right', anchor='e', padx=30, pady=20, expand=1)


# --- Кнопка выхода ---

def nazad_1_2():

    diam_text.grid_remove()
    diam_vvod.grid_remove()
    material_text.grid_remove()
    material_vvod.grid_remove()
    okno1_2.pack_forget()
    okno(okno1_1)

knopka_nazad_1_2 = tk.Button(okno1_2, width = 10, height = 2, text = 'Назад', command=nazad_1_2)
knopka_nazad_1_2.pack(side='left', anchor='w', padx=30, pady=20, expand=1)

###################################
###   Окно справки ("Окно 3")   ###
###################################

okno3 = tk.LabelFrame(master)

# --- Справочный текст ---

tekst3=tk.Frame(okno3)
tekst3.pack(pady=25)

try:
    for i in open('info.txt',encoding='utf-8'):
        tk.Label(tekst3, text=i.rstrip()).pack(anchor='w', padx=5)
except:
    for i in open('info.txt'):
        tk.Label(tekst3, text=i.rstrip()).pack(anchor='w', padx=5)

# --- Кнопка выхода ---

back_b(okno3,okno0)

tk.mainloop()


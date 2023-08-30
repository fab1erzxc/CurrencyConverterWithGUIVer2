from kzt_exchangerates import Rates
from datetime import date
from tkinter import *
from tkinter import ttk


def exchange():
    e_usd.delete(0, END)
    e_eur.delete(0, END)
    e_try.delete(0, END)
    e_rub.delete(0, END)
    e_cny.delete(0, END)
    e_usd.insert(0, round(float(e_kzt.get()) * float(rates.get_exchange_rate('USD', from_kzt=False)), 2))
    e_eur.insert(0, round(float(e_kzt.get()) * float(rates.get_exchange_rate('EUR', from_kzt=False)), 2))
    e_try.insert(0, round(float(e_kzt.get()) * float(rates.get_exchange_rate('TRY', from_kzt=False)), 2))
    e_rub.insert(0, round(float(e_kzt.get()) * float(rates.get_exchange_rate('RUB', from_kzt=False)), 2))
    e_cny.insert(0, round(float(e_kzt.get()) * float(rates.get_exchange_rate('CNY', from_kzt=False)), 2))


rates = Rates()
from_tenge = rates.get_exchange_rates(from_kzt=True)
to_tenge = rates.get_exchange_rates()

usd1 = from_tenge['rates']['USD']
eur1 = from_tenge['rates']['EUR']
tryy1 = from_tenge['rates']['TRY']
rub1 = from_tenge['rates']['RUB']
cny1 = from_tenge['rates']['CNY']
usd2 = to_tenge['rates']['USD']
eur2 = to_tenge['rates']['EUR']
tryy2 = to_tenge['rates']['TRY']
rub2 = to_tenge['rates']['RUB']
cny2 = to_tenge['rates']['CNY']

# print(f'Today is {date.today()}, and the echange rates are:')
# print(f'1 USD is {usd1} Tenge, and 1 Tenge is {usd2} USD')
# print(f'1 EUR is {eur1} Tenge, and 1 Tenge is {eur2} EUR')
# print(f'1 TRY is {tryy1} Tenge, and 1 Tenge is {tryy2} TRY')
# print(f'1 RUB is {rub1} Tenge, and 1 Tenge is {rub2} RUB')
# print(f'1 CNY is {cny1} Tenge, and 1 Tenge is {cny2} CNY')

root = Tk()
root.title('Конвертер валют')
root.geometry('300x350+300+300')
root.resizable(width=False, height=False)
root['bg'] = 'black'

header_frame = Frame(root)
header_frame.pack(fill=X)

header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

h_currency = Label(header_frame, text='Валюта', bg='black', fg='lime', font='Arial 12 bold')
h_currency.grid(row=0, column=0, sticky=EW)

h_course = Label(header_frame, text='Курс', bg='black', fg='lime', font='Arial 12 bold')
h_course.grid(row=0, column=1, columnspan=2, sticky=EW)

# USD курс
usd_currency = Label(header_frame, text='USD', font='Arial 10')
usd_currency.grid(row=1, column=0, sticky=EW)
# usd_one = Label(header_frame, text='1', font='Arial 10')
# usd_one.grid(row=1, column=1, sticky=EW)
usd_converted = Label(header_frame, text=usd1, font='Arial 10')
usd_converted.grid(row=1, column=1, columnspan=2, sticky=EW)

# EUR курс
eur_currency = Label(header_frame, text='EUR', font='Arial 10')
eur_currency.grid(row=2, column=0, sticky=EW)
# eur_one = Label(header_frame, text='1', font='Arial 10')
# eur_one.grid(row=2, column=1, sticky=EW)
eur_converted = Label(header_frame, text=eur1, font='Arial 10')
eur_converted.grid(row=2, column=1, columnspan=2, sticky=EW)

# TRY курс
try_currency = Label(header_frame, text='TRY', font='Arial 10')
try_currency.grid(row=3, column=0, sticky=EW)
try_converted = Label(header_frame, text=tryy1, font='Arial 10')
try_converted.grid(row=3, column=1, columnspan=2, sticky=EW)

# RUB курс
rub_currency = Label(header_frame, text='RUB', font='Arial 10')
rub_currency.grid(row=4, column=0, sticky=EW)
rub_converted = Label(header_frame, text=rub1, font='Arial 10')
rub_converted.grid(row=4, column=1, columnspan=2, sticky=EW)

# CNY курс
cny_currency = Label(header_frame, text='CNY', font='Arial 10')
cny_currency.grid(row=5, column=0, sticky=EW)
cny_converted = Label(header_frame, text=cny1, font='Arial 10')
cny_converted.grid(row=5, column=1, columnspan=2, sticky=EW)

# Calculation
calc_frame = Frame(root, bg='black')
calc_frame.pack(expand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1, weight=1)

# KZT
l_kzt = Label(calc_frame, text='Тенге', bg='black', fg='lime', font='Arial 12 bold')
l_kzt.grid(row=0, column=0, padx=10)
e_kzt = Entry(calc_frame, justify=CENTER, font='Arial 10')
e_kzt.grid(row=0, column=1, columnspan=2, pady=10, padx=10, sticky=EW)

btn_calc = Button(calc_frame, text='Конвертировать', command=exchange)
btn_calc.grid(row=1, column=1, columnspan=2, sticky=EW, padx=10)

res_frame = Frame(root)
res_frame.pack(expand=1, fill=BOTH, pady=5)
res_frame.grid_columnconfigure(1, weight=1)

# USD
l_usd = Label(res_frame, text='USD', font='Arial 10 bold')
l_usd.grid(row=2, column=0)
e_usd = Entry(res_frame, justify=CENTER, font='Arial 10')
e_usd.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)

# EUR
l_eur = Label(res_frame, text='EUR', font='Arial 10 bold')
l_eur.grid(row=3, column=0)
e_eur = Entry(res_frame, justify=CENTER, font='Arial 10')
e_eur.grid(row=3, column=1, columnspan=2, padx=10, sticky=EW)

# TRY
l_try = Label(res_frame, text='TRY', font='Arial 10 bold')
l_try.grid(row=4, column=0)
e_try = Entry(res_frame, justify=CENTER, font='Arial 10')
e_try.grid(row=4, column=1, columnspan=2, padx=10, sticky=EW)

# RUB
l_rub = Label(res_frame, text='RUB', font='Arial 10 bold')
l_rub.grid(row=5, column=0)
e_rub = Entry(res_frame, justify=CENTER, font='Arial 10')
e_rub.grid(row=5, column=1, columnspan=2, padx=10, sticky=EW)

# CNY
l_cny = Label(res_frame, text='CNY', font='Arial 10 bold')
l_cny.grid(row=6, column=0)
e_cny = Entry(res_frame, justify=CENTER, font='Arial 10')
e_cny.grid(row=6, column=1, columnspan=2, padx=10, sticky=EW)

root.mainloop()

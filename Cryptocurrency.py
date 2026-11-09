# import requests
# import json
# #
# result = requests.get('https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin&names=Bitcoin&symbols=btc')
# data = json.loads(result.text)
#
#
# print(data)
# iiii = data['bitcoin']['usd']
# print(iiii)

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_currency_label(event):
    # Получаем полное название валюты из словаря и обновляем метку
    code = combobox.get()
    name = currencies[code]
    currency_label.config(text=name)

def exchange():
    code = combobox.get()

    if code:
        try:
            response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&symbols={code}')
            response.raise_for_status()
            data = response.json()

            if code in data:
                exchange_rate = data[code]['usd']
                currency_name = currencies.get(code, code)
                mb.showinfo("Курс обмена", f"Курс {exchange_rate:.2f} $ (Доллар США) за 1{code} ({currency_name})")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите код валюты")

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты к доллару")
window.geometry("360x180")

Label(text="Выберите код валюты:").pack(padx=10, pady=10)

combobox = ttk.Combobox(values=list(currencies.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()
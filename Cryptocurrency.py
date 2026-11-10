from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_currency_label(event):
    # Получаем полное название криптовалют из словаря и обновляем метку
    code = combobox.get()
    name = currencies[code]
    currency_label.config(text=name)

def exchange():
    code = combobox.get()

    if code:
        try:
            response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids={code}')
            response.raise_for_status()
            data = response.json()

            if code in data:
                exchange_rate = data[code]['usd']
                currency_name = currencies.get(code, code)
                mb.showinfo("Курс обмена", f"Курс {exchange_rate:.2f} $ (Доллар США) за 1{code} ({currency_name})")
            else:
                mb.showerror("Ошибка", f"Криптовалюты {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите код Криптовалюты")
# Словарь кодов криптовалют и их полных названий
currencies = {
    "bitcoin": "Биткоин",
    "ethereum": "Эфириум",
    "tether": "Тезер",
    "binancecoin": "Бинанс коин",
    "ripple": "XRP",
    "usd-coin": "USD Coin",
    "solana": "Солана",
    "tron": "ТРОН",
    "figure-heloc": "Фигюр Хелок",
    "staked-ether": "Lido Staked Ether"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена криптовалюты к доллару")
window.geometry("400x180")

Label(text="Выберите код криптовалюты:").pack(padx=10, pady=10)

combobox = ttk.Combobox(values=list(currencies.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()
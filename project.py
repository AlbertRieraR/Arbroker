import requests
import sys
import locale
from datetime import datetime, timedelta
import pandas as pd
from dictionary import sapo

prices = {}
locale.setlocale(locale.LC_NUMERIC, "es_ES.UTF-8")


symbols = {}
for key, value in sapo.items():
    symbols[value] = key


def main():
    for token in symbols:
        print(f"{token} - {symbols[token]}")
    symbol = input("API Token: ").strip().upper()
    try:
        days = int(input("Days: ").strip())
    except ValueError:
        sys.exit("Invalid days number")
    try:
        perc, price, date = get_data(symbol)
        finalprice = compound_interest(price, perc, days)
    except:
        sys.exit("Invalid API Token")
    else:
        lastprint = final_price(days, symbol, finalprice, price, str(perc), date)
        print(lastprint)


def get_data(a):
    try:
        api = f"https://finnhub.io/api/v1/quote?symbol={a}&token=cqfd951r01qle0e3fd6gcqfd951r01qle0e3fd70"
        response = requests.get(api)
        data = response.json()
        price = float(data["o"])
        perc = data["dp"]
        date = data["t"]
        return perc, price, date
    except:
        sys.exit("Invalid API Token")


def compound_interest(a, b, c):
    return round(a * (1 + b / 100) ** c, 2)


def conversion():
    url = "https://v6.exchangerate-api.com/v6/395838d8e93891027fe82ddd/latest/USD"
    response = requests.get(url)
    usd_eur = response.json()
    return float(round(usd_eur["conversion_rates"]["EUR"], 2))


def decimal_point(a, b):
    difference = conversion()
    z = locale.format_string("%.2f", a * difference, grouping=True)
    x = locale.format_string("%.2f", b * difference, grouping=True)
    return z, x


def get_date(a):
    dt_object = datetime.fromtimestamp(a)
    return dt_object.strftime("%d-%m-%Y %H:%M:%S")


def final_price(a, b, c, d, e, f):
    if e[0] != "-":
        e = "+" + e

    x, z = decimal_point(d, c)
    date = get_date(f)

    return f"\n-----------\nLast update: {date}\n-----$----- \nActual Price: {d:,.2f}$ \nChange Percentatge: {e}% \nIn {a} days, the price of {symbols[b]} will be: {c:,.2f}$ \n-----€----- \nActual Price: {x}€ \nChange Percentatge: {e}% \nIn {a} days, the price of {symbols[b]} will be: {z}€"


if __name__ == "__main__":
    main()

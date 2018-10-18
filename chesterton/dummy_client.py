import requests

base_url = "http://localhost:8888"

def get_stock():
    symbol = "tlt"
    url = "{}/stock/{}".format(base_url, symbol)
    stock = requests.get(url).json()
    print(stock)
    return stock

def get_option_positions():
    symbol = "tlt"
    url = "{}/option_positions".format(base_url)
    oos = requests.get(url).json()
    msg = "Option Positions, count = {}".format(len(oos))
    print(msg)
    return oos

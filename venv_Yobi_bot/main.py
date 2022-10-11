import requests
from config import API_KEY, API_SECRET
import time
from urllib.parse import urlencode
import hmac
import hashlib

def get_ticker(coin1="btc", coin2="usd"):
    response = requests.get(url=f"https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1")
    return response.json()

def get_info():
    values = {}
    values["method"] = "getInfo"
    values["nonce"] = str(int(time.time()))

    body = urlencode(values).encode("utf-8")
    sign = hmac.new(API_SECRET.encode("utf-8"),body, hashlib.sha512).hexdigest()

    headers = {
        "key": API_KEY,
        "sign": sign
    }

    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)
    return response.json()

def get_deposit_address(coin_name="btc"):
    values = dict()
    values["method"] = "GetDepositAddress"
    values["coinName"] = coin_name
    values["need_new"] = 0
    values["nonce"] = str(int(time.time()))

    body = urlencode(values).encode("utf-8")
    sign = hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()

    headers = {
        "key": API_KEY,
        "sign": sign
    }

    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)
    return response.json()

def buy_coin(coin1="eth", coin2="usd", rate=None, amount=0):
    ticker = get_ticker(coin1, coin2)
    sell_price = ticker[f"{coin1}_{coin2}"]["sell"]
    values = dict()
    values["method"] = "Trade"
    values["nonce"] = str(int(time.time()))
    values["pair"] = f"{coin1}_{coin2}"
    values["type"] = "buy"
    values["rate"] = sell_price if rate is None else rate
    # values["amount"] = amount
    values["amount"] = amount / (sell_price if rate is None else rate)
    # return values

    body = urlencode(values).encode("utf-8")
    sign = hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()

    headers = {
        "key": API_KEY,
        "sign": sign
    }

    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)

    return response.json()

def sell_coin(coin1="eth", coin2="usd", rate=None, amount=0):
    ticker = get_ticker(coin1, coin2)
    buy_price = ticker[f"{coin1}_{coin2}"]["buy"]
    values = dict()
    values["method"] = "Trade"
    values["nonce"] = str(int(time.time()))
    values["pair"] = f"{coin1}_{coin2}"
    values["type"] = "sell"
    values["rate"] = buy_price if rate is None else rate
    values["amount"] = amount
    # values["amount"] = amount / (buy_price if rate is None else rate)
    # return values

    body = urlencode(values).encode("utf-8")
    sign = hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()

    headers = {
        "key": API_KEY,
        "sign": sign
    }

    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)

    return response.json()

def cancel_order(order_id):
    values = dict()
    values["method"] = "CancelOrder"
    values["nonce"] = str(int(time.time()))
    values["order_id"] = order_id

    body = urlencode(values).encode("utf-8")
    sign = hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()

    headers = {
        "key": API_KEY,
        "sign": sign
    }

    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)

    return response.json()

def main():
    # coin_name = input("Enter a coin name: ")
    # print(get_deposit_address(coin_name=coin_name))
    print(get_info())
    # print(get_ticker(coin1="usd", coin2="rur"))
    # print(buy_coin())
    # print(buy_coin(rate=800))
    # print(buy_coin(rate= 800, amount=1))
    # print(cancel_order(1500103724275144))
    print(sell_coin(coin1="usd", coin2="rur", amount=1))

if __name__ == '__main__':
    main()

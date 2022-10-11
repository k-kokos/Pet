from binance.client import Client
import pandas as pd
import ta
from binance.exceptions import BinanceAPIException
from time import sleep
api_key = 'GugGlYbS587NFLPxdrBoQ8uPqgO2r2uANcH3mOghnZKYp9oDJtdMz9vkdLX7lrZD'
api_secret = 'HUFrT07RzfJaJrDXJG20mZ9hudX9kOQm7Pzomg3FFV5YtJikGHIIhmV2bdPJuqx8'
client = Client(api_key=api_key, api_secret=api_secret)


def klines(symbol):
    try:
        df = pd.DataFrame(client.get_historical_klines(symbol, '1m', '40m UTC'))
    except BinanceAPIException as e:
        print(e)
        sleep(60)
        df = pd.DataFrame(client.get_historical_klines(symbol, '1m', '40m UTC'))

    df = df.iloc[:, :6]
    df.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    df = df.set_index('Time')
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df.astype(float)
    return df


def strategy(symbol, qty, open_position=False):
    while True:
        df = klines(symbol)
        if not open_position:
            if ta.trend.macd_diff(df.Close).iloc[-1] > 0 \
                    and ta.trend.macd_diff(df.Close).iloc[-2] < 0:
                order = client.create_order(symbol=symbol, side='BUY', type='MARKET', quantity=qty)
                print(order)
                open_position = True
                buyprice = float(order['fills'][0]['price'])
                break

    if open_position:
        while True:
            df = klines(symbol)
            if ta.trend.macd_diff(df.Close).iloc[-1] < 0 \
                    and ta.trend.macd_diff(df.Close).iloc[-2] > 0:
                order = client.create_order(symbol=symbol, side='SELL', type='MARKET', quantity=qty)
                print(order)
                sellprice = float(order['fills'][0]['price'])
                print(f'profit = {(sellprice - buyprice) / buyprice}')
                open_position = False
                break

while True:
    strategy('ETHBTC', qty=0.01)
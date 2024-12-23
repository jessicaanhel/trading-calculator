import ccxt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def get_historical_data(symbol, timeframe, since_days=90):
    exchange = ccxt.binance()
    since = exchange.parse8601((datetime.utcnow() - timedelta(days=since_days)).strftime('%Y-%m-%dT%H:%M:%S'))
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since=since)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df


def calculate_atr(data, period=14):
    data['H-L'] = data['high'] - data['low']
    data['H-C'] = abs(data['high'] - data['close'].shift(1))
    data['L-C'] = abs(data['low'] - data['close'].shift(1))
    data['TR'] = data[['H-L', 'H-C', 'L-C']].max(axis=1)
    data['ATR'] = data['TR'].rolling(window=period).mean()
    return data


symbol = 'BTC/USDT'
timeframe = '1h'  # 1h, 1d
data = get_historical_data(symbol, timeframe)
data = calculate_atr(data)
print(data.tail())  # Check last ATR values

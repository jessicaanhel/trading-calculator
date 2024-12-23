import ccxt
import numpy as np

# Binance
api_key = ""
api_secret = ""

exchange = ccxt.binance({
    "apiKey": api_key,
    "secret": api_secret,
    "enableRateLimit": True
})

# Trade FUTURE settings
symbol = "BTC/USDT"
amount = 0.001       # ammount of symbol per order
min_price = 65300    # min expected price
max_price = 65800    # max expected price
atr = 380            # ATR for take-profit
num_orders = 10
k_tp = 1.5           # take-profit %

# Generate order levels and TP
order_step = (max_price - min_price) / num_orders
order_levels = np.arange(min_price, max_price, order_step)
take_profits = order_levels + atr * k_tp

# Realize orders by API
for i, level in enumerate(order_levels):
    try:
        # Limit buy order
        order = exchange.create_limit_buy_order(
            symbol=symbol,
            amount=amount,
            price=level
        )
        print(f"Buy Order {i+1} placed at {level:.2f}")

        # Set TP
        tp_price = take_profits[i]
        tp_order = exchange.create_limit_sell_order(
            symbol=symbol,
            amount=amount,
            price=tp_price
        )
        print(f"Take-Profit {i+1} placed at {tp_price:.2f}")
    except Exception as e:
        print(f"Error placing order {i+1}: {e}")

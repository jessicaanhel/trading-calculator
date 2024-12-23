import ccxt
import numpy as np

# Binance api keys
api_key = ""
api_secret = ""

exchange = ccxt.binance({
    "apiKey": api_key,
    "secret": api_secret,
    "enableRateLimit": True
})

# Parameters
symbol = "BTC/USDT"
amount = 0.001       # amount of symbol to buy
min_price = 65300
max_price = 65800
atr = 380
num_orders = 10
k_tp = 1.5           # TP %
k_sl = 1.0           # SL %


order_step = (max_price - min_price) / num_orders
order_levels = np.arange(min_price, max_price, order_step)
take_profits = order_levels + atr * k_tp
stop_losses = order_levels - atr * k_sl

# Orders placement
for i, level in enumerate(order_levels):
    try:
        # Limit order
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

        # Set SL
        sl_price = stop_losses[i]
        sl_order = exchange.create_order(
            symbol=symbol,
            type='stop_loss_limit',  # Order typr
            side='sell',
            amount=amount,
            price=sl_price,  # activation price
            params={'stopPrice': sl_price}  # activation price for stop_loss
        )
        print(f"Stop-Loss {i+1} placed at {sl_price:.2f}")

    except Exception as e:
        print(f"Error placing order {i+1}: {e}")

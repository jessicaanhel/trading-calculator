import numpy as np

# parameters
min_price = 65300  # minimal price for last 3m
max_price = 65800  # max price for last 3m
atr = 380          # last ATR
num_orders = 10    # numbers of orders
k_tp = 1.5         # take-profit %
k_sl = 1.0         # Stop-loss %

order_step = (max_price - min_price) / num_orders

order_levels = np.arange(min_price, max_price, order_step)
take_profits = order_levels + atr * k_tp
stop_losses = order_levels - atr * k_sl

# Result
for i, level in enumerate(order_levels):
    print(f"Order {i+1}:")
    print(f"  Level: {level:.2f}")
    print(f"  Take-Profit: {take_profits[i]:.2f}")
    print(f"  Stop-Loss: {stop_losses[i]:.2f}\n")

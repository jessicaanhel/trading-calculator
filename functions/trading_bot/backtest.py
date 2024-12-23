import pandas as pd
import numpy as np

def backtest_strategy(data, min_price, max_price, atr, num_orders=10, k_tp=1.5, k_sl=1.0, total_capital=1000):
    """
    Backtesting trading strategy on historical data with a fixed total capital across all orders.
    :param data: DataFrame with OHLCV data (must include 'high' and 'low' columns).
    :param min_price: Minimum price for order placement.
    :param max_price: Maximum price for order placement.
    :param atr: Average True Range for TP/SL calculation.
    :param num_orders: Number of orders to simulate.
    :param k_tp: Multiplier for take-profit.
    :param k_sl: Multiplier for stop-loss.
    :param total_capital: Total capital to be evenly divided across all orders.
    :return: Dictionary with backtesting results.
    """
    # Calculate amount per order based on total capital
    amount_per_trade = total_capital / num_orders

    # Generate order levels
    order_step = (max_price - min_price) / num_orders
    order_levels = np.arange(min_price, max_price, order_step)
    take_profits = order_levels + atr * k_tp
    stop_losses = order_levels - atr * k_sl

    # Variables for tracking performance
    total_profit = 0
    num_tp = 0
    num_sl = 0
    profit_tp = 0
    loss_sl = 0
    trades = []

    # Backtest simulation
    for i, row in data.iterrows():
        for j, level in enumerate(order_levels):
            # Check if the order level is reached
            if row['low'] <= level <= row['high']:
                entry_price = level
                tp_price = take_profits[j]
                sl_price = stop_losses[j]

                # Check for take-profit or stop-loss
                if row['high'] >= tp_price:
                    profit = (tp_price - entry_price) * amount_per_trade
                    trades.append({'entry': entry_price, 'exit': tp_price, 'profit': profit})
                    total_profit += profit
                    profit_tp += profit
                    num_tp += 1
                elif row['low'] <= sl_price:
                    loss = (entry_price - sl_price) * amount_per_trade
                    trades.append({'entry': entry_price, 'exit': sl_price, 'profit': -loss})
                    total_profit -= loss
                    loss_sl += loss
                    num_sl += 1

    num_trades = len(trades)
    profitable_trades = sum(1 for t in trades if t['profit'] > 0)
    win_rate = profitable_trades / num_trades * 100 if num_trades > 0 else 0

    return {
        'total_profit': total_profit,
        'num_trades': num_trades,
        'win_rate': win_rate,
        'num_tp': num_tp,          # Number of take-profits
        'num_sl': num_sl,          # Number of stop-losses
        'profit_tp': profit_tp,    # Total profit from take-profits
        'loss_sl': loss_sl,        # Total loss from stop-losses
        'trades': trades,          # Detailed trade log
        'total_investment': total_capital  # Total investment across all orders
    }

# Mocked OHLCV data
data = pd.DataFrame({
    'timestamp': pd.date_range(start='2024-10-01', periods=100, freq='h'),
    'open': np.random.uniform(65000, 66000, 100),
    'high': np.random.uniform(65500, 66500, 100),
    'low': np.random.uniform(64500, 65500, 100),
    'close': np.random.uniform(65000, 66000, 100),
})

# Parameters
min_price = 65300
max_price = 65800
atr = 380
num_orders = 10
k_tp = 1.5
k_sl = 1.0
usdt_total_capital = 1000

# Calling function
results = backtest_strategy(data, min_price, max_price, atr, num_orders, k_tp, k_sl, usdt_total_capital)

# Display results
print(f"Total Profit in $: {results['total_profit']:.2f}")
print(f"Number of Trades: {results['num_trades']}")
print(f"Win Rate: {results['win_rate']:.2f}%")
print(f"Number of Take-Profits: {results['num_tp']}")
print(f"Number of Stop-Losses: {results['num_sl']}")
print(f"Total Take-Profit Amount $: {results['profit_tp']:.2f}")
print(f"Total Stop-Loss Amount $: {results['loss_sl']:.2f}")
print(f"Total Investment in $: {results['total_investment']:.2f}")

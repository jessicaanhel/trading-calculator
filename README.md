## Column Explanation
1. timestamp: The time at which the candlestick (OHLC) data was recorded.

* Example: 2024-10-15 04:00:00 means the candlestick represents price movement from 4:00 to 5:00 UTC.
open, high, low, close: Standard OHLC values for the candlestick.

2. open: Price at the start of the hour.
* high: Highest price during the hour.
* low: Lowest price during the hour.
* close: Price at the end of the hour.
* L-C (Low-Close): The absolute difference between the current candlestick's low and the previous close.

Used to calculate the True Range (TR).
3. TR (True Range): The largest of the following:

* High - Low (price range for the current hour).
* High - Previous Close (gap up).
* Low - Previous Close (gap down).
* TR reflects the actual price movement, accounting for gaps between candlesticks.
* ATR (Average True Range): A moving average of the True Range (TR) over the last 14 periods (default).

4. ATR measures volatility:
* A higher ATR means the price fluctuates significantly.
* A lower ATR means the market is less volatile.

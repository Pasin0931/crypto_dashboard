import requests

class token_data:
    def __init__(self, token_symbol):
        self.token_symbol = token_symbol

    def get_current_price(self):
        # 1. Get Current Price
        url = "https://api.binance.com/api/v3/ticker/price"
        params = {"symbol": self.token_symbol}
        response = requests.get(url, params=params)
        this_res = response.json()
        print(this_res)                  # Get real time price
        # {"symbol": "BTCUSDT", "price": "95234.50"}

    def get_24H_static(self):
        # 2. Get 24-Hour Statistics
        url = "https://api.binance.com/api/v3/ticker/24hr"
        params = {"symbol": self.token_symbol}
        response = requests.get(url, params=params)
        data = response.json()
        # print(data)                                    # Get statistic
        # -------------------------
        print(f"Price: ${data['lastPrice']}")
        print(f"24h Change: {data['priceChangePercent']}%")
        print(f"24h Volume: {data['volume']} BTC")
        print(f"High: ${data['highPrice']}")
        print(f"Low: ${data['lowPrice']}")

    def get_order_book_depth(self):
        # 3. Get Order Book Depth
        url = "https://api.binance.com/api/v3/depth"
        params = {"symbol": self.token_symbol, "limit": 10}  # Top 10 bids/asks
        response = requests.get(url, params=params)
        data = response.json()

        # print(data["bids"])            # Get all bids

        # print("Top 5 Bids (Buy Orders):")
        # for price, quantity in data['bids'][:8]:
        #     print(f"  Price: ${price}, Quantity: {quantity} BTC")

        # print("\nTop 5 Asks (Sell Orders):")
        # for price, quantity in data['asks'][:8]:
        #     print(f"  Price: ${price}, Quantity: {quantity} BTC")

        set_data = {"bids": sorted(data["bids"][:8]).reverse(), "sells": sorted(data["asks"][:8])}
        print(set_data)
        # return set_data

    def get_recent_trades(self):
        # 4. Get Recent Trades
        url = "https://api.binance.com/api/v3/trades"
        params = {"symbol": "BTCUSDT", "limit": 5}
        response = requests.get(url, params=params)

        for trade in response.json():
            side = "BUY" if trade['isBuyerMaker'] else "SELL"
            print(f"{side}: {trade['qty']} BTC @ ${trade['price']}")

    def get_candle_stick_data(self):
        # 5. Get Candlestick (Kline) Data
        url = "https://api.binance.com/api/v3/klines"
        params = {
            "symbol": "BTCUSDT",
            "interval": "1h",  # 1m, 5m, 15m, 1h, 4h, 1d, 1w, 1M
            "limit": 24  # Last 24 hours
        }
        response = requests.get(url, params=params)

        for candle in response.json():
            timestamp = candle[0]
            open_price = candle[1]
            high = candle[2]
            low = candle[3]
            close = candle[4]
            volume = candle[5]
            print(f"Open: ${open_price}, High: ${high}, Low: ${low}, Close: ${close}")

this__ = token_data("BTCUSDT")
# this__.get_current_price()
# this__.get_24H_static()
# this__.get_order_book_depth()
this__.get_recent_trades()
# this__.get_candle_stick_data()
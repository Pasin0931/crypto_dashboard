import requests

# REST endpoint for current price
url = "https://api.binance.com/api/v3/ticker/price"
params = {"symbol": "BTCUSDT"}

response = requests.get(url, params=params)
data = response.json()

print(f"BTC Price: ${data['price']}")
# Output: BTC Price: $95234.50
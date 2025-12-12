import websocket
import json
import threading

class socket:
    def __init__(self, url, name):
        self.url = url
        self.name = name
        self.coin_data = None

    def on_message(self, ws, message):
        data = json.loads(message)
        self.coin_data = data
        # print(data)
        print(f"BTC Price: ${data['c']}")

    def on_error(self, ws, error):
        print(f"Error: {error}")

    def on_close(self, ws, close_status, close_msg):
        print("Connection closed")

    def on_open(self, ws):
        print("Connected to Binance")

    def setup_n_start_normal(self):
        ws = websocket.WebSocketApp(
            self.url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )
        ws.run_forever()

    def setup_n_start_threading(self):
        ws = websocket.WebSocketApp(
            self.url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )
        thread = threading.Thread(target=ws.run_forever, daemon=True)
        thread.start()
        return ws
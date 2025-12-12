import websocket
import json
import threading

class socket:
    def __init__(self, url, name):
        self.url = url
        self.name = name
        self.coin_data = {"s": "N/A", "c": "N/A", "v": 0, "P": 0, "p": 0}

        self.is_running = False
        self.ws = None

        self.update_callback = None # --

    def on_message(self, ws, message):
        data = json.loads(message)
        self.coin_data = data
        # print(data)
        print(f"BTC Price: ${data['c']}")

        if self.update_callback:         # --
            self.update_callback(data)   # --

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
        ws_ = websocket.WebSocketApp(
            self.url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )
        thread = threading.Thread(target=ws_.run_forever, daemon=True)
        thread.start()

        self.ws = ws_
        self.is_running = True

        return ws_

    def set_update_callback(self, callback_function):  # --
        self.update_callback = callback_function       # --

    def stop_socket(self):
        try:
            self.running = False
            self.is_running = False
            if self.ws:
                self.ws.close()
                self.ws = None
            print(f"Socket stopped for {self.name}")

        except Exception as e:
            print(f"Error while stopping socket: {e}")
import tkinter as tk
from tkinter import ttk
import websocket
import json
import threading

class BTCTicker:
    def __init__(self, root):
        self.root = root
        self.root.title("BTC Price Ticker")
        self.root.geometry("400x200")
        
        self.is_closing = False
        self.ws = None
        
        # UI Setup
        self.setup_ui()
        
        # Start WebSocket
        self.start_websocket()
    
    def setup_ui(self):
        # Title
        title = ttk.Label(self.root, text="BTC/USDT", 
                         font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Price Display
        self.price_label = tk.Label(self.root, text="--,---", 
                                    font=("Arial", 48, "bold"),
                                    fg="black")
        self.price_label.pack(pady=20)
        
        # Change Display
        self.change_label = ttk.Label(self.root, text="--", 
                                      font=("Arial", 14))
        self.change_label.pack()
    
    def start_websocket(self):
        """Start WebSocket connection in background thread."""
        ws_url = "wss://stream.binance.com:9443/ws/btcusdt@ticker"
        
        self.ws = websocket.WebSocketApp(
            ws_url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )
        
        # Run in separate thread to not block GUI
        ws_thread = threading.Thread(target=self.ws.run_forever, daemon=True)
        ws_thread.start()
    
    def on_message(self, ws, message):
        """Handle incoming WebSocket messages."""
        if self.is_closing:
            return
        
        data = json.loads(message)
        price = float(data['c'])  # Current price
        change = float(data['p'])  # 24h price change
        percent = float(data['P'])  # 24h percent change
        
        # Update GUI (must use root.after for thread safety)
        self.root.after(0, self.update_display, price, change, percent)
    
    def update_display(self, price, change, percent):
        """Update the display with new price data."""
        if self.is_closing:
            return
        
        # Determine color based on change
        color = "green" if change >= 0 else "red"
        
        # Update price
        self.price_label.config(text=f"{price:,.2f}", fg=color)
        
        # Update change
        sign = "+" if change >= 0 else ""
        change_text = f"{sign}{change:,.2f} ({sign}{percent:.2f}%)"
        self.change_label.config(text=change_text, foreground=color)
    
    def on_error(self, ws, error):
        print(f"WebSocket Error: {error}")
    
    def on_close(self, ws, status, msg):
        print("WebSocket Closed")
    
    def on_open(self, ws):
        print("WebSocket Connected")
    
    def on_closing(self):
        """Clean up when closing."""
        self.is_closing = True
        if self.ws:
            self.ws.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BTCTicker(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

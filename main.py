import tkinter as tk
from tkinter import ttk, OptionMenu, StringVar

from libs.widget_lib import System, Widget, Label, Button, Frame
from libs.lib_socket import socket

def update_live_ui(data):   # Upadte token data real time
    live_coin.config(text=data["s"])
    live_price.config(text=f"${float(data['c']):.3f}")
    live_volume.config(text=f"Volume: {float(data['v']):.3f}")
    live_change_amount.config(text=f"Change: {float(data['p']):.3f}")
    live_change_percent.config(text=f"Change (%): {data['P']}%")

operator = System()
this_root = operator.initiate()

screen = Widget(this_root)
label = Label(this_root)
button = Button(this_root)
frame = Frame(this_root)

token_ = socket("wss://stream.binance.com:9443/ws/btcusdt@ticker", "BTC-USDT")

# ----------------------------------- header
header_ = label.create_label(None, "BTC/UTC Dashboard", 20, "bold")
header_.pack(anchor="ne", padx=50, pady=(38, 5))

sub_header = label.create_label(None, "This dashboard shows the value of bitcoin value", 12, "normal")
sub_header.pack(anchor="ne", padx=50, pady=(0, 20))

# ----------------------------------- frame for left/right side
main = frame.create_frame(None, "flat", 0, None, 0, 0)
main.pack(fill="both", expand=True, padx=10)

# ----------------------------------- bottom (transactions)
bottom_pannel = frame.create_frame(main, "flat", 0, None, 260, 0)
bottom_pannel.pack(side="bottom", fill="both", expand=False)

transaction = frame.create_frame(bottom_pannel, "flat", 0, None, 0, 0)
transaction.pack(side="left", anchor="n", padx=0, pady=(0,70))

transaction_ui = frame.create_frame(bottom_pannel, "ridge", 10, None, 800, 80)
transaction_ui.pack(anchor="n", pady=(0,25), expand=False)

# ----------------------------------- left side
left_panel = frame.create_frame(main, "flat", 0, None, 260, 0)
left_panel.pack(side="left", anchor="n", padx=(35,0), pady=10)

# Buttons
b1 = button.create_button(left_panel, "Reload", None)
b1.pack(ipadx=32, pady=(18,0))

# Dropdown
dropdown_var = StringVar(value="BTC")
dropdown_1 = OptionMenu(left_panel, dropdown_var, "BTC/USDT","ETH/USDT","BNB/USDT","XRP/USDT","SOL/USDT")
dropdown_1.config(width=16, bg="#1E1E1E", fg="white", highlightthickness=0)
dropdown_1.pack(pady=(18, 18))

# ------------------------------------------------------------------------------------------------------------------
# Live Price
live_box = frame.create_frame(left_panel, "ridge", 2, None, 0, 100)
live_box.pack()

left_col = tk.Frame(live_box, bg="#1E1E1E")
left_col.pack(side="left", anchor="nw", padx=10, pady=5)

right_col = tk.Frame(live_box, bg="#1E1E1E")
right_col.pack(side="left", anchor="nw", padx=20, pady=5)

# ---------------- LEFT
# Coin label
live_coin = tk.Label(left_col, text=token_.coin_data["s"], bg="#1E1E1E", fg="#AAAAAA", font=("Helvetica", 11, "bold"))
live_coin.pack(anchor="w")

# Price
live_price = tk.Label(left_col, text=token_.coin_data["c"], bg="#1E1E1E", fg="white", font=("Helvetica", 18, "bold"))
live_price.pack(anchor="w")

# ---------------- RIGHT
# Volume
live_volume = tk.Label(right_col, text=f"Volume: {token_.coin_data['v']}", bg="#1E1E1E", fg="#AAAAAA", font=("Helvetica", 10))
live_volume.pack(anchor="w", pady=2)

# Change amount
live_change_amount = tk.Label(right_col, text=f"Change: {token_.coin_data['p']}", bg="#1E1E1E", fg="white", font=("Helvetica", 10))
live_change_amount.pack(anchor="w", pady=2)

# Change percent
live_change_percent = tk.Label(right_col, text=f"Change %: {token_.coin_data['P']}", bg="#1E1E1E", fg="#AAAAAA", font=("Helvetica", 10))
live_change_percent.pack(anchor="w", pady=2)

# ------------------------------------------------------------------------------------------------------------------

# Bid and Sell Panels
bid_sell_container = frame.create_frame(left_panel, "flat", 0, None, 0, 0)
bid_sell_container.pack(pady=20)

bid_ = frame.create_frame(bid_sell_container, "ridge", 10, None, 260, 310)
bid_.pack(side="left", padx=10)

sell_ = frame.create_frame(bid_sell_container, "ridge", 10, None, 260, 310)
sell_.pack(side="left", padx=10)

# ----------------------------------- right side
right_pannel = frame.create_frame(main, "flat", 0, None, 260, 0)
right_pannel.pack(side="right", anchor="n", padx=25, pady=10)

charts = frame.create_frame(right_pannel, "flat", 0, None, 0, 0)
charts.pack(side="left", fill="both", expand=True, padx=25, pady=(18,0))

main_chart = frame.create_frame(charts, "ridge", 10, None, 650, 360)
main_chart.pack(anchor="n", pady=10)

second_chart = frame.create_frame(charts, "ridge", 10, None, 650, 135)
second_chart.pack(anchor="n", pady=1)

# ----------------------------------- close buton
close_button = button.create_button(None, "close", comm=this_root.destroy)
close_button.pack(anchor="se", padx=30, pady=(20, 40))

if __name__ == "__main__":
    token_.set_update_callback(update_live_ui) # call back to update token data
    token_.setup_n_start_threading()
    this_root.mainloop()

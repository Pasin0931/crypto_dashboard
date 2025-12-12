import tkinter as tk
from tkinter import ttk, OptionMenu, StringVar

from libs.widget_lib import System, Widget, Label, Button, Frame

operator = System()
this_root = operator.initiate()

screen = Widget(this_root)
label = Label(this_root)
button = Button(this_root)
frame = Frame(this_root)

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
dropdown_1 = OptionMenu(left_panel, dropdown_var, "BTC/UTC", "MyCoin", "Plummet Coin")
dropdown_1.config(width=16, bg="#1E1E1E", fg="white", highlightthickness=0)
dropdown_1.pack(pady=(18, 18))

# ------------------------------------------------------------------------------------------------------------------
# Live Price
live_box = frame.create_frame(left_panel, "ridge", 2, None, 220, 90)
live_box.pack()

# Coin label
live_coin = tk.Label(live_box, text="BTC/USDT", bg="#1E1E1E", fg="#AAAAAA", font=("Helvetica", 11, "bold"))
live_coin.pack(anchor="w", padx=12, pady=(6, 0))

# Price label
live_price = tk.Label(live_box, text="$90,321.76", bg="#1E1E1E", fg="white", font=("Helvetica", 18, "bold"))
live_price.pack(anchor="w", padx=12)

# Percentage label
live_percent = tk.Label(live_box, text="-1.88%", bg="#1E1E1E", fg="#FF5555", font=("Helvetica", 11))
live_percent.pack(anchor="w", padx=12, pady=(0, 6))
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
    this_root.mainloop()

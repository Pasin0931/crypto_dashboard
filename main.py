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
header_ = label.create_label("BTC/UTC Dashboard", 20, "bold")
header_.pack(anchor="ne", padx=50, pady=(38, 5))

sub_header = label.create_label("This dashboard shows the value of bitcoin value", 12, "normal")
sub_header.pack(anchor="ne", padx=50, pady=(0, 20))

# ----------------------------------- frame for left/right side
main = tk.Frame(this_root, bg="#252526")
main.pack(fill="both", expand=True, padx=10)

# ----------------------------------- left side
left_panel = tk.Frame(main, bg="#252526")
left_panel.pack(side="left", anchor="n", padx=25, pady=10)

# Buttons
b1 = button.create_button("Menu", None)
b1.pack(in_=left_panel, ipadx=32)

# Dropdown
dropdown_var = StringVar(value="BTC")
dropdown_1 = OptionMenu(left_panel, dropdown_var, "BTC/UTC", "MyCoin", "Plummet Coin")
dropdown_1.config(width=16, bg="#1E1E1E", fg="white", highlightthickness=0)
dropdown_1.pack(pady=(20, 9))

# Bid and Sell Panels
bid_sell_container = tk.Frame(left_panel, bg="#252526")
bid_sell_container.pack(pady=20)

bid_ = frame.create_frame("ridge", 10, None, 200, 300)
bid_.pack(in_=bid_sell_container, side="left", padx=10)

sell_ = frame.create_frame("ridge", 10, None, 200, 300)
sell_.pack(in_=bid_sell_container, side="left", padx=10)

# ----------------------------------- right side
chart_panel = tk.Frame(main, bg="#252526")
chart_panel.pack(side="left", fill="both", expand=True, padx=25)

chart_ = frame.create_frame("ridge", 10, None, 650, 400)
chart_.pack(in_=chart_panel, anchor="n", pady=10)

# ----------------------------------- close buton
close_button = button.create_button("close", comm=this_root.destroy)
close_button.pack(anchor="se", padx=30, pady=(0, 40))

if __name__ == "__main__":
    this_root.mainloop()

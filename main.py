import tkinter as tk
from tkinter import ttk

from libs.widget_lib import System, Widget, Label, Button, Frame

operator = System()
this_root = operator.initiate()

screen = Widget(this_root)
label = Label(this_root)
button = Button(this_root)
frame = Frame(this_root)

header_ = label.create_label("BTC/UTC Dashboard", 20, "bold")
sub_header = label.create_label("This dashboard shows the value of bitcoin value", 12, "normal")
b1 = button.create_button("Menu", None)
b2 = button.create_button("Test1", None)
b3 = button.create_button("Test2", None)
frame_1 = frame.create_frame("ridge", 10, None, 650, 400)
close_button = button.create_button("close", comm=this_root.destroy)

header_.pack(anchor="e", padx=55, pady=(25, 0)) # Header
sub_header.pack(anchor="e", padx=55, pady=(0, 20))
# button_1.pack()
frame_1.pack(anchor='e', padx=30)
close_button.pack(anchor='se', pady=(25, 0), padx=40)

if __name__ == "__main__":
    this_root.mainloop()
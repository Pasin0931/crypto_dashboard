import tkinter as tk
from tkinter import ttk

from libs.widget_lib import System, Widget, Label, Button, Frame

operator = System()
this_root = operator.initiate()

screen = Widget(this_root)
label = Label(this_root)
button = Button(this_root)
frame = Frame(this_root)

label_1 = label.create_label("Hello world")
button_1 = button.create_button("button", None)
frame_1 = frame.create_frame("ridge", 10, None, 700, 400)

close_button = button.create_button("close", None)

label_1.pack()
button_1.pack()
frame_1.pack(padx=10, pady=10)

close_button.pack()

if __name__ == "__main__":
    this_root.mainloop()
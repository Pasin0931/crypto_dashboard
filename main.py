import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("My First App")
root.geometry("400x300")

# Create a label
label = ttk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# Create a button with an event handler
def on_button_click():
    label.config(text="Button Clicked!")

button = ttk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Start the event loop
root.mainloop()
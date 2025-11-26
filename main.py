import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My Crypto")
root.geometry("1000x600")

label = ttk.Label(root, text="Hello World !")
label.pack()

if __name__ == "__main__":
    root.mainloop()
import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Example widget
label = tk.Label(root, text="Hello, I'm visible!")
label.pack(pady=20)

def hide_label():
    label.pack_forget()  # hides the label

def show_label():
    label.pack(pady=20)  # shows the label again

# Buttons to hide/show
hide_btn = tk.Button(root, text="Hide", command=hide_label)
hide_btn.pack()

show_btn = tk.Button(root, text="Show", command=show_label)
show_btn.pack()

root.mainloop()

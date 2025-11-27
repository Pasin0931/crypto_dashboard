import tkinter as tk
from tkinter import ttk

class System:
    def __init__(self):
        return None

    def initiate(self):
        root = tk.Tk()
        root.config(bg="#252526")
        root.title("My Crypto")
        root.geometry("1070x578") # resize window
        return root
    
class Widget:
    def __init__(self, root):
        self.root = root
        self.all_widgets = []
        
    def pack_all(self):
        for i in self.all_widgets:
            i.pack()
            
class Label(Widget):
    def __init__(self, root):
        super().__init__(root)
    
    def create_label(self, msg, s, st):
        this_label = ttk.Label(self.root, text=msg)
        this_label.config(style='Big.TLabel', font=('Helvetica', s, st)) # normal/bold
        this_label.config(background="#252526", foreground="white")
        self.all_widgets.append(this_label)
        return this_label
    
class Button(Widget):
    def __init__(self, root):
        super().__init__(root)

    def create_button(self, msg, comm):
        this_button = ttk.Button(self.root, text=msg, command=comm)
        this_button.config(style="Crypto.TButton")
        style = ttk.Style()
        style.configure("Crypto.TButton", background="#1E1E1E", foreground="#000000")
        self.all_widgets.append(this_button)
        return this_button
    
class Frame(Widget):
    def __init__(self, root):
        super().__init__(root)
            
    def create_frame(self, r, bw, pd, w, h):
        this_frame = ttk.Frame(relief=r, borderwidth=bw, padding=pd, width=w, height=h)
        this_frame.config(style="Crypto.TFrame")
        style = ttk.Style()
        style.configure("Crypto.TFrame", background="#1E1E1E")
        self.all_widgets.append(this_frame)
        return this_frame
    
    
    
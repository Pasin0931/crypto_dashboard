import tkinter as tk
from tkinter import ttk

class System:
    def __init__(self):
        return None

    def initiate(self):
        root = tk.Tk()
        root.config(bg="#252526")
        root.title("My Crypto")
        root.geometry("1300x960") # resize window
        # root.resizable(False, False)
        root.minsize(200, 200)     # optional: allow shrinking to a minimum
        root.maxsize(1300, 960)    # prevent expanding beyond this
        return root
    
    def clean_bid_sale(self, list_order):
        for i in list_order.values():
            for j in i:
                for z in j:
                    # print(z)
                    z.destroy()
        list_order = {"left": [], "right": []}
        return list_order
    
    # def on_reload(self, list_order):
    #     # print("Hellooo")
    #     self.clean_bid_sale(list_order)
    #     print("reloaded")
    
    def hide_this(self, obj):
        if obj.winfo_viewable():
            obj.pack_forget()
        else:
            obj.pack(pady=20)

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
    
    def create_label(self, in_, msg, s, st):
        if in_ == None:
            r_ = self.root
        else:
            r_ = in_
        this_label = ttk.Label(r_, text=msg)
        this_label.config(style='Big.TLabel', font=('Helvetica', s, st)) # normal/bold
        this_label.config(background="#252526", foreground="white")
        self.all_widgets.append(this_label)
        return this_label
    
class Button(Widget):
    def __init__(self, root):
        super().__init__(root)

    def create_button(self, in_, msg, comm):
        if in_ == None:
            r_ = self.root
        else:
            r_ = in_
        this_button = ttk.Button(r_, text=msg, command=comm)
        this_button.config(style="Crypto.TButton")
        style = ttk.Style()
        style.configure("Crypto.TButton", background="#1E1E1E", foreground="#000000")
        self.all_widgets.append(this_button)
        return this_button
    
class Frame(Widget):
    def __init__(self, root):
        super().__init__(root)
            
    def create_frame(self, in_, r, bw, pd, w, h):
        if in_ == None:
            r_ = self.root
        else:
            r_ = in_
        this_frame = ttk.Frame(r_, relief=r, borderwidth=bw, padding=pd, width=w, height=h)
        this_frame.config(style="Crypto.TFrame")
        style = ttk.Style()
        style.configure("Crypto.TFrame", background="#1E1E1E")
        self.all_widgets.append(this_frame)
        return this_frame
    
    
    
import tkinter as tk
from tkinter import ttk

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Counter")
        
        self.count = 0
        
        # Display
        self.label = ttk.Label(root, text="Count: 0", font=("Arial", 24))
        self.label.pack(pady=20)
        
        # Buttons
        btn_frame = ttk.Frame(root)
        btn_frame.pack()
        
        ttk.Button(btn_frame, text="+", command=self.increment).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="-", command=self.decrement).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Reset", command=self.reset).pack(side=tk.LEFT, padx=5)
    
    def increment(self):
        self.count += 1
        self.update_display()
    
    def decrement(self):
        self.count -= 1
        self.update_display()
    
    def reset(self):
        self.count = 0
        self.update_display()
    
    def update_display(self):
        self.label.config(text=f"Count: {self.count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()

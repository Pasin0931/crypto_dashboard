# graphmaker.py
import tkinter as tk
from collections import deque
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.ticker import ScalarFormatter

class LiveGraph:
    def __init__(self, root, title="", ylabel="", max_points=150, size1=6, size2=2):
        self.size1 = size1
        self.size2 = size2

        self.root = root
        self.max_points = max_points

        self.x_data = deque(maxlen=max_points)
        self.y_data = deque(maxlen=max_points)

        # ------------------------- Graph Setup
        self.fig = Figure(figsize=(size1, size2), dpi=100)
        self.fig.patch.set_facecolor("#1E1E1E")   # FIGURE background

        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor("#1E1E1E")           # AXES background

        self.ax.set_title(title, color="white")
        self.ax.set_ylabel(ylabel, color="white")

        self.ax.tick_params(colors="white")        # ticks color
        self.ax.grid(True, color="#333333")

        self.line, = self.ax.plot([], [])

        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.ax.yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
        self.ax.ticklabel_format(style='plain', axis='y')


    def update(self, value):
        self.x_data.append(len(self.x_data))
        self.y_data.append(value)

        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()

        self.canvas.draw_idle()

    def clear(self):
        self.x_data.clear()
        self.y_data.clear()
        self.line.set_data([], [])
        self.canvas.draw_idle()

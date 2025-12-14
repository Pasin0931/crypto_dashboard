# graphmaker.py
import tkinter as tk
from collections import deque
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
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

class LiveCandleStick:
    def __init__(self, root, title="", ylabel="", max_points=60, size1=6, size2=4):
        self.root = root
        self.max_points = max_points

        self.opens = deque(maxlen=max_points)
        self.highs = deque(maxlen=max_points)
        self.lows  = deque(maxlen=max_points)
        self.closes = deque(maxlen=max_points)

        self.fig = Figure(figsize=(size1, size2), dpi=100)
        self.fig.patch.set_facecolor("#1E1E1E")

        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor("#1E1E1E")
        self.ax.set_title(title, color="white")
        self.ax.set_ylabel(ylabel, color="white")
        self.ax.tick_params(colors="white")
        self.ax.grid(True, color="#333333")

        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.current_candle = None

    def update(self, price):
        if self.current_candle is None:
            self.current_candle = {
                "open": price,
                "high": price,
                "low": price,
                "close": price
            }
            return
        
        self.current_candle["high"] = max(self.current_candle["high"], price)
        self.current_candle["low"] = min(self.current_candle["low"], price)
        self.current_candle["close"] = price

    def close_candle(self):
        if not self.current_candle:
            return

        self.opens.append(self.current_candle["open"])
        self.highs.append(self.current_candle["high"])
        self.lows.append(self.current_candle["low"])
        self.closes.append(self.current_candle["close"])

        self.current_candle = None
        self.draw()

    def draw(self):
        self.ax.clear()
        self.ax.set_facecolor("#1E1E1E")
        self.ax.grid(True, color="#333333")
        self.ax.tick_params(colors="white")

        for i, (o, h, l, c) in enumerate(
            zip(self.opens, self.highs, self.lows, self.closes)
        ):
            color = "green" if c >= o else "red"

            # Wick
            self.ax.plot([i, i], [l, h], color=color, linewidth=1)

            # Body
            rect = Rectangle(
                (i - 0.3, min(o, c)),
                0.6,
                abs(c - o),
                facecolor=color,
                edgecolor=color
            )
            self.ax.add_patch(rect)

        self.ax.autoscale_view()
        self.canvas.draw_idle()

    def clear(self):
        self.opens.clear()
        self.highs.clear()
        self.lows.clear()
        self.closes.clear()
        self.current_candle = None
        self.ax.clear()
        self.canvas.draw_idle()

    def load_from_api(self, candles):
        self.opens.clear()
        self.highs.clear()
        self.lows.clear()
        self.closes.clear()

        for c in candles:
            self.opens.append(float(c[1]))
            self.highs.append(float(c[2]))
            self.lows.append(float(c[3]))
            self.closes.append(float(c[4]))

        self.draw()


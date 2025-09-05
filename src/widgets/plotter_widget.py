import numpy as np
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QWidget, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class PlotterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.toolbar = None
        self.ax = None
        self.canvas = None
        self.figure = None
        self.init_components()
        self.init_layout()
        self.apply_styles()
        self.connect_signals()

    def init_components(self):
        self.figure = Figure(figsize=(5, 4), dpi=100, tight_layout=True)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.toolbar = NavigationToolbar(self.canvas, self)

    def init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def apply_styles(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            """
            PlotterWidget {
                background-color: #ffffff;
            }
            """
        )

    def connect_signals(self):
        pass

    def plot_functions(self, f1, f2, f1_expr: str = None, f2_expr: str = None, x_center=None, span=5.0, default_range=(-10, 10), annotate=None):
        self.ax.clear()

        if x_center is not None and np.isfinite(x_center):
            x_min = x_center - span
            x_max = x_center + span
        else:
            x_min, x_max = default_range

        xs = np.linspace(x_min, x_max, 1000)
        y1 = np.array([f1(x) for x in xs], dtype=float)
        y2 = np.array([f2(x) for x in xs], dtype=float)

        if (f1_expr is not None) and (f2_expr is not None):
            self.ax.plot(xs, y1, label=f"$f_1(x) = {f1_expr.replace('*', '')}$")
            self.ax.plot(xs, y2, label=f"$f_2(x) = {f2_expr.replace('*', '')}$")
        else:
            self.ax.plot(xs, y1, label="$f_1(x)")
            self.ax.plot(xs, y2, label="$f_2(x)")

        if annotate is not None and annotate[0] is not None:
            for (xr, yr) in annotate:
                if xr is not None and yr is not None and np.isfinite(xr) and np.isfinite(yr):
                    self.ax.scatter([xr], [yr], s=60, zorder=5)
                    self.ax.annotate(f"Solution\n(x={xr:.4g}, y={yr:.4g})",
                                     xy=(xr, yr),
                                     xytext=(10, 10),
                                     textcoords="offset points",
                                     bbox=dict(boxstyle="round,pad=0.3", fc="w", ec="0.5", alpha=0.9),
                                     arrowprops=dict(arrowstyle="->", lw=1))

        self.ax.grid(True, alpha=0.3)
        self.ax.legend(loc="best")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.set_title("PySolver Function Plotter")
        self.canvas.draw_idle()

    def clear(self):
        self.ax.clear()
        self.canvas.draw_idle()

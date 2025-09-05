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

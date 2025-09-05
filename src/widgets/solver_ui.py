from PySide2.QtWidgets import QWidget, QVBoxLayout

from src.widgets.input_widget import InputPanelWidget
from src.widgets.plotter_widget import PlotterWidget


class SolverUI(QWidget):
    def __init__(self):
        super().__init__()
        self.plotter = None
        self.layout = None
        self.input_panel = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Solver UI')
        self.setGeometry(100, 100, 400, 300)

        self.plotter = PlotterWidget(self)
        self.input_panel = InputPanelWidget(self)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)
        self.layout.addWidget(self.plotter)
        self.layout.addWidget(self.input_panel)

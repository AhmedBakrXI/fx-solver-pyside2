from PySide2.QtWidgets import (
    QWidget, QLineEdit, QVBoxLayout, QLabel, QGridLayout
)

class InputPanelWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_components()
        self.init_layout()
        self.apply_styles()
        self.connect_signals()

    def init_components(self):
        self.f1_label = QLabel('f1(x):')
        self.f1_input = QLineEdit()
        self.f1_input.setPlaceholderText('e.g., x^2 + 3*x - 4')

        self.f2_label = QLabel('f2(x):')
        self.f2_input = QLineEdit()
        self.f2_input.setPlaceholderText('e.g., 2*x + 1')


    def init_layout(self):
        grid = QGridLayout()
        grid.addWidget(self.f1_label, 0, 0)
        grid.addWidget(self.f1_input, 0, 1)
        grid.addWidget(self.f2_label, 1, 0)
        grid.addWidget(self.f2_input, 1, 1)
        self.setLayout(grid)

    def apply_styles(self):
        pass

    def connect_signals(self):
        pass


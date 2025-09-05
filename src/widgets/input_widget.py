from PySide2.QtGui import Qt
from PySide2.QtWidgets import (
    QWidget, QLineEdit, QVBoxLayout, QLabel, QGridLayout
)

class InputPanelWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.f2_input = None
        self.f2_label = None
        self.f1_input = None
        self.f1_label = None
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
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            """
            InputPanelWidget {
                background-color: #f0f0f0;
                color: #ffffff;
                max-height: 120px;
                border-top: 1px solid #cccccc;
                border-radius: 16px;
            }
            QLineEdit {
                background-color: #ffffff;
                border-radius: 8px;
                border: 1px solid #cccccc;
                height: 20px;
                min-width: 100px;
                padding: 4px;
            }
            QLabel {
                font-weight: bold;
                font-size: 14px;
                color: #0000ff;
            }
            """
        )

    def connect_signals(self):
        pass


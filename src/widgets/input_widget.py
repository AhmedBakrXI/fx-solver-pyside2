from PySide2.QtGui import Qt
from PySide2.QtWidgets import (
    QWidget, QLineEdit, QLabel, QGridLayout, QDoubleSpinBox, QHBoxLayout, QPushButton
)

"""
InputPanelWidget is a QWidget that provides input fields for two functions, range limits, and a span value.
It includes "Solve" and "Clear" buttons to trigger actions.
It uses a grid layout for organized placement of components and applies custom styles for child components.
"""
class InputPanelWidget(QWidget):
    # Initialize the InputPanelWidget with optional parent
    def __init__(self, parent=None):
        super().__init__(parent)
        self.clear_btn = None
        self.solve_btn = None
        self.span_label = None
        self.x_max_label = None
        self.x_min_label = None
        self.span = None
        self.x_max = None
        self.x_min = None
        self.f2_input = None
        self.f2_label = None
        self.f1_input = None
        self.f1_label = None
        # Initialize components, layout, styles, and signals
        self.init_components()
        self.init_layout()
        self.apply_styles()
        self.connect_signals()

    """
    Initializes the UI components of the InputPanelWidget, including labels, input fields, and buttons.
    """
    def init_components(self):
        self.f1_label = QLabel('f1(x):')
        self.f1_input = QLineEdit()
        self.f1_input.setPlaceholderText('e.g., x^2 + 3*x - 4')

        self.f2_label = QLabel('f2(x):')
        self.f2_input = QLineEdit()
        self.f2_input.setPlaceholderText('e.g., 2*x + 1')

        self.x_min_label = QLabel('X_min:')
        self.x_min = QDoubleSpinBox()
        self.x_min.setRange(-1e6, 1e6)
        self.x_min.setValue(-10.0)
        self.x_min.setDecimals(0)

        self.x_max_label = QLabel('X_max:')
        self.x_max = QDoubleSpinBox()
        self.x_max.setRange(-1e6, 1e6)
        self.x_max.setValue(10.0)
        self.x_max.setDecimals(0)

        self.span_label = QLabel('Center Span(±):')
        self.span = QDoubleSpinBox()
        self.span.setRange(0.1, 1e6)
        self.span.setValue(5.0)
        self.span.setDecimals(0)

        self.solve_btn = QPushButton('Solve')
        self.clear_btn = QPushButton('Clear')


    """
    Organizes the UI components into a grid layout for the InputPanelWidget.
    """
    def init_layout(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.f1_label, 0, 0)
        grid.addWidget(self.f1_input, 0, 1)
        grid.addWidget(self.f2_label, 0, 2)
        grid.addWidget(self.f2_input, 0, 3)
        grid.addWidget(self.x_min_label, 1, 0)
        grid.addWidget(self.x_min, 1, 1)
        grid.addWidget(self.x_max_label, 1, 2)
        grid.addWidget(self.x_max, 1, 3)
        grid.addWidget(self.span_label, 2, 0)
        grid.addWidget(self.span, 2, 1)
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.solve_btn)
        btn_layout.addWidget(self.clear_btn)
        grid.addLayout(btn_layout, 3, 0, 1, 4)
        self.setLayout(grid)

    """
    Applies custom styles to the InputPanelWidget and its child components.
    """
    def apply_styles(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            """
            InputPanelWidget {
                background-color: #F3F3F3;
                color: #ffffff;
                max-height: 180px;
                border-top: 1px solid #cccccc;
                border-radius: 15px;
            }
            QLineEdit {
                background-color: #ffffff;
                border-radius: 8px;
                border: 1px solid #cccccc;
                height: 20px;
                min-width: 100px;
                padding: 4px;
                font-size: 15px;
            }
            QDoubleSpinBox {
                background-color: #ffffff;
                border-radius: 8px;
                border: 1px solid #cccccc;
                height: 20px;
                min-width: 100px;
                padding: 4px;
                font-size: 15px;
            }
            QAbstractSpinBox::up-button {
                width: 0px; height: 0px;
            }
            QAbstractSpinBox::down-button {
                width: 0px; height: 0px;
            }
            QLabel {
                font-weight: bold;
                font-size: 15px;
                color: #0451A5;
            }
            QPushButton {
                border-radius: 8px;
                font-weight: bold;
                font-size: 15px;
                width: 100px;
                color: #ffffff;
                padding: 6px 12px;
            }
            """
        )
        self.solve_btn.setStyleSheet("background-color: #007ACC;")
        self.solve_btn.setCursor(Qt.PointingHandCursor)
        self.solve_btn.setFixedHeight(30)
        self.clear_btn.setStyleSheet("background-color: #F44747;")
        self.clear_btn.setCursor(Qt.PointingHandCursor)
        self.clear_btn.setFixedHeight(30)

        self.f1_input.setFixedHeight(30)
        self.f2_input.setFixedHeight(30)
        self.x_min.setFixedHeight(30)
        self.x_max.setFixedHeight(30)
        self.span.setFixedHeight(30)


    """
    Connects signals to slots for the InputPanelWidget. Currently, no signals are connected.
    This method can be expanded in the future to handle button clicks or input changes.
    """
    def connect_signals(self):
        pass


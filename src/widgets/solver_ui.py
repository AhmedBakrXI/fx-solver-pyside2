import numpy as np
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QWidget, QVBoxLayout, QMessageBox

from src.fxsolver.parser import ExpressionParser
from src.fxsolver.solver import FxSolver
from src.widgets.input_widget import InputPanelWidget
from src.widgets.plotter_widget import PlotterWidget


class SolverUI(QWidget):
    def __init__(self):
        super().__init__()
        self.plotter = None
        self.layout = None
        self.input_panel = None
        self.init_ui()
        self.setup_connections()

    def init_ui(self):
        self.setWindowTitle('Solver UI')
        self.setGeometry(100, 100, 800, 600)

        self.plotter = PlotterWidget(self)
        self.input_panel = InputPanelWidget(self)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)
        self.layout.addWidget(self.plotter)
        self.layout.addWidget(self.input_panel)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            """
            SolverUI {
                background-color: #F3F3F3;
            }
            """
        )

    def setup_connections(self):
        self.input_panel.solve_btn.clicked.connect(self.on_solve)
        self.input_panel.clear_btn.clicked.connect(self.on_clear)

    def on_solve(self):
        try:
            f1_str = self.input_panel.f1_input.text()
            f2_str = self.input_panel.f2_input.text()
            x_min = self.input_panel.x_min.value()
            x_max = self.input_panel.x_max.value()
            span = self.input_panel.span.value()

            if not f1_str or not f2_str:
                raise ValueError("Both function inputs must be provided.")

            f1 = ExpressionParser.convert_expr_to_function(f1_str)
            f2 = ExpressionParser.convert_expr_to_function(f2_str)
            xr, yr = FxSolver.find_root(f1, f2, x_min, x_max)
            if not xr or not yr:
                QMessageBox.information(self, "No solution found", "No solution found")
                self.plotter.clear()
                self.plotter.plot_functions(f1, f2, f1_expr=f1_str, f2_expr=f2_str)
                return

            self.plotter.clear()
            self.plotter.plot_functions(
                f1, f2,
                f1_expr=f1_str,
                f2_expr=f2_str,
                x_center=float(xr),
                span=float(span),
                default_range=(x_min, x_max),
                annotate=(xr, yr)
            )

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def on_clear(self):
        self.input_panel.f1_input.clear()
        self.input_panel.f2_input.clear()
        self.plotter.clear()

import sys

from PySide2.QtWidgets import QApplication

from src.widgets.solver_ui import SolverUI


def main():
    app = QApplication(sys.argv)
    ui = SolverUI()
    ui.show()
    sys.exit(app.exec_())
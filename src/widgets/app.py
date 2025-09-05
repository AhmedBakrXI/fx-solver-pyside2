import sys

from PySide2.QtWidgets import QApplication

from src.widgets.solver_ui import SolverUI

"""
Entry point for the application.
Initializes the QApplication and displays the SolverUI then run the event loop.
"""
def main():
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the main window
    ui = SolverUI()
    ui.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
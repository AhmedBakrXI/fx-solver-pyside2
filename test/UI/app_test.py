from PySide2 import QtWidgets
from PySide2.QtGui import Qt

from src.widgets.solver_ui import SolverUI


def test_app_launch(qtbot):
    app = SolverUI()
    qtbot.addWidget(app)
    app.show()
    assert app.isVisible()
    assert app.windowTitle() == 'Solver UI'

def test_initial_state(qtbot):
    app = SolverUI()
    qtbot.addWidget(app)
    assert app.input_panel.f1_input.text() == ''
    assert app.input_panel.f2_input.text() == ''
    assert app.input_panel.x_min.value() == -10
    assert app.input_panel.x_max.value() == 10
    assert app.input_panel.span.value() == 5.0
    assert app.plotter.figure is not None
    assert app.plotter.ax is not None
    assert app.plotter.canvas is not None

def test_on_clear(qtbot):
    app = SolverUI()
    qtbot.addWidget(app)
    app.input_panel.f1_input.setText('x^2')
    app.input_panel.f2_input.setText('x + 2')
    app.input_panel.x_min.setValue(-5)
    app.input_panel.x_max.setValue(5)
    app.input_panel.span.setValue(3.0)
    app.on_clear()
    assert app.input_panel.f1_input.text() == ''
    assert app.input_panel.f2_input.text() == ''
    assert app.input_panel.x_min.value() == -5
    assert app.input_panel.x_max.value() == 5
    assert app.input_panel.span.value() == 3.0


def test_on_solve_valid_input(qtbot):
    app = SolverUI()
    qtbot.addWidget(app)
    app.input_panel.f1_input.setText('x^2')
    app.input_panel.f2_input.setText('x + 2')
    app.input_panel.x_min.setValue(-10)
    app.input_panel.x_max.setValue(10)
    app.input_panel.span.setValue(5.0)
    app.on_solve()
    assert len(app.plotter.ax.lines) > 0  # Check if functions are plotted
    assert any('f_1' in line.get_label() for line in app.plotter.ax.lines)

def test_on_solve_no_solution(qtbot, monkeypatch):
    app = SolverUI()
    qtbot.addWidget(app)

    # Patch QMessageBox to intercept the message
    called = {}

    def fake_info(parent, title, text, *args, **kwargs):
        called["title"] = title
        called["text"] = text
        return QtWidgets.QMessageBox.Ok

    monkeypatch.setattr(QtWidgets.QMessageBox, "information", fake_info)

    # Provide input that leads to no solution
    app.input_panel.f1_input.setText('x^2')
    app.input_panel.f2_input.setText('x^2 + 1')  # No intersection
    qtbot.mouseClick(app.input_panel.solve_btn, Qt.LeftButton)

    assert "No solution" in called["text"]


def test_on_solve_invalid_input(qtbot, monkeypatch):
    app = SolverUI()
    qtbot.addWidget(app)

    called = {}
    def fake_critical(parent, title, text, *args, **kwargs):
        called["title"] = title
        called["text"] = text
        return QtWidgets.QMessageBox.Ok

    monkeypatch.setattr(QtWidgets.QMessageBox, "critical", fake_critical)
    app.input_panel.f1_input.setText('a + 3*b')
    app.input_panel.f2_input.setText('2*x + 1')
    qtbot.mouseClick(app.input_panel.solve_btn, Qt.LeftButton)

    assert "Error" in called["title"]


def test_on_solve_empty_input(qtbot, monkeypatch):
    app = SolverUI()
    qtbot.addWidget(app)

    called = {}
    def fake_critical(parent, title, text, *args, **kwargs):
        called["title"] = title
        called["text"] = text
        return QtWidgets.QMessageBox.Ok

    monkeypatch.setattr(QtWidgets.QMessageBox, "critical", fake_critical)
    app.input_panel.f1_input.setText('')
    app.input_panel.f2_input.setText('2*x + 1')
    qtbot.mouseClick(app.input_panel.solve_btn, Qt.LeftButton)

    assert "Error" in called["title"]
    assert "Both function inputs must be provided." in called["text"]


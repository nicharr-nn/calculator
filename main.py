"""Display the calculator user interface."""
from view import Calculator_UI
from controller import Calculator

if __name__ == '__main__':
    # create the UI.  There is no controller (yet), so nothing to inject.
    calculator = Calculator()
    ui = Calculator_UI(calculator)
    ui.run()

from model import History
# from view import Calculator_UI


class Calculator:
    def __init__(self, history, ui):
        self.history = history
        self.ui = ui
        self.ui.set_cgitontroller(self)

    def update_display(self, result):
        self.ui.display_text(result)

    def calculate(self, expression):
        try:
            result = eval(expression)
            self.history.add_to_history(expression, result)
            self.update_display(result)
        except Exception as e:
            pass

    def del_function(self):
        current_text = self.ui.widget.get_display_text()
        self.ui.display_text(current_text[:-1])

    def clear_function(self):
        self.update_display("")

    def evaluate_expression(self):
        exp = self.ui.get_display_text()
        if exp:
            self.calculate(exp)
        else:
            self.ui.show_error()

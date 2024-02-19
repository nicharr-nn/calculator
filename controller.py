from model import History
# from view import Calculator_UI


class Calculator:
    def __init__(self, history=None, ui=None):
        self.history = history
        self.ui = ui
        # self.ui.set_cgitontroller(self)

    # def update_display(self, result):
    #     self.ui.display_text(result)

    def calculate(self, expression):
        try:
            result = eval(expression)
            self.history.add_to_history(expression, result)
            # self.update_display(result)
        except Exception as e:
            pass

    def del_function(self):
        current_text = self.ui.widget.get_display_text()
        self.ui.display_text(current_text[:-1])

    def evaluate_expression(self, expression: str):
        # exp = self.ui.get_display_text()
        # print(exp)
        try:
            return eval(expression)
        except Exception as e:
            return e


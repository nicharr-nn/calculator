from model import History
from math import *
# from view import Calculator_UI


class Calculator:
    def __init__(self, history=None, ui=None):
        self.history = history
        self.ui = ui

    def evaluate_expression(self, expression: str):
        try:
            result = eval(expression)
            self.save_model()
            return result
        except Exception as e:
            return e

    def save_model(self):
        pass

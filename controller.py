from model import History
from math import *


class Calculator:
    def __init__(self):
        self.model = History()

    def evaluate_expression(self, expression: str):
        try:
            result = eval(expression)
            self.model.add_to_history(expression, result)
            return result
        except Exception as e:
            return e

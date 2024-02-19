"""It's a controller module that contains the Calculator class,
which evaluates the expression and adds the result to the history."""
from math import *
from model import History


class Calculator:
    """Evaluating the expression and adding the result to the history."""
    def __init__(self):
        """Create a new instance of the History class."""
        self.model = History()

    def evaluate_expression(self, expression: str):
        """Calculate and return the result of the expression.
        Also add the expression and result to the history."""
        try:
            result = eval(expression)
            self.model.add_to_history(expression, result)
            return result
        except Exception as e:
            return e

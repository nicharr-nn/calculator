""" Stores the history of the calculator """


class History:
    """Stores the history of the calculator."""
    def __init__(self):
        """Create a new instance of the History class."""
        self.history = []

    def get_history(self):
        """Return the history of the calculator."""
        return self.history

    def add_to_history(self, expression, result):
        """Add an expression and result to the history."""
        self.history.append((expression, result))

""" Stores the history of the calculator """


class History:
    def __init__(self, history):
        self.history = history

    def get_history(self):
        return self.history

    def add_to_history(self, expression, result):
        self.history.append((expression, result))

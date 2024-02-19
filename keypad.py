"""keypad widget."""
import tkinter as tk
from tkinter import ttk


class Keypad(tk.Frame):
    """A keypad widget for a calculator."""
    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        # keynames and columns
        super().__init__(parent, **kwargs)
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        for i, keyname in enumerate(self.keynames):
            row, col = divmod(i, columns)
            btn = ttk.Button(self, text=keyname)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="news")
        for i in range(columns):
            self.grid_columnconfigure(i, weight=1)
        for i in range(len(self.keynames) // columns):
            self.grid_rowconfigure(i, weight=1)

    def bind(self, sequence, func, **kwargs):
        """Bind an event handler to an event sequence.
        :param **kwargs:
        """
        # as the bind method of Tkinter widgets.
        # Use the parameters to bind all the buttons in the keypad
        # to the same event handler.
        for i in self.winfo_children():
            i.bind(sequence, func, **kwargs)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for i in self.winfo_children():
            i[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        return self.winfo_children()[0][key]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        self.config(cnf, **kwargs)

    # the the superclass object for this keypad.
    # This is so that a programmer can set properties of a keypad's frame,
    # e.g. keypad.frame.configure(background='blue')
    @property
    def frame(self):
        return super()


if __name__ == '__main__':
    keys = list('789456123 0.')  # = ['7','8','9',...]

    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = Keypad(root, keynames=keys, columns=3)
    keypad.pack(expand=True, fill=tk.BOTH)
    root.mainloop()

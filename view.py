"""It's view module that contains the Calculator_UI class, which displays the calculator user interface."""
import tkinter as tk
from tkinter import ttk
from keypad import Keypad
from controller import Calculator


class Calculator_UI:
    """Display the calculator user interface."""
    def __init__(self, controller: Calculator()):
        """Create a new instance of the Calculator_UI class."""
        self.tk = tk.Tk()
        self.tk.title("Calculator")
        self.tk.geometry("700x600")
        self.tk.resizable(True, True)
        self.text_result = tk.StringVar()
        self.history_var = tk.StringVar()
        self.combo_value = tk.StringVar()
        self.controller = controller
        self.stack = []

        self.operator_list = ['*', '/', '+', '-', '^', '(', ')', '=']
        self.operator_list2 = ['mod', 'DEL', 'CLR']
        self.adv_operator_list = ['exp', 'ln', 'log2', 'log10', 'sqrt']
        self.replace_list = ['^', 'mod', 'ln']

        self.init_components()

    def init_components(self):
        """Create the calculator interface."""
        frame = ttk.Frame(self.tk)
        frame.pack(expand=True, fill=tk.BOTH)
        self.display_label = ttk.Label(frame, textvariable=self.text_result, anchor="e", font=('Arial', 14))
        self.display_label.grid(row=1, column=0, columnspan=5, padx=10, pady=5, sticky="news")

        self.history = ttk.Label(frame, textvariable=self.history_var, anchor="e", font=('Arial', 14))
        self.history.grid(row=0, column=3, columnspan=2, padx=10, pady=5, sticky="news")

        self.history_list_q = []
        self.history_cbb_q = ttk.Combobox(frame, values=self.history_list_q, state='readonly')
        self.history_cbb_q.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="news")
        self.history_cbb_q.bind('<<ComboboxSelected>>', self.select_history)

        self.history_list_a = []
        self.history_cbb_a = ttk.Combobox(frame, values=self.history_list_a, state='readonly')
        self.history_cbb_a.grid(row=0, column=2, columnspan=1, padx=10, pady=5, sticky="news")
        self.history_cbb_a.bind('<<ComboboxSelected>>', self.select_history)

        adv_opt = ttk.Combobox(frame, values=self.adv_operator_list, textvariable=self.combo_value)
        adv_opt.grid(row=2, column=3, padx=5, pady=5, sticky="news", columnspan=4)
        adv_opt.current(0)
        adv_opt.bind('<<ComboboxSelected>>', self.cbb_text)

        keypad = Keypad(frame, keynames=['7', '8', '9', '4', '5', '6', '1', '2', '3', ' ', '0', '.'], columns=3)
        keypad.grid(row=3, column=0, sticky="news", columnspan=3)
        keypad.bind('<Button>', self.observer)
        # keypad.config(background='blue')

        op = Keypad(frame, keynames=self.operator_list)
        op.grid(row=3, column=3, sticky="news", columnspan=1)
        op.bind('<Button>', self.observer)

        op2 = Keypad(frame, keynames=self.operator_list2, columns=3)
        op2.grid(row=2, column=0, sticky="news", columnspan=3)
        op2.bind('<Button>', self.observer)

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        for i in range(1, 4):
            frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)

    def display_text(self, event):
        """Display the text on the calculator."""
        self.display_label.config(foreground='black')
        key_pressed = event.widget.cget('text')
        if key_pressed == 'DEL':
            current_text = self.text_result.get()
            self.text_result.set(current_text[:-1])
        elif key_pressed == 'CLR':
            self.text_result.set("")
        elif key_pressed == '=':
            txt = self.text_result.get()
            for operator in self.replace_list:
                if operator in txt:
                    if operator == '^':
                        txt = txt.replace(operator, '**')
                    elif operator == 'ln':
                        txt = txt.replace(operator, 'log')
                    elif operator == 'mod':
                        txt = txt.replace(operator, '%')
            result = self.controller.evaluate_expression(expression=txt)
            if isinstance(result, SyntaxError):
                self.display_label.config(foreground='red')
                tk.Tk.bell(self.tk)
            else:
                self.controller.model.add_to_history(txt, result)
                history = self.controller.model.get_history()[-1]
                self.history_list_q.append(history[0])
                self.history_cbb_q.config(values=self.history_list_q, textvariable=self.history_list_q[-1])
                self.history_cbb_q.current(len(self.history_list_q) - 1)
                self.history_list_a.append(history[1])
                self.history_cbb_a.config(values=self.history_list_a, textvariable=self.history_list_a[-1])
                self.history_cbb_a.current(len(self.history_list_a) - 1)
                self.history_var.set(f"{history[0]} = {history[1]}")
                self.text_result.set(result)
        else:
            self.text_result.set(self.text_result.get() + event.widget.cget('text'))

    def get_display_text(self):
        """Return the text displayed on the calculator."""
        return self.text_result.get()

    def observer(self, event):
        """Handle the event when a button is clicked."""
        self.display_text(event)

    def cbb_text(self, event):
        """Add the advanced operator to the expression."""
        if self.text_result.get() == "":
            self.text_result.set(self.combo_value.get() + '(')
        else:
            if self.text_result.get()[-1:] in self.operator_list:
                self.text_result.set(self.text_result.get() + self.combo_value.get() + '(')
            else:
                self.text_result.set(self.combo_value.get() + '(' + self.text_result.get() + ')')

    def select_history(self, event):
        """Select the history from the combobox."""
        self.text_result.set(event.widget.get())

    def run(self):
        """Display the calculator user interface."""
        self.tk.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from keypad import Keypad
from controller import Calculator


class Calculator_UI:
    def __init__(self):
        self.tk = tk.Tk()
        self.tk.title("Calculator")
        self.text_result = tk.StringVar()
        self.tk.geometry("450x450")
        self.tk.resizable(True, True)
        self.init_components()
        self.controller = None

    def init_components(self):
        frame = ttk.Frame(self.tk)
        frame.pack(expand=True, fill=tk.BOTH)
        self.display_label = ttk.Label(frame, textvariable=self.text_result, anchor="e", font=('Arial', 14))
        self.display_label.grid(row=0, column=0, columnspan=5, padx=10, pady=5, sticky="news")

        # adv_opt = Keypad(frame, keynames=['exp', 'ln', 'log2', 'log10', 'sqrt', 'mod', 'DEL', 'CLR'])
        # adv_opt.grid(row=1, column=4, sticky="news")
        # adv_opt.bind('<Button>', self.observer)
        adv_opt = ttk.Combobox(frame, values=['exp', 'ln', 'log2', 'log10', 'sqrt'])
        adv_opt.grid(row=1, column=0, padx=5, pady=5, sticky="news", columnspan=4)
        adv_opt.bind('<<ComboboxSelected>>', self.observer)

        keypad = Keypad(frame, keynames=['7', '8', '9', '4', '5', '6', '1', '2', '3', ' ', '0', '.'], columns=3)
        keypad.grid(row=2, column=0, sticky="news", columnspan=3)
        keypad.bind('<Button>', self.observer)

        op = Keypad(frame, keynames=['*', '/', '+', '-', '^', '=', '(', ')', 'DEL', 'CLR'])
        op.grid(row=2, column=3, sticky="news", columnspan=1)
        op.bind('<Button>', self.observer)

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        for i in range(1, 4):
            frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)

    def display_text(self, event):
        key_pressed = event.widget.cget('text')
        if key_pressed == 'DEL':
            self.controller.del_function()
        elif key_pressed == 'CLR':
            self.controller.clear_function()
        elif key_pressed == '=':
            self.controller.evaluate_expression()
        else:
            self.text_result.set(self.text_result.get() + event.widget.cget('text'))

    def get_display_text(self):
        return self.text_result.get()

    def observer(self, event):
        self.display_text(event)

    def error_msg(self):
        messagebox.showerror("Error", "Invalid expression")

    def history(self):
        pass

    def run(self):
        self.tk.mainloop()


# if __name__ == '__main__':
#     ui = Calculator_UI()
#     ui.run()

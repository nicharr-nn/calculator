import tkinter as tk
from tkinter import ttk, messagebox
from keypad import Keypad
from controller import Calculator


class Calculator_UI:
    def __init__(self, controller: Calculator()):
        self.tk = tk.Tk()
        self.tk.title("Calculator")
        self.tk.geometry("700x600")
        self.tk.resizable(True, True)
        self.text_result = tk.StringVar()
        self.combo_value = tk.StringVar()
        self.controller = controller
        self.stack = []

        self.operator_list = ['*', '/', '+', '-', '^', '=', '(', ')', 'DEL', 'CLR']
        self.adv_operator_list = ['exp', 'ln', 'log2', 'log10', 'sqrt']
        self.replace_list = self.adv_operator_list + ['^']

        self.init_components()

    def init_components(self):
        frame = ttk.Frame(self.tk)
        frame.pack(expand=True, fill=tk.BOTH)
        self.display_label = ttk.Label(frame, textvariable=self.text_result, anchor="e", font=('Arial', 14))
        self.display_label.grid(row=0, column=0, columnspan=5, padx=10, pady=5, sticky="news")


        adv_opt = ttk.Combobox(frame, values=self.adv_operator_list, textvariable=self.combo_value)
        adv_opt.grid(row=1, column=0, padx=5, pady=5, sticky="news", columnspan=4)
        adv_opt.current(0)
        adv_opt.bind('<<ComboboxSelected>>', self.cbb_text)

        keypad = Keypad(frame, keynames=['7', '8', '9', '4', '5', '6', '1', '2', '3', ' ', '0', '.'], columns=3)
        keypad.grid(row=2, column=0, sticky="news", columnspan=3)
        keypad.bind('<Button>', self.observer)

        op = Keypad(frame, keynames=self.operator_list)
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
        # print('key', self.text_result.get())
        if key_pressed == 'DEL':
            current_text = self.text_result.get()
            self.text_result.set(current_text[:-1])
        elif key_pressed == 'CLR':
            self.text_result.set("")
        elif key_pressed == '=':
            txt = self.text_result.get()
            print(self.replace_list)
            # Mark for loop useing slicing with index
            for i in self.replace_list:
                if i in txt:
                    if i == '^':
                        txt = txt.replace(i, '**')
                    elif i == 'ln':
                        txt = txt.replace(i, 'math.' + i)
                    else:
                        txt = txt.replace(i, 'math.' + i)
            print(txt)
            result = self.controller.evaluate_expression(expression=txt)
            if isinstance(result, SyntaxError):
                self.error_msg(result)
            else:
                self.text_result.set(result)
        else:
            self.text_result.set(self.text_result.get() + event.widget.cget('text'))
            print(self.text_result.get())

    def get_display_text(self):
        return self.text_result.get()

    def observer(self, event):
        operator = self.combo_value.get()
        self.display_text(event)

    def cbb_text(self, event):
        operator = self.combo_value.get()
        print('op', operator)
        if self.text_result.get() == "":
            self.text_result.set(self.combo_value.get() + '(')
        else:
            if self.text_result.get()[-1:] in self.operator_list:
                self.text_result.set(self.text_result.get() + self.combo_value.get() + '(')
            else:
                self.text_result.set(self.combo_value.get() + '(' + self.text_result.get() + ')')

    def error_msg(self, result):
        tk.messagebox.showerror("Error Message", result)

    def history(self):
        pass

    def run(self):
        self.tk.mainloop()


# if __name__ == '__main__':
#     ui = Calculator_UI()
#     ui.run()
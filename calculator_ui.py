import tkinter as tk
from tkinter import ttk
from keypad import Keypad

class Calculator_UI:
    def __init__(self):
        self.tk = tk.Tk()
        self.tk.title("Calculator")
        self.text_result = tk.StringVar()
        self.tk.geometry("450x300")
        self.tk.resizable(True, True)
        self.init_components()

    def init_components(self):
        frame = ttk.Frame(self.tk)
        frame.pack(expand=True, fill=tk.BOTH)
        self.display_label = ttk.Label(frame, textvariable=self.text_result, anchor="e", font=('Arial', 14))
        self.display_label.grid(row=0, column=0, columnspan=5, padx=10, pady=5, sticky="news")

        adv_opt = Keypad(frame, keynames=['exp', 'ln', 'log2', 'log10', 'sqrt', 'mod', ')'])
        adv_opt.grid(row=1, column=4, sticky="news")
        adv_opt.bind('<Button>', self.observer)

        keypad = Keypad(frame, keynames=['7', '8', '9', '4', '5', '6', '1', '2', '3', ' ', '0', '.'], columns=3)
        keypad.grid(row=1, column=0, sticky="news", columnspan=3)
        keypad.bind('<Button>', self.observer)

        op = Keypad(frame, keynames=['*', '/', '+', '-', '^', '=', '('])
        op.grid(row=1, column=3, sticky="news", columnspan=1)
        op.bind('<Button>', self.observer)

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        for i in range(1, 4):
            frame.grid_rowconfigure(i, weight=1)
        for i in range(5):
            frame.grid_columnconfigure(i, weight=1)

        keypad.frame.configure(background='blue')
        op.frame.configure(background='blue')

    def display_text(self, event):
        self.text_result.set(self.text_result.get() + event.widget.cget('text'))

    def observer(self, event):
        self.display_text(event)

    def press_btn(self, event):
        pressed = event.widget.cget('text')
        current_text = self.text_result.get()
        if pressed == 'DEL':
            pass

    def run(self):
        self.tk.mainloop()


if __name__ == '__main__':
    ui = Calculator_UI()
    ui.run()

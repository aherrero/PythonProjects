#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk

class MainApplication:
    def __init__(self, root):
        self.root = root

        content = ttk.Frame(root, padding=(3,3,12,12))

        labelTitle = ttk.Label(content, text="Tester application for the product Linear Actuator", font=("Arial Bold", 16))

        btn1 = ttk.Button(content, text="Start", command=self.greet)
        btn2 = ttk.Button(content, text="Close", command=root.quit)

        content.grid(column=0, row=0, sticky=(N, S, E, W))

        labelTitle.grid(column=0, row=1, columnspan=1, sticky=(N, W), padx=5, pady=5)
        btn1.grid(column=0, row=3, columnspan=1)
        btn2.grid(column=1, row=3, columnspan=1)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)
        # content.rowconfigure(1, weight=1)

    def greet(self):
        print("Greetings!")

def main():
    root = Tk()
    root.geometry('800x600')
    root.title("A simple GUI")
    my_gui = MainApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()

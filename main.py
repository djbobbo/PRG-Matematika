#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random

# from tkinter import ttk

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "matematikovací věda"

    def __init__(self):
        super().__init__(className=self.name)
        self.lbl = tk.Label(self, text="matematikovací věda")
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl.grid(row=0)
        self.lblGr = tk.Label(self, text="")
        self.lblGr.grid(row=3, column=2)
        self.generovani()
        self.entry = tk.Entry(self, width=5)
        self.entry.grid(row=2, column=3)
        self.bind('<Return>', self.kontrola)
        self.but = tk.Button(self, text="Konec", command=self.quit)
        self.but.grid(row=3, column=3)

    def kontrola(self, event):
        try:
            if int(self.entry.get()) == self.vysledek:
                self.lblGr.config(text="SPRÁVNĚ", fg="green")

            else:
                self.lblGr.config(text="ŠPATNĚ",fg="red")

            self.generovani()
            self.entry.delete(0, tk.END)
        except ValueError:
            return


    def plus(self):
        self.cisloA = random.randint(1, 100)
        self.cisloB = random.randint(1, 100 - self.cisloA)
        self.vysledek = self.cisloA + self.cisloB
        self.lbl.config(text=f'{self.cisloA} + {self.cisloB} = ')

        return self.lbl.config(text=f'{self.cisloA} + {self.cisloB} = ')

    def minus(self):
        self.cisloA = random.randint(1, 100)
        self.cisloB = random.randint(1, self.cisloA)
        self.vysledek = self.cisloA - self.cisloB
        self.lbl.config(text=f'{self.cisloA} - {self.cisloB} = ')

        return self.lbl.config(text=f'{self.cisloA} - {self.cisloB} = ')

    def krat(self):
        self.cisloA = random.randint(1, 9)
        self.cisloB = random.randint(1, 9)
        self.vysledek = self.cisloA * self.cisloB
        self.lbl.config(text=f'{self.cisloA} * {self.cisloB} = ')

        return self.lbl.config(text=f'{self.cisloA} * {self.cisloB} = ')

    def deleno(self):
        self.vysledek = random.randint(1, 9)
        self.cisloB = random.randint(1, 9)
        self.cisloA = self.vysledek * self.cisloB
        self.lbl.config(text=f'{self.cisloA} / {self.cisloB} = ')

        return self.lbl.config(text=f'{self.cisloA} / {self.cisloB} = ')

    def generovani(self):
        priklad = random.choice([self.plus, self.minus, self.krat, self.deleno])
        priklad()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()

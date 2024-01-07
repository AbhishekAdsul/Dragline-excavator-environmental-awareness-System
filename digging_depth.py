from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime

from tkinter import Tk, Label, Entry, Button, messagebox

class digging_depth:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300+10+250")
        self.root.title("Digging Depth Calculator")

        self.label_length = Label(root, text="Enter Length:")
        self.label_length.pack()
        self.entry_length = Entry(root)
        self.entry_length.pack()

        self.label_breadth = Label(root, text="Enter Breadth:")
        self.label_breadth.pack()
        self.entry_breadth = Entry(root)
        self.entry_breadth.pack()

        self.label_height = Label(root, text="Enter Height:")
        self.label_height.pack()
        self.entry_height = Entry(root)
        self.entry_height.pack()

        self.label_dump_area = Label(root, text="Enter Dump Area:")
        self.label_dump_area.pack()
        self.entry_dump_area = Entry(root)
        self.entry_dump_area.pack()

        self.label_swell_factor = Label(root, text="Enter Swell Factor:")
        self.label_swell_factor.pack()
        self.entry_swell_factor = Entry(root)
        self.entry_swell_factor.pack()

        self.calculate_button = Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = Label(root, text="")
        self.result_label.pack()

    def calculate(self):
        try:
            a = float(self.entry_length.get())
            b = float(self.entry_breadth.get())
            h = float(self.entry_height.get())
            A1 = (((a + b) / 2) * h)

            A2 = float(self.entry_dump_area.get())
            s = float(self.entry_swell_factor.get())
            A3 = (A1 * s - A2)

            if A3 < 0:
                h = (2 * A2) / (s * (a + b))
                self.result_label.config(text=f"The height is now: {h}\nNo rehandling is required")
            elif A3 == 0:
                self.result_label.config(text="No rehandling required")
            else:
                self.result_label.config(text=f"The height is now: {h}\nThe extra area is: {A3}\nThe reach has to be increased")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values.")

if __name__ == "__main__":
    root = Tk()
    obj = digging_depth(root)
    root.mainloop()

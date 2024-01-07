from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import os
from time import strftime
from datetime import datetime

class cost_calculation:
    def __init__(self, root):
        self.root = root
        self.root.geometry("350x400+10+250")
        self.root.title("Koyala Yantri")
        
        self.create_widgets()

    def create_widgets(self):
        input_labels = ['Cost of Dragline (in million Rs.):', 'Number of Years:', 'Power Consumption (in KWh):', 'Bucket Capacity (cu.m):',
                        'Cycle Time (s):', 'Availability:', 'Utilization:', 'Stripping Ratio:', 'Rehandling (Decimals):',
                        'Method (s):']

        self.entries = []
        for i, label_text in enumerate(input_labels):
            label = Label(self.root, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
            entry = Entry(self.root)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries.append(entry)

        cost_entry, years_entry, power_entry, bucket_entry, cycle_entry, availability_entry, utilization_entry, stripping_entry, rehandling_entry, method_entry = self.entries

        calculate_button = Button(self.root, text="Calculate", command=self.calculate)
        calculate_button.grid(row=len(input_labels), columnspan=2, padx=10, pady=10)

        self.output_label = Label(self.root, text="")
        self.output_label.grid(row=len(input_labels) + 1, columnspan=2, padx=10, pady=5)

    def annualproduction(self, b, ct, a, ut):
        pa = (b / ct) * a * ut * 0.719 * 0.733 * 0.8 * 8 * 3 * 365 * 60 * 60 / 1000000
        self.output_label.config(text=f'The annual production of the dragline is: {pa:.2f} M cu.m')

    def ownershipcost(self, c, n):
        d = 0.04 * c
        aai = ((n + 1) / (2 * n)) * c
        ai = (15.00 / 100) * aai
        oc = d + ai
        return oc

    def operatingcost(self, p, c):
        d = 0.04 * c
        mc = (0.20 * 6.00) + (0.14 * 3.00)
        ap = 4.89 * p * 1000000
        al = 0.30 * ap
        am = (0.20 * d) + (0.02 * c)
        op = mc + ap + al + am
        return op

    def totalcost(self, pa, oc, op):
        ta = oc + op
        self.output_label.config(text=f'The total costs of dragline/year = Rs. {ta:.2f} ')

    def calculate(self):
        c = float(self.entries[0].get()) * 1000000  # Convert million to actual currency
        n = int(self.entries[1].get())
        p = float(self.entries[2].get())
        b = float(self.entries[3].get())
        ct = float(self.entries[4].get())
        a = float(self.entries[5].get())
        ut = float(self.entries[6].get())
        s = float(self.entries[7].get())
        r = float(self.entries[8].get())
        t = self.entries[9].get()

        if t == 's':
            self.annualproduction(b, ct, a, ut)
            oc = self.ownershipcost(c, n)
            op = self.operatingcost(p, c)
            self.totalcost(None, oc, op)  # pa value is not used for total cost calculation in this case
        elif t == 'e':
            # Update accordingly if needed
            pass

if __name__ == "__main__":
    root = Tk()
    obj = cost_calculation(root)
    root.mainloop()

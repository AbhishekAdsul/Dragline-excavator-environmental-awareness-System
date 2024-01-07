import tkinter as tk

def annualproduction(b, ct, a, ut):
    pa = (b / ct) * a * ut * 0.719 * 0.733 * 0.8 * 8 * 3 * 365 * 60 * 60
    output_label.config(text=f'The annual production of the dragline is: {pa:.2f}')

def ownershipcost(c, n):
    d = 0.04 * c
    aai = ((n + 1) / (2 * n)) * c
    ai = (15.00 / 100) * aai
    oc = d + ai
    output_label.config(text=f'The ownership cost of the dragline is: {oc:.2f}')

def operatingcost(p, c):
    d = 0.04 * c
    mc = (0.20 * 6.00) + (0.14 * 3.00)
    ap = 4.89 * p * 1000000
    al = 0.30 * ap
    am = (0.20 * d) + (0.02 * c)
    op = mc + ap + al + am
    output_label.config(text=f'The operating cost of the dragline is: {op:.2f}')

# Define other calculation functions (totalcost, overburdencost, coalexposure1, coalexposure2) similarly

def calculate():
    c = float(cost_entry.get())
    n = int(years_entry.get())
    p = float(power_entry.get())
    b = float(bucket_entry.get())
    ct = float(cycle_entry.get())
    a = float(availability_entry.get())
    ut = float(utilization_entry.get())
    s = float(stripping_entry.get())
    r = float(rehandling_entry.get())
    t = method_entry.get()

    if t == 's':
        annualproduction(b, ct, a, ut)
        ownershipcost(c, n)
        operatingcost(p, c)
        # Call other calculation functions with respective arguments
    elif t == 'e':
        annualproduction(b, ct, a, ut)
        ownershipcost(c, n)
        operatingcost(p, c)
        # Call other calculation functions with respective arguments

root = tk.Tk()
root.title("Dragline Cost Calculator")

input_labels = ['Cost of Dragline:', 'Number of Years:', 'Power Consumption:', 'Bucket Capacity:',
                'Cycle Time:', 'Availability:', 'Utilization:', 'Stripping Ratio:', 'Rehandling (Decimals):',
                'Method (s/e):']

for i, label_text in enumerate(input_labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    if i == 9:
        method_entry = entry
    elif i == 0:
        cost_entry = entry
    elif i == 1:
        years_entry = entry
    elif i == 2:
        power_entry = entry
    elif i == 3:
        bucket_entry = entry
    elif i == 4:
        cycle_entry = entry
    elif i == 5:
        availability_entry = entry
    elif i == 6:
        utilization_entry = entry
    elif i == 7:
        stripping_entry = entry
    elif i == 8:
        rehandling_entry = entry

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=len(input_labels), columnspan=2, padx=10, pady=10)

output_label = tk.Label(root, text="")
output_label.grid(row=len(input_labels) + 1, columnspan=2, padx=10, pady=5)

root.mainloop()

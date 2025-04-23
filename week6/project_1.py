import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simi Services Delivery")

# Labels and instructions
tk.Label(root, text="Welcome to Simi Services!").pack(pady=5)
tk.Label(root, text="Here are the locations we deliver to:").pack()
tk.Label(root, text="0. Ibeju-lekki Community\n1. Epe").pack(pady=5)
tk.Label(root, text="Enter 0 or 1 to select your location:").pack()

location_entry = tk.Entry(root)
location_entry.pack()

tk.Label(root, text="What is the weight of your package?").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

def on_click():
    my_location = location_entry.get()
    weight_of_package = weight_entry.get()

    if my_location.isdigit() and weight_of_package.isdigit():
        my_location = int(my_location)
        weight_of_package = int(weight_of_package)

        if my_location in [0, 1]:
            if my_location == 0:
                if weight_of_package >= 10:
                    charge = 5000
                    messagebox.showinfo("Charge", f"You are to pay {charge} Naira for the delivery of this package.")
                elif weight_of_package <= 10:
                    charge = 3500
                    messagebox.showinfo("Charge", f"You are to pay {charge} Naira for this package.")
            if my_location == 1:
                if weight_of_package >= 10:
                    charge = 10000
                    messagebox.showinfo("Charge", f"You are to pay {charge} Naira for your delivery.")
                elif weight_of_package <= 10:
                    charge = 5000
                    messagebox.showinfo("Charge", f"You are to pay {charge} Naira for your delivery.")
        else:
            messagebox.showerror("Error", "We don't deliver to this location, sorry.")
    else:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Button
tk.Button(root, text="Submit", command=on_click).pack(pady=10)

root.mainloop()
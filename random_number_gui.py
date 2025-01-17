import tkinter as tk
from tkinter import messagebox
import random

# Function to generate random number
def generate_random():
    try:
        bottom = int(entry_bottom.get())
        top = int(entry_top.get())
        if bottom > top:
            messagebox.showerror("Input Error", "Bottom number must be less than or equal to the top number.")
        else:
            random_number = random.randint(bottom, top)
            result_label.config(text=f"Random Number: {random_number}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers.")

# Create the main window
root = tk.Tk()
root.title("Random Number Generator")

# Create and place labels and text boxes
label_bottom = tk.Label(root, text="Bottom Number:")
label_bottom.grid(row=0, column=0, padx=10, pady=10)
entry_bottom = tk.Entry(root)
entry_bottom.grid(row=0, column=1, padx=10, pady=10)

label_top = tk.Label(root, text="Top Number:")
label_top.grid(row=1, column=0, padx=10, pady=10)
entry_top = tk.Entry(root)
entry_top.grid(row=1, column=1, padx=10, pady=10)

# Create and place the generate button
generate_button = tk.Button(root, text="Generate", command=generate_random)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create and place the result label
result_label = tk.Label(root, text="Random Number: ", font=("Arial", 14))
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()

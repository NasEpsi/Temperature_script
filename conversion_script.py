# Importing the necessary modules from the Tkinter library
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Creating the main window
fenetre = tk.Tk()
fenetre.title("Temperature Converter")  # Setting the title of the window

# Configuring columns for widget placement
fenetre.columnconfigure(0, weight=1)
fenetre.columnconfigure(1, weight=3)

# Creating a label for entering the temperature in Fahrenheit
label = ttk.Label(fenetre, text="Enter the temperature in Fahrenheit:")
label.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

# Creating an entry widget for entering the temperature in Fahrenheit
entry = ttk.Entry(fenetre)
entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# Function to perform the temperature conversion and display the result
def convert():
    temperature = entry.get()
    calculation = (float(temperature) - 32) * 5 / 9
    result = f"Here is the conversion in degrees Celsius: {calculation} °C"
    messagebox.showinfo("Temperature in Celsius", result)

# Creating a button that triggers the conversion function when clicked
button = ttk.Button(fenetre, text="Convert", command=convert)
button.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# Starting the Tkinter main loop to display the window
fenetre.mainloop()
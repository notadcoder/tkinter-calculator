import tkinter as tk


def add():
    """Add the two input numbers"""
    result = float(num1_entry.get()) + float(num2_entry.get())
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, str(result))
    result_entry.config(state="readonly")


def subtract():
    """Subtract the second input number from the first"""
    result = float(num1_entry.get()) - float(num2_entry.get())
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, str(result))
    result_entry.config(state="readonly")


def multiply():
    """Multiply the two input numbers"""
    result = float(num1_entry.get()) * float(num2_entry.get())
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, str(result))
    result_entry.config(state="readonly")


def divide():
    """Divide the first input number by the second"""
    result = float(num1_entry.get()) / float(num2_entry.get())
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, str(result))
    result_entry.config(state="readonly")


# Create the GUI window
window = tk.Tk()
window.title("Simple Calculator")

# Create the input fields and labels
num1_label = tk.Label(window, text="Enter first number:")
num1_label.pack()
num1_entry = tk.Entry(window)
num1_entry.pack()
num2_label = tk.Label(window, text="Enter second number:")
num2_label.pack()
num2_entry = tk.Entry(window)
num2_entry.pack()
result_label = tk.Label(window, text="Result:")
result_label.pack()
result_entry = tk.Entry(window, state="readonly")
result_entry.pack()

# Create the buttons
add_button = tk.Button(window, text="+", command=add)
add_button.pack()
subtract_button = tk.Button(window, text="-", command=subtract)
subtract_button.pack()
multiply_button = tk.Button(window, text="*", command=multiply)
multiply_button.pack()
divide_button = tk.Button(window, text="/", command=divide)
divide_button.pack()

# Run the GUI loop
window.mainloop()

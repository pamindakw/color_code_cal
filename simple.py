import tkinter as tk

def sum_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create the main window
window = tk.Tk()
window.title("Sum Two Numbers")

# Create and place the input boxes
entry1 = tk.Entry(window)
entry1.pack(pady=5)

entry2 = tk.Entry(window)
entry2.pack(pady=5)

# Create and place the button
sum_button = tk.Button(window, text="Sum", command=sum_numbers)
sum_button.pack(pady=5)

# Create and place the result label
result_label = tk.Label(window, text="Result: ")
result_label.pack(pady=5)

# Start the GUI event loop
window.mainloop()
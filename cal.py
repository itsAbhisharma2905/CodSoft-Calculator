import tkinter as tk

# Function to update the input field when buttons are pressed
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the input field
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def button_equal():
    try:
        result = eval(entry.get())  # Evaluate the mathematical expression
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

# Create an entry widget to display the calculations
entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=20)

# Create buttons
button_list = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in button_list:
    if text == '=':
        tk.Button(root, text=text, padx=40, pady=20, font=('Arial', 18),
                  command=button_equal).grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(root, text=text, padx=40, pady=20, font=('Arial', 18),
                  command=lambda txt=text: button_click(txt)).grid(row=row, column=col, sticky="nsew")

# Clear button
tk.Button(root, text="C", padx=40, pady=20, font=('Arial', 18), command=button_clear).grid(row=5, column=0, columnspan=4, sticky="nsew")

# Configure grid layout for even button distribution
for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i - 1, weight=1)

# Run the application
root.mainloop()

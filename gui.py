# Beatrice Akinpelu
# 11/24/2024


from tkinter import *

root = Tk()
root.title("Simple Calculator")  

# Creating an entry widget for user input
e = Entry(root, width=35, borderwidth=5)  # Entry box with specified width and border
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)  # Positioning the entry widget in the grid layout

# Function to handle button clicks for numbers
def button_click(number):
    """
    Appends the clicked number to the current value in the entry box.
    Args:
        number: The number associated with the clicked button.
    """
    current = e.get()  # Get the current value in the entry box
    e.delete(0, END)  # Clear the entry box
    e.insert(0, str(current) + str(number))  # Insert the new value

# Function to clear the entry box
def button_clear():
    """Clears all content in the entry box."""
    e.delete(0, END)

# Function to handle operators (+, -, *, /)
def button_operator(operator):
    """
    Stores the first number and the operator for calculation.
    Args:
        operator: The operator (+, -, *, /) associated with the clicked button.
    """
    first_number = e.get()  # Get the first number from the entry box
    global f_num  # Declare a global variable to store the first number
    global num_operator  # Declare a global variable to store the operator
    f_num = int(first_number)  # Convert the first number to an integer
    num_operator = operator  # Store the selected operator
    e.delete(0, END)  # Clear the entry box for the next input

# Function to handle the "=" button and perform calculations
def button_equal():
    """
    Performs the operation based on the stored operator and the second number.
    Displays the result in the entry box.
    """
    second_number = e.get()  # Get the second number from the entry box
    e.delete(0, END)  # Clear the entry box
    # Perform the calculation based on the operator
    if num_operator == '+':
        e.insert(0, f_num + int(second_number))
    elif num_operator == '-':
        e.insert(0, f_num - int(second_number))
    elif num_operator == '*':
        e.insert(0, f_num * int(second_number))
    elif num_operator == '/':
        e.insert(0, f_num / int(second_number))
    else:
        e.insert(0, "Invalid!!!")  # Handle invalid operators

# Creating buttons for numbers, operations, and functions
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_operator("+"))
button_equal = Button(root, text="=", padx=79, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))

# Placing the buttons on the GUI using grid layout
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# Start the main loop to display the GUI and handle events
root.mainloop()

import tkinter as tk

def x_box(text):
	g = ""
	window = tk.Tk()
	window.title("Configurações")
	window.geometry("300x200")
	
	
	my_int_var = tk.IntVar(window, value=100)
	
	x_1 = tk.Entry(window, borderwidth = 5, width = 15, textvariable=my_int_var)
	x_1.pack()
	window.mainloop()
	
	
	
	return g

x_box("aloha")

# print(x_1)

"""
import tkinter as tk
root = tk.Tk()

# Create a StringVar
user_input_var_x = tk.IntVar()
user_input_var_y = tk.IntVar()

# Link it to an Entry widget using the 'textvariable' option
entry_widget = tk.Entry(root, textvariable=user_input_var_x)
entry_widget.pack()

# The value of user_input_var can be accessed later with .get()
# e.g., when a button is clicked
def on_button_click():
    print(f"User entered: {user_input_var_x.get()}") # Use .get() to retrieve the value

button = tk.Button(root, text="Get Value", command=on_button_click)
button.pack()

root.mainloop()
"""

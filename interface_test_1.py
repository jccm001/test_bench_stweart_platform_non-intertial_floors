import tkinter as tk

def x_box(text):
	g = ""
	window = tk.Tk()
	window.title("Configurações")
	window.geometry("300x200")
	
	x_0 = tk.Label(window, text = float)
	x_0.pack()
	
	x_1 = tk.Entry(window, borderwidth = 5, width = 15)
	x_1.pack()
	window.mainloop()
	return g

x_0 = x_box("f")

print(x_0)
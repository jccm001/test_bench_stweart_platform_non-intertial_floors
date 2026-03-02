import tkinter as tk




def on_button_click():
    print(f"User entered amplitude: {entry_widget_x_amp.get()}")
    print(f"User entered frequency factor: {entry_widget_x_freq.get()}")
    #
    print(f"User entered amplitude: {entry_widget_y_amp.get()}")
    print(f"User entered frequency factor: {entry_widget_y_freq.get()}")

root = tk.Tk()
root.title("Configurações")
root.geometry("400x200")
label = tk.Label(root, text="Parâmetros de Ajuste").grid(row=0,column=0)

# elements positions (rows, columns)
x_position = [2, 0]
y_position = [2, 1]
z_position = [2, 2]
u_position = [5, 0]
v_position = [5, 1]
w_position = [5, 2]

# eixos cartesianos
# parametros x
tk.Label(root, text="X").grid(row=x_position[0]-1, column=x_position[1])
x_amplitude = tk.DoubleVar()
entry_widget_x_amp = tk.Entry(root, textvariable=x_amplitude)
entry_widget_x_amp.grid(row=x_position[0],column=x_position[1])

x_freq = tk.IntVar()
entry_widget_x_freq = tk.Entry(root, textvariable=x_freq)
entry_widget_x_freq.grid(row=x_position[0]+1,column=x_position[1])

# parametros y
tk.Label(root, text="Y").grid(row=y_position[0]-1, column=y_position[1])
y_amplitude = tk.DoubleVar()
entry_widget_y_amp = tk.Entry(root, textvariable=y_amplitude)
entry_widget_y_amp.grid(row=y_position[0],column=y_position[1])

y_freq = tk.IntVar()
entry_widget_y_freq = tk.Entry(root, textvariable=y_freq)
entry_widget_y_freq.grid(row=y_position[0]+1,column=y_position[1])

# parametros z
tk.Label(root, text="Z").grid(row=z_position[0]-1, column=z_position[1])
z_amplitude = tk.DoubleVar()
entry_widget_z_amp = tk.Entry(root, textvariable=z_amplitude)
entry_widget_z_amp.grid(row=z_position[0],column=z_position[1])

z_freq = tk.IntVar()
entry_widget_z_freq = tk.Entry(root, textvariable=z_freq)
entry_widget_z_freq.grid(row=z_position[0]+1,column=z_position[1])

# angulos

# parametros u
tk.Label(root, text="U").grid(row=u_position[0]-1, column=u_position[1])
u_amplitude = tk.DoubleVar()
entry_widget_u_amp = tk.Entry(root, textvariable=u_amplitude)
entry_widget_u_amp.grid(row=u_position[0],column=u_position[1])

u_freq = tk.IntVar()
entry_widget_u_freq = tk.Entry(root, textvariable=u_freq)
entry_widget_u_freq.grid(row=u_position[0]+1,column=u_position[1])

# parametros v
tk.Label(root, text="V").grid(row=v_position[0]-1, column=v_position[1])
v_amplitude = tk.DoubleVar()
entry_widget_v_amp = tk.Entry(root, textvariable=v_amplitude)
entry_widget_v_amp.grid(row=v_position[0],column=v_position[1])

v_freq = tk.IntVar()
entry_widget_v_freq = tk.Entry(root, textvariable=v_freq)
entry_widget_v_freq.grid(row=v_position[0]+1,column=v_position[1])

# parametros w
tk.Label(root, text="W").grid(row=w_position[0]-1, column=w_position[1])
w_amplitude = tk.DoubleVar()
entry_widget_w_amp = tk.Entry(root, textvariable=w_amplitude)
entry_widget_w_amp.grid(row=w_position[0],column=w_position[1])

w_freq = tk.IntVar()
entry_widget_w_freq = tk.Entry(root, textvariable=w_freq)
entry_widget_w_freq.grid(row=w_position[0]+1,column=w_position[1])
    
button = tk.Button(root, text="Get Value", command=on_button_click).grid(row=0,column=1)

root.mainloop()

# def interface():
    


if __name__ == '__main__':
    main()
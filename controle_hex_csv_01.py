import tkinter as tk
import csv
import math
from time import sleep
from pipython import GCSDevice, pitools

__signature__ = 0x3ca8b29e8dce284b4c380701e26b337c


def truncate(number):
    truncated_number = "{:.3f}".format(number)
    return truncated_number


x_a = 0.0; x_f = 1
y_a = 0.0; y_f = 1
z_a = 2.0; z_f = 1
u_a = 0.0; u_f = 1
v_a = 0.0; v_f = 1
w_a = 1.0; w_f = 1

def on_button_click_values(x_a_b, x_f_b, y_a_b, y_f_b, z_a_b, z_f_b, u_a_b, u_f_b, v_a_b, v_f_b, w_a_b, w_f_b):
    print("assigning value to variables!")
    x_a_b = entry_widget_x_amp.get()
    x_f_b = entry_widget_x_freq.get()
    y_a_b = entry_widget_y_amp.get()
    y_f_b = entry_widget_y_freq.get()
    z_a_b = entry_widget_z_amp.get()
    z_f_b = entry_widget_z_freq.get()
    u_a_b = entry_widget_u_amp.get()
    u_f_b = entry_widget_u_freq.get()
    v_a_b = entry_widget_v_amp.get()
    v_f_b = entry_widget_v_freq.get()
    w_a_b = entry_widget_w_amp.get()
    w_f_b = entry_widget_w_freq.get()
    print("parameters:", x_a_b, x_f_b, y_a_b, y_f_b, z_a_b, z_f_b, u_a_b, u_f_b, v_a_b, v_f_b, w_a_b, w_f_b)
    print("values assigned to variables!")

def on_button_click_csv_generate(x_a_c, x_f_c, y_a_c, y_f_c, z_a_c, z_f_c, u_a_c, u_f_c, v_a_c, v_f_c, w_a_c, w_f_c):
    factor = 2000
    divisor = '\t'
    print('creating wave.txt!')
    print("parameters:", x_a_c, x_f_c, y_a_c, y_f_c, z_a_c, z_f_c, u_a_c, u_f_c, v_a_c, v_f_c, w_a_c, w_f_c)
    with open('wave.txt', 'w', newline='') as csvfile_w:
        sinwriter = csv.writer(csvfile_w, delimiter='d', quotechar='q', quoting=csv.QUOTE_NONE, escapechar='e')
        for i in range(factor+1):
            value_x = x_a_c*math.sin(math.pi*i/(factor/x_f_c))
            value_y = y_a_c*math.sin(math.pi*i/(factor/y_f_c))
            value_z = z_a_c*math.sin(math.pi*i/(factor/z_f_c))
            value_u = u_a_c*math.sin(math.pi*i/(factor/u_f_c))
            value_v = v_a_c*math.sin(math.pi*i/(factor/v_f_c))
            value_w = w_a_c*math.sin(math.pi*i/(factor/w_f_c))
            
            value_string = truncate(value_x)
            value_string = value_string + divisor + truncate(value_y)
            value_string = value_string + divisor + truncate(value_z)
            value_string = value_string + divisor + truncate(value_u)
            value_string = value_string + divisor + truncate(value_v)
            value_string = value_string + divisor + truncate(value_w)
            sinwriter.writerow([value_string])
    print('wave.txt created!')

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
    
button_values = tk.Button(root, text="Get Value", command=lambda: on_button_click_values(x_a, x_f, y_a, y_f, z_a, z_f, u_a, u_f, v_a, v_f, w_a, w_f))
button_values.grid(row=0,column=1)
button_csv = tk.Button(root, text="Get CSV", command=lambda: on_button_click_csv_generate(x_a, x_f, y_a, y_f, z_a, z_f, u_a, u_f, v_a, v_f, w_a, w_f))
button_csv.grid(row=0,column=2)

root.mainloop()


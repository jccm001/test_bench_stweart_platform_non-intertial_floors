import tkinter as tk
import csv
import math
from time import sleep
from pipython import GCSDevice, pitools

__signature__ = 0x3ca8b29e8dce284b4c380701e26b337c
CONTROLLERNAME = 'C-887'  # This sample ist only valid vor C-887 controller
STAGES = None  # connect stages to axes
REFMODES = None  # reference the connected stages
DATAFILE = r'wave.txt'

x_a = 0.0; x_f = 1
y_a = 0.0; y_f = 1
z_a = 0.0; z_f = 1
u_a = 0.0; u_f = 1
v_a = 0.0; v_f = 1
w_a = 0.0; w_f = 1

resolution = 2
default_mult_size = 1000

g_velocity = 10
g_num_cycles = 4
g_table_rate = 10

# elements positions (rows, columns)
x_position = [2, 0]
y_position = [2, 1]
z_position = [2, 2]
u_position = [5, 0]
v_position = [5, 1]
w_position = [5, 2]

velocity_position = [8, 0]
num_cycles_position = [8, 1]
table_rate_position = [8, 2]


def truncate(number):
    truncated_number = "{:.3f}".format(number)
    return truncated_number


def on_button_click_csv_generate(x_a_c, x_f_c, y_a_c, y_f_c, z_a_c, z_f_c, u_a_c, u_f_c, v_a_c, v_f_c, w_a_c, w_f_c):

    try:
        x_a_c = x_amplitude.get(); x_f_c = x_freq.get()
        y_a_c = y_amplitude.get(); y_f_c = y_freq.get()
        z_a_c = z_amplitude.get(); z_f_c = z_freq.get()
        u_a_c = u_amplitude.get(); u_f_c = u_freq.get()
        v_a_c = v_amplitude.get(); v_f_c = v_freq.get()
        w_a_c = w_amplitude.get(); w_f_c = w_freq.get()
        g_velocity = vel.get()
        g_num_cycles = num_cycles.get()
        g_table_rate = table_rate.get()
    except Exception as e:
        print("certifique-se de que todos os campos estão preenchidos corretamente.")
        return
    
    mult_size = x_mult_size.get()
    # mult_size = 250
    factor = x_factor.get()
    points = mult_size * factor
    
    divisor = '\t'
    print('\ncreating wave.txt!\n')
    print("file points:", points)
    print("wave parameters:", "\n\tX: ", x_a_c, x_f_c, "\n\tY: ", y_a_c, y_f_c, "\n\tZ: ", z_a_c, z_f_c, "\n\tU: ", u_a_c, u_f_c, "\n\tV: ", v_a_c, v_f_c, "\n\tW: ", w_a_c, w_f_c)
    print("hexapode parameters:", "\n\tVelocity: ", g_velocity, "\n\tCycles: ", g_num_cycles, "\n\tRate: ", g_table_rate)
    
    with open('wave.txt', 'w', newline='') as csvfile_w:
        sinwriter = csv.writer(csvfile_w, delimiter='d', quotechar='q', quoting=csv.QUOTE_NONE, escapechar='e')
        for i in range(points+1):
            if x_a_c > 0:
                value_x = x_a_c*math.sin(2*math.pi*i*x_f_c/(points/factor))
            else:
                value_x = x_a_c*math.cos(2*math.pi*i*x_f_c/(points/factor))
                
            if y_a_c > 0:
                value_y = y_a_c*math.sin(2*math.pi*i*y_f_c/(points/factor))
            else:
                value_y = y_a_c*math.cos(2*math.pi*i*y_f_c/(points/factor))
                
            if z_a_c > 0:
                value_z = z_a_c*math.sin(2*math.pi*i*z_f_c/(points/factor))
            else:
                value_z = z_a_c*math.cos(2*math.pi*i*z_f_c/(points/factor))
                
            if u_a_c > 0:
                value_u = u_a_c*math.sin(2*math.pi*i*u_f_c/(points/factor))
            else:
                value_u = u_a_c*math.cos(2*math.pi*i*u_f_c/(points/factor))
                
            if v_a_c > 0:
                value_v = v_a_c*math.sin(2*math.pi*i*v_f_c/(points/factor))
            else:
                value_v = v_a_c*math.cos(2*math.pi*i*v_f_c/(points/factor))
                
            if w_a_c > 0:
                value_w = w_a_c*math.sin(2*math.pi*i*w_f_c/(points/factor))
            else:
                value_w = w_a_c*math.cos(2*math.pi*i*w_f_c/(points/factor))
            
            value_string = truncate(value_x)
            value_string = value_string + divisor + truncate(value_y)
            value_string = value_string + divisor + truncate(value_z)
            value_string = value_string + divisor + truncate(value_u)
            value_string = value_string + divisor + truncate(value_v)
            value_string = value_string + divisor + truncate(value_w)
            sinwriter.writerow([value_string])
    print('\nwave.txt created!')

def readwavedata():
    """Read DATAFILE, must have a column for each wavetable.
    @return : Datapoints as list of lists of values.
    """
    print('\nread wave points from file {}'.format(DATAFILE))
    data = None
    with open(DATAFILE) as datafile:
        for line in datafile:
            items = line.strip().split()
            if data is None:
                print('found {} data columns in file\n'.format(len(items)))
                data = [[] for _ in range(len(items))]
            for i, item in enumerate(items):
                data[i].append(item)
    return data

def runwavegen(pidevice, NUMCYLES, TABLERATE):
    """Read wave data, set up wave generator and run them.
    @type pidevice : pipython.gcscommands.GCSCommands
    """
    
    
    wavedata = readwavedata()
    axes = pidevice.axes[:len(wavedata)]
    assert len(wavedata) == len(axes), 'this sample requires {} connected axes'.format(len(wavedata))
    
    # wavetables = range(1, len(wavedata) + 1)
    # wavegens = range(1, len(wavedata) + 1)
    wavegens = (1, 2, 3, 4, 5, 6)
    wavetables = (1, 2, 3, 4, 5, 6)
    
    if pidevice.HasWSL():  # you can remove this code block if your controller does not support WSL()
        print('\nconnect wave tables {} to wave generators {}'.format(wavetables, wavegens))
        pidevice.WSL(wavegens, wavetables)
    #
    if pidevice.HasWGC():  # you can remove this code block if your controller does not support WGC()
        print('\nset wave generators {} to run for {} cycles'.format(wavegens, NUMCYLES))
        pidevice.WGC(wavegens, [NUMCYLES] * len(wavegens))
    #
    if pidevice.HasWTR():  # you can remove this code block if your controller does not support WTR()
        print('\nset wave table rate to {} for wave generators {}\n'.format(TABLERATE, wavegens))
        pidevice.WTR(wavegens, [TABLERATE] * len(wavegens), interpol=[0] * len(wavegens))
        
    if pidevice.HasWCL():  # you can remove this code block if your controller does not support WCL()
        print('clear wave tables {}'.format(wavetables))
        pidevice.WCL(wavetables)
    
    for i, wavetable in enumerate(wavetables):
        print('write wave points of wave table {} and axis {}'.format(wavetable, axes[i]))
        pitools.writewavepoints(pidevice, wavetable, wavedata[i], bunchsize=10)
        
    startpos = [wavedata[i][0] for i in range(len(wavedata))]
    print('\nmove axes {} to start positions \n{}'.format(axes, startpos))
    pidevice.MOV(axes, startpos)
    pitools.waitontarget(pidevice, axes)
    
    print('\nstart wave generators {}'.format(wavegens))
    pidevice.WGO(wavegens, mode=[1] * len(wavegens))
    
    while any(list(pidevice.IsGeneratorRunning(wavegens).values())):
        print('.', end='')
        sleep(1.0)
        
    print('\nreset wave generators {}'.format(wavegens))
    pidevice.WGO(wavegens, mode=[0] * len(wavegens))
    print('\ndone')
    print('\n-------------------------------------------------------------------------------------------')

# def set_velocity(pidevice, VELOCITY):
#     pidevice.VLS(VELOCITY)

def execute(pidevice, VELOCITY, NUMCYLES, TABLERATE):
    on_button_click_csv_generate(x_a, x_f, y_a, y_f, z_a, z_f, u_a, u_f, v_a, v_f, w_a, w_f)
    VELOCITY = vel.get()
    NUMCYLES = num_cycles.get()
    TABLERATE = table_rate.get()
    
    pidevice.VLS(VELOCITY)
    runwavegen(pidevice, NUMCYLES, TABLERATE)
    

with GCSDevice(CONTROLLERNAME) as pidevice:
    pidevice.ConnectRS232(comport=3, baudrate=115200)
    print('connected: %s' % pidevice.qIDN().strip())
    print('initialize connected stages...')
    pitools.startup(pidevice, stages=STAGES, refmodes=REFMODES)
    
    root = tk.Tk()
    root.title("Parâmetros de Ajuste")
    root.geometry("400x200")
    # label = tk.Label(root, text="Parâmetros de Ajuste").grid(row=0,column=0)
    
    
    x_factor = tk.IntVar()
    x_factor.set(resolution)
    entry_widget_x_factor = tk.Entry(root, textvariable=x_factor)
    entry_widget_x_factor.grid(row=0,column=0)
    
    x_mult_size = tk.IntVar()
    x_mult_size.set(default_mult_size)
    entry_widget_x_mult_size = tk.Entry(root, textvariable=x_mult_size)
    entry_widget_x_mult_size.grid(row=0,column=1)
    
    # --------------------------------------------------------------------------
    # eixos cartesianos
    
    # parametros x
    tk.Label(root, text="X").grid(row=x_position[0]-1, column=x_position[1])
    x_amplitude = tk.DoubleVar()
    entry_widget_x_amp = tk.Entry(root, textvariable=x_amplitude)
    entry_widget_x_amp.grid(row=x_position[0],column=x_position[1])
    
    x_freq = tk.IntVar()
    x_freq.set(x_f)
    entry_widget_x_freq = tk.Entry(root, textvariable=x_freq)
    entry_widget_x_freq.grid(row=x_position[0]+1,column=x_position[1])
    
    # parametros y
    tk.Label(root, text="Y").grid(row=y_position[0]-1, column=y_position[1])
    y_amplitude = tk.DoubleVar()
    entry_widget_y_amp = tk.Entry(root, textvariable=y_amplitude)
    entry_widget_y_amp.grid(row=y_position[0],column=y_position[1])
    
    y_freq = tk.IntVar()
    y_freq.set(y_f)
    entry_widget_y_freq = tk.Entry(root, textvariable=y_freq)
    entry_widget_y_freq.grid(row=y_position[0]+1,column=y_position[1])
    
    # parametros z
    tk.Label(root, text="Z").grid(row=z_position[0]-1, column=z_position[1])
    z_amplitude = tk.DoubleVar()
    entry_widget_z_amp = tk.Entry(root, textvariable=z_amplitude)
    entry_widget_z_amp.grid(row=z_position[0],column=z_position[1])
    
    z_freq = tk.IntVar()
    z_freq.set(z_f)
    entry_widget_z_freq = tk.Entry(root, textvariable=z_freq)
    entry_widget_z_freq.grid(row=z_position[0]+1,column=z_position[1])
    
    # --------------------------------------------------------------------------
    # angulos
    
    # parametros u
    tk.Label(root, text="U").grid(row=u_position[0]-1, column=u_position[1])
    u_amplitude = tk.DoubleVar()
    entry_widget_u_amp = tk.Entry(root, textvariable=u_amplitude)
    entry_widget_u_amp.grid(row=u_position[0],column=u_position[1])
    
    u_freq = tk.IntVar()
    u_freq.set(u_f)
    entry_widget_u_freq = tk.Entry(root, textvariable=u_freq)
    entry_widget_u_freq.grid(row=u_position[0]+1,column=u_position[1])
    
    # parametros v
    tk.Label(root, text="V").grid(row=v_position[0]-1, column=v_position[1])
    v_amplitude = tk.DoubleVar()
    entry_widget_v_amp = tk.Entry(root, textvariable=v_amplitude)
    entry_widget_v_amp.grid(row=v_position[0],column=v_position[1])
    
    v_freq = tk.IntVar()
    v_freq.set(v_f)
    entry_widget_v_freq = tk.Entry(root, textvariable=v_freq)
    entry_widget_v_freq.grid(row=v_position[0]+1,column=v_position[1])
    
    # parametros w
    tk.Label(root, text="W").grid(row=w_position[0]-1, column=w_position[1])
    w_amplitude = tk.DoubleVar()
    entry_widget_w_amp = tk.Entry(root, textvariable=w_amplitude)
    entry_widget_w_amp.grid(row=w_position[0],column=w_position[1])
    
    w_freq = tk.IntVar()
    w_freq.set(w_f)
    entry_widget_w_freq = tk.Entry(root, textvariable=w_freq)
    entry_widget_w_freq.grid(row=w_position[0]+1,column=w_position[1])
    
    # --------------------------------------------------------------------------
    # parametros do hexapode
    
    # velocidade de deslocamento
    tk.Label(root, text="Velocity").grid(row=velocity_position[0]-1, column=velocity_position[1])
    vel = tk.DoubleVar()
    vel.set(g_velocity)
    entry_widget_vel = tk.Entry(root, textvariable=vel)
    entry_widget_vel.grid(row=velocity_position[0]+1,column=velocity_position[1])
    
    
    # numero de repetições
    tk.Label(root, text="Cycles").grid(row=num_cycles_position[0]-1, column=num_cycles_position[1])
    num_cycles = tk.IntVar()
    num_cycles.set(g_num_cycles)
    entry_widget_num_cycles = tk.Entry(root, textvariable=num_cycles)
    entry_widget_num_cycles.grid(row=num_cycles_position[0]+1,column=num_cycles_position[1])
    
    
    # duracao dos ciclos
    # "duration of a wave table point in multiples of servo cycle times as integer"
    tk.Label(root, text="Rate").grid(row=table_rate_position[0]-1, column=table_rate_position[1])
    table_rate = tk.IntVar()
    table_rate.set(g_table_rate)
    entry_widget_table_rate = tk.Entry(root, textvariable=table_rate)
    entry_widget_table_rate.grid(row=table_rate_position[0]+1,column=table_rate_position[1])
    
    # --------------------------------------------------------------------------
    # botões
    # button_csv = tk.Button(root,text="Get Table", command=lambda: on_button_click_csv_generate(
    #     x_a, x_f,
    #     y_a, y_f,
    #     z_a, z_f,
    #     u_a, u_f,
    #     v_a, v_f,
    #     w_a, w_f)
    # )
    # button_csv.grid(row=0,column=1)
    
    button_send_wave = tk.Button(root, text="Send Wave", command=lambda: execute(
        pidevice,
        g_velocity,
        g_num_cycles,
        g_table_rate))
    button_send_wave.grid(row=0,column=2)
    
    def on_closing():
        pidevice.CloseConnection()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    root.mainloop()

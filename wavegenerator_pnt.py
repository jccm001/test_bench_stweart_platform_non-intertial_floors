#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This example helps you to define arbitrary waveforms read out from a file."""

# (c)2016 Physik Instrumente (PI) GmbH & Co. KG
# Software products that are provided by PI are subject to the
# General Software License Agreement of Physik Instrumente (PI) GmbH & Co. KG
# and may incorporate and/or make use of third-party software components.
# For more information, please read the General Software License Agreement
# and the Third Party Software Note linked below.
# General Software License Agreement:
# http://www.physikinstrumente.com/download/EULA_PhysikInstrumenteGmbH_Co_KG.pdf
# Third Party Software Note:
# http://www.physikinstrumente.com/download/TPSWNote_PhysikInstrumenteGmbH_Co_KG.pdf


from time import sleep

from pipython import GCSDevice, pitools

__signature__ = 0x3ca8b29e8dce284b4c380701e26b337c

CONTROLLERNAME = 'C-887'  # This sample ist only valid vor C-887 controller
STAGES = None  # connect stages to axes
REFMODES = None  # reference the connected stages

VELOCITY = 25

# DATAFILE = r'wavegenerator_pnt.txt'
DATAFILE = r'wave.txt'
NUMCYLES = 4  # number of cycles for wave generator output
TABLERATE = 10  # duration of a wave table point in multiples of servo cycle times as integer


def main():
    """Connect controller, setup wave generator, move axes to startpoint and start wave generator."""
    with GCSDevice(CONTROLLERNAME) as pidevice:
        # pidevice.ConnectTCPIP(ipaddress='192.168.178.42')
        # pidevice.ConnectUSB(serialnum='000000004')
        pidevice.ConnectRS232(comport=3, baudrate=115200)
        print('connected: %s' % pidevice.qIDN().strip())
        print('initialize connected stages...')
        pitools.startup(pidevice, stages=STAGES, refmodes=REFMODES)
        
        # vel = pidevice.qVEL('x')
        # print('\nvelocity set as %i' %vel)
        # vel = pidevice.VLS(VELOCITY)
        # print('\nnew maximum velocity set as %i' %VELOCITY)
        
        runwavegen(pidevice)
        


def runwavegen(pidevice):
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
    
    for i, wavetable in enumerate(wavetables):
        print('write wave points of wave table {} and axis {}'.format(wavetable, axes[i]))
        pitools.writewavepoints(pidevice, wavetable, wavedata[i], bunchsize=10)
        
    # if pidevice.HasWCL():  # you can remove this code block if your controller does not support WCL()
    #     print('\nclear wave tables {}'.format(wavetables))
    #     pidevice.WCL(wavetables)
    #
    if pidevice.HasWSL():  # you can remove this code block if your controller does not support WSL()
        print('\nconnect wave tables {} to wave generators {}'.format(wavetables, wavegens))
        pidevice.WSL(wavegens, wavetables)
    #
    if pidevice.HasWGC():  # you can remove this code block if your controller does not support WGC()
        print('\nset wave generators {} to run for {} cycles'.format(wavegens, NUMCYLES))
        pidevice.WGC(wavegens, [NUMCYLES] * len(wavegens))
    #
    if pidevice.HasWTR():  # you can remove this code block if your controller does not support WTR()
        print('\nset wave table rate to {} for wave generators {}'.format(TABLERATE, wavegens))
        pidevice.WTR(wavegens, [TABLERATE] * len(wavegens), interpol=[0] * len(wavegens))
        
    startpos = [wavedata[i][0] for i in range(len(wavedata))]
    print('\nmove axes {} to start positions {}'.format(axes, startpos))
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


if __name__ == '__main__':
    # from pipython import PILogger, DEBUG, INFO, WARNING, ERROR, CRITICAL
    # PILogger.setLevel(DEBUG)
    main()

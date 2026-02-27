'''
Created on 19 de jan. de 2026

@author: Julio
'''
from pipython import GCSDevice, pitools

__signature__ = 0x986c0f898592ce476e1c88820b09bf94

controllername = 'C-887'

gcs = GCSDevice(controllername)

gcs.InterfaceSetupDlg()

print(gcs.qIDN())

gcs.CloseConnection()


from turtle import position


smb_ruta='/1.1.1.1/eoi/python'
smb_ruta= smb_ruta[2:]
posicion_barra= smb_ruta.index('/')
direccion=smb_ruta[:posicion_barra]
path= smb_ruta[posicion_barra:]
print(f'host={direccion});path={path}')

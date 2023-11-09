#Lectura de archivos
def read(archivo):
    with open(archivo, 'r') as file:
        lineas = file.readlines()
    return lineas
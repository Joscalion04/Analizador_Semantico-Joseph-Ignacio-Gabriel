#Proyecto 2, Estructura de Datos, Ignacio Bonilla - Joseph Leon - Gabriel Robleto  
import Lectura
import Analisis

dato = ""
prev = "213a"
text = None

"""
lineas = Lectura.read("Codigo.txt") 
for linea in lineas: 
    words = Lectura.separateWords(linea)
    for word in words: 
        if Analisis.isTipo(word) == True: 
            dato = word
        elif word == '=': 
            prev = word
        elif dato != None and prev != None: 
            text = word
            print(Analisis.tipoDato(dato,text))
            dato = None
            prev = None

"""

""""
#Asi se agregan elementos en el diccionario 
datos = {}     
datos["x"] = (int, "122")  #asi agregamos variables 
datos["y"] = (float, "122.5")

funcion={}
funcion["sumar"]=(10,10) #asi agregamos funciones 
funcion["resta"]=(10,2)
datos ["funcion"] = funcion
#print(datos["funcion"]["resta"][1]) #asi se accede a un dato dentro de una posicion 

linea = "double a = 12.3 "
dato, nombre, valor = Lectura.dataIdentifyTypeToNameToValue(linea)
print("El tipo de dato es:" + dato)
print("El nombre de la variable es: "+ nombre)
print("El valor es: "+valor)
"""

def lectura(linea, num):
    tipo = ""
    nombre = ""
    valor = ""
    operacion = ""
    error = "Linea " + str(num) + " exitosa"
    try:
        tipo , nombre, valor, operacion = Lectura.dataIdentifyTypeToNameToValue(linea)
        if Analisis.isTipo(tipo) == False: 
            error = "Linea " + str(num) + " Error: "+ str(tipo) + " no es un tipo de dato aceptado"
        elif Analisis.validateGeneral(tipo,valor) == False: 
            error = "Linea " + str(num) + " Error: "+ str(valor) + " no es un dato aceptable para una variable de tipo " + str(tipo)            
    except Exception: 
       print("linea sin poder leerse 1")
       pass
    try:
        tipo, nombre, operacion = Lectura.dataIdentifyTypeToName(line)
        if Analisis.isTipo(tipo) == False: 
            error = "Linea " + str(num) + " Error: "+ str(tipo) + " no es un tipo de dato aceptado"
    except Exception: 
        print("linea sin poder leerse 2")
        pass  
    return error 
lineas = Lectura.read("Codigo.txt") 
numLine = 0 
for line in lineas: 
    print(lectura(line,numLine))
    numLine += 1


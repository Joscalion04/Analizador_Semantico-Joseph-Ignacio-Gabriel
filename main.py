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

def lectura(linea):
    try:
      tipo, nombre3, valor3, operacion = Lectura.dataIdentifyTypeToNameToValue(linea)
      print("Operacion " + operacion )
      print("Tipo " + tipo)
      print("Nombre: "+ nombre3)
      print("Valor: "+ valor3)

    except Exception: 
       print("linea sin poder leerse 1")
       pass

    try:
        tipo2, nombre, operacion2 = Lectura.dataIdentifyTypeToName(line)
        print("Operacion " + operacion2 ) 
        print("Tipo " + tipo2)
        print("Nombre: "+ nombre)
         
    except Exception: 
        print("linea sin poder leerse 2")
        pass  

lineas = Lectura.read("Codigo.txt")  
for line in lineas: 
    lectura(line)


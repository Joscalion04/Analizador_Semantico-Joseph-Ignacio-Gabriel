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

def lectura(linea, num, operacion, function, functionName):
    tipo = ""
    nombre = ""
    valor = ""
    error = "Linea " + str(num) + " exitosa"
    try:
        tipo , nombre, valor, operacion = Lectura.dataIdentifyTypeToNameToValue(linea)
        if Analisis.isTipo(tipo) == False: 
            error = "Linea " + str(num) + " Error: "+ str(tipo) + " no es un tipo de dato aceptado"
        elif Analisis.validateGeneral(tipo,valor) == False: 
            error = "Linea " + str(num) + " Error: "+ str(valor) + " no es un dato aceptable para una variable de tipo " + str(tipo)
            if function ==True:
                if Analisis.KeyInFunction(functionName, nombre) == False:
                    Analisis.addVarFunction(functionName, nombre,tipo)
                else:
                    error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
            else: 
                if Analisis.KeyEnDiccionario(nombre)==False:
                    Analisis.addVariableGen(nombre,tipo)
                else: 
                     error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
    except Exception: 
       print("linea sin poder leerse 1")
       pass


    try:
        tipo, nombre, operacion = Lectura.dataIdentifyTypeToName(line)
        if Analisis.isTipo(tipo) == False: 
            error = "Linea " + str(num) + " Error: "+ str(tipo) + " no es un tipo de dato aceptado"
        else: 
            if function ==True:
                if Analisis.KeyInFunction(functionName, nombre) == False:
                    Analisis.addVarFunction(functionName, nombre,tipo)
                else:
                    error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
            else: 
                if Analisis.KeyEnDiccionario(nombre)==False:
                    Analisis.addVariableGen(nombre,tipo)
                else: 
                     error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
    except Exception: 
        print("linea sin poder leerse 2")
        pass  
    
    try:
        name, valor, operacion = Lectura.dataIdentifyNameToValue(line)
        if Analisis.KeyEnDiccionario(name) == True: 
            if Analisis.validateGeneral(Analisis.TipoVarEnDiccionario(name),valor) == False:
                error = "Linea " + str(num) + " Error: "+ str(valor) + " no es un dato aceptable para una variable de tipo " + str(tipo)
        elif function == True: 
            if Analisis.KeyInFunction(functionName, name) == True:
                if Analisis.validateGeneral()
                
    except Exception:
        print("linea sin poder leerse 3")
        pass
  

    return error,operacion, function, functionName


lineas = Lectura.read("Codigo.txt") 
numLine = 0 
operacion = ""
function = False
functionName = ""
for line in lineas: 
    error, operacion, function, functionName = lectura(line,numLine, operacion,function, functionName)
    print(error)
    numLine += 1

print(Analisis.diccionarioGen)


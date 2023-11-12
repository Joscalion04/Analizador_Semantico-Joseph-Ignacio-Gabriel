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


#Asi se agregan elementos en el diccionario 
datos = {}     
datos["x"] = (int, "122")  #asi agregamos variables 
datos["y"] = (float, "122.5")

funcion={}
funcion["sumar"]=(10,10) #asi agregamos funciones 
funcion["resta"]=(10,2)
datos ["funcion"] = funcion
#print(datos["funcion"]["resta"][1]) #asi se accede a un dato dentro de una posicion 

def KeyEnDiccionario(word,dic):
    if word in dic:
        print("Si esta")
    else: 
        print("No esta")


def ValorEnDiccionario(word):
    if  diccionarioGen[word][0] == "var":
        return  diccionarioGen[word][2]
    if  diccionarioGen[word][0] == "fun":
        return 

def funEnDiccionario(funName,):



KeyEnDiccionario("funcion",datos)
KeyEnDiccionario("sumar",funcion)



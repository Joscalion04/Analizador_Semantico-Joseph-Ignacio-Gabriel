#Proyecto 2, Estructura de Datos, Ignacio Bonilla - Joseph Leon - Gabriel Robleto  
import Lectura
import Analisis

dato = None
prev = None
text = None


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






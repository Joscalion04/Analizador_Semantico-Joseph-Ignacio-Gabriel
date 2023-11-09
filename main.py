#Proyecto 2, Estructura de Datos, Ignacio Bonilla - Joseph Leon - Gabriel Robleto  
import Lectura
import Analisis


lineas = Lectura.read("Codigo.txt")
for linea in lineas: 
    words = Lectura.separateWords(linea)
    for word in words: 
        print(word)




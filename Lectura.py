#Lectura de archivos
import re

def read(archivo):
    with open(archivo, 'r') as file:
        lineas = file.readlines()
    return lineas

def separateWords(text): 
    words=[]
    lines = text.split('\n')
    for line in lines: 
        lineWords = line.split(' ')
        words.extend(lineWords)
    return words 

def dataIdentify(text):
    patron = r"(\w+)\s+(\w+)\s+=\s+(.+)"
    
    dataValue = ""
    dataType = ""
    resultado = re.search(patron, text)
    if resultado:
        dataType = resultado.group(1)
        dataName = resultado.group(2)
        dataValue = resultado.group(3)
        return dataType,dataName,dataValue
    else:
        return None


 
# tipo nombre =  valor     //1  nueva variable
# nombre = valor           //2   variable = valor
# nombre = nombre         //3     variable = variable 
# tipo nombre (           //4     nueva funcion 
# (tipo nombre, tipo nombre)  //5 parametros
# } //6 cierre de funcion 


def dataIdentifyWithParenthesis(text):
    patron = r"(\w+)\s+(\w+)\s+\((.*)\)"

    dataType = ""
    dataName = ""
    dataValue = ""
    resultado = re.search(patron, text)
    if resultado:
        dataType = resultado.group(1)
        dataName = resultado.group(2)
        dataValue = resultado.group(3)
        return dataType,dataName,dataValue
    else:
        return None
    


text = "int a (int x, int y ) "

dataType, dataName, dataValue = dataIdentifyWithParenthesis(text)

print(dataType)
print(dataName)
print(dataValue)

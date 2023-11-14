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

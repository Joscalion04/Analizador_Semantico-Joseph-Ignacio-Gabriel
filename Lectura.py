#Lectura de archivos
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

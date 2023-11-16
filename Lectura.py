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
        if line != '\n': 
            lineWords = line.split(' ')
            words.extend(lineWords)
    return words 

# tipo nombre =  valor         //1 nueva variable -> Check
# tipo nombre                  //2 variable sin valor
# nombre = valor               //3 variable = valor -> Check
# nombre = nombre              //4 variable = variable 
# tipo nombre (                //5 nueva funcion 
# (tipo nombre, tipo nombre)   //6 parametros
# }                            //7 cierre de funcion 

def dataIdentifyTypeToNameToValue(text): #1 JOSEPH <------------- CHECK ------------
    try: 
        patron = r"(\w+)\s+(\w+)\s*=\s*(.+)"
        dataValue = "" 
        dataType = "" 
        resultado = re.search(patron, text)
        if re.match(patron,text):
            if resultado: 
                dataType = resultado.group(1) 
                dataName = resultado.group(2) 
                dataValue = resultado.group(3) 
                if(len(dataValue.split()) == 1):
                    return dataType,dataName,dataValue,"1" 
                else:
                    raise ValueError("Error, argumentos")
        else:
            return None
    except Exception: 
        return None
    
def dataIdentifyTypeToName(text): #2 JOSEPH <------------- CHECK ------------
    try: 
        if len(text.split()) != 2: 
            raise ValueError("Invalid number of words. Expected 2.") 
        patron = r"(\w+)\s+(\w+)+?" 
        resultado = re.search(patron, text) 
        if resultado: 
            dataType = resultado.group(1) 
            dataName = resultado.group(2) 
            return dataType, dataName,"2" 
    except Exception:  
        return None  

def dataIdentifyNameToValue(text): #3
    if len(text.split()) >3:
            return None
    patron = r"([A-Za-z]+)\s*=\s*([0-9_]+)\s*$"
    resultado = re.search(patron, text)
    if resultado is None:
        patron = r"([A-Za-z]+)\s*=\s*('[^']*'|\"[^\"]*\")\s*$"
        resultado =  re.search(patron, text)
    if resultado:
        dataName = resultado.group(1)
        dataValue = resultado.group(2)
        return dataName, dataValue, "3" 
    else:
        return None

def dataIdentifyNameToName(text):  #4
    if len(text.split()) > 3:
           return None
    patron = r"([A-Za-z]+)\s*=\s*([A-Za-z]+)\s*$"
    resultado = re.search(patron, text)
    if resultado:
        nombre1 = resultado.group(1)
        nombre2 = resultado.group(2)
        return nombre1, nombre2, "4"
    else:
        return None

def dataIdentifyWithParenthesis(text): #5 JOSEPH <------------- CHECK ------------
    patron = r"(\w+)\s+(\w+)\s*\(\s*(.*)\s*\)\s*(\{)?"
    dataType = ""
    dataName = ""
    resultado = re.search(patron, text)
    if resultado:
        dataType = resultado.group(1)
        dataName = resultado.group(2)
        parameters = resultado.group(3)
        if resultado.group(4) == "{" or resultado.group(4) == "":
           return dataType, dataName, parameters, "5"
        return None
    else:
        return None

def find_closing_brace(line):
    if "}" in line:
        if line[line.index("}") + 1:] == "":
            return "8"
        else:
            return None
    else:
        return None

#tipo nombre , .... de una linea 
# int x, int y, string p... 


#text = "int a (int x, int y ) "

"""
dataType, dataName, dataValue = dataIdentifyWithParenthesis(text)

print(dataType)
print(dataName)
print(dataValue)

linea2 = "string a"
tipo2, nombre2 = dataIdentifyTypeToName(linea2)
print("\nDATA IDENTIFY 2")
print("Tipo: "+ tipo2)
print("Nombre: "+ nombre2)

linea3 = "a = joseph"
nombre3, valor3 = dataIdentifyNameToValue(linea3)
print("\nDATA IDENTIFY 3")
print("Nombre: "+ nombre3)
print("Valor: "+ valor3)

linea4 = "var1 = var2"
variable1,variable2 = dataIdentifyNameToName(linea4)
print("\nDATA IDENTIFY 4")
print("Var 1: "+ variable1)
print("Var 2: "+ variable2)
"""
def variablesDeLasFunciones(text):

    parameters=[]
    line = text
    line=line.replace(",",'')
    lines = text.split('\n')
    lineWords = line.split(' ')
    word=""
    for line in lineWords:  
            word=line
            try:
                var1, var2,num = dataIdentifyNameToName(word)
                parameters.append(var1)
                parameters.append(var2)
            except Exception:
                try: 
                    var3, var4,num = dataIdentifyNameToValue(word)
                    parameters.append(var3)
                    parameters.append(var4)
                except Exception:
                    word=word.replace("=",'')
                    if word !='':
                        parameters.append(word)
    return parameters      


#parametros=variablesDeLasFunciones(" int x=0, int y = 0, string p='pruebas' , string c ")

#print(parametros)
#print(dataIdentifyNameToValue('e = pepe 89'))
#Lectura de archivos
import re

def read(archivo):
    with open(archivo, 'r') as file:
        lineas = [line.lstrip() for line in file.readlines()]
    return lineas

def separateWords(text): 
    words=[]
    lines = text.split('\n')
    for line in lines:
        if line != '\n': 
            lineWords = line.split(' ')
            words.extend(lineWords)
    return words 

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

def dataNametoOperation(text): # JOSEPH <-------------UN- CHECK ------------
    try:
        patron = r"(\w+)\s*=\s*((\w+(\s*[\+\-\*/]\s*\w+)*))"
        resultado = re.search(patron, text)
        if resultado and resultado.start() == 0:
            dato = resultado.group(1)
            operacion = resultado.group(2)
            if not re.match(r'^\w+(\s*[\+\-\*/]\s*\w+)*$', operacion):
                return None
            operandos = re.split(r'\s*[\+\-\*/]\s*', operacion)
            return dato, operandos,"8"
        else:
            return None
    except Exception:
        return None
    
def dataTypeNameToOperation(text): # JOSEPH <-------------UN- CHECK ------------
    try:
        patron = r"(\w+)\s+(\w+)\s*=\s*((\w+(\s*[\+\-\*/]\s*\w+)*))"
        resultado = re.search(patron, text)
        if resultado and resultado.start() == 0:
            daatYpe = resultado.group(1)
            nameData = resultado.group(2)
            operators = resultado.group(3)
            if not re.match(r'^\w+(\s*[\+\-\*/]\s*\w+)*$', operators):
                return None
            operators = re.split(r'\s*[\+\-\*/]\s*', operators)
            return daatYpe, nameData, operators,"9"
        else:
            return None
    except Exception:
        return None

def conditionalDetection(text):# JOSEPH <-------------CHECK ------------
    try:
        patron = r"^\s*if\s*\(\s*(\w+)\s*([<>]=?)\s*(\w+)\s*\)\s*{?$"
        resultado = re.search(patron, text)
        if resultado:
            value1 = resultado.group(1)
            value2 = resultado.group(3)
            return "if", value1, value2,"10"
        else:
            return None
    except Exception:
        return None
    
def loopDetection(text):# JOSEPH <-------------CHECK ------------
    try:
        patron = r"^\s*while\s*\(\s*(\w+)\s*([<>]=?)\s*(\w+)\s*\)\s*{?$"
        resultado = re.search(patron,text)
        if resultado:
            value1 = resultado.group(1)
            value2 = resultado.group(2)
            return "while",value1,value2, "11"
        else:
            return None
    except Exception:
        return None

def dataToNameToFunction(text): # JOSEPH <-------------CHECK ------------
    pattern = r"(\w+)\s+(\w+)\s*=\s*(\w+)\s*\(\s*(.*?)\s*\)"
    match = re.match(pattern, text)
    if match:
        data_type = match.group(1)
        variable_name = match.group(2)
        function_name = match.group(3)
        params_string = match.group(4)
        if re.match(r"[a-zA-Z]+", data_type):
            return data_type, variable_name, function_name, params_string,"12"
        else:
            return None
    else:
        return None

def nameToFunction(text): # JOSEPH <-------------CHECK ------------
    pattern = r"(\w+)\s*=\s*(\w+)\s*\(\s*(.*?)\s*\)"
    match = re.match(pattern, text)
    if match:
        variable_name = match.group(1)
        function_name = match.group(2)
        params_string = match.group(3)
        return variable_name, function_name, params_string, "13"
    else:
        return None

# ---------------------------------- DATOS Y PRUEBAS LECTURA.PY --------------------------------------
def validaLinea(linea):
    if dataTypeNameToOperation(linea):
        tipo_dato, nombre_dato, operadores,nun = dataTypeNameToOperation(linea)
        print("Tipo de Dato:", tipo_dato)
        print("Nombre del Dato:", nombre_dato)
        print("Operadores:", operadores)
        print("Numero de Operacion: "+num)
    elif dataNametoOperation(linea):
        dato, operandos,num = dataNametoOperation(linea)
        print("Dato:", dato)
        print("Operandos:", operandos)
        print("Numero de Operacion: "+num)
    elif conditionalDetection(linea):
        condicion, valor1, valor2,num = conditionalDetection(linea)
        print("Condicional: " + condicion)
        print("Valor 1: " + valor1)
        print("Valor 2: " + valor2)
        print("Numero de Operacion: "+num)
    elif loopDetection(linea):
        loop, valor1, valor2,num = loopDetection(linea)
        print("Condicional: " + loop)
        print("Valor 1: " + valor1)
        print("Valor 2: " + valor2)
        print("Numero de Operacion: "+num)
    else :
        print("ERROR DE LINEA")

texto_ejemplo = "while (5 < 6){"
validaLinea(texto_ejemplo)
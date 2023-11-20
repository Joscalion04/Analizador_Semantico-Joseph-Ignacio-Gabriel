#Lectura de archivos
import re

"""
read es un metodo dedicado a la lectura del documento, se encarga de insertar cada linea por separado en una lista, 
a su vez elimina los espacios en blancos al inicio de cada linea para facilitar el analisis de la misma
Parametros: 
(String) - archivo: Nombre del Archivo
Devolucion: 
-Lista: Lista de Lineas
"""
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

"""
dataIdentifyTypeToNameToValue es un metodo dedicado a la lectura de una linea para
 detectar el patron especifico: tipo Dato, nombre Dato y valor de dato, y agrupar esos datos de forma individual
Parametros: 
(String) - text: linea a estructurar
Devolucion: 
- String : tipo de dato, nombre del dato, valor del dato, numero de Operacion de Estructuracion
"""

def dataIdentifyTypeToNameToValue(text):# ------------------------------- Operacion 1
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
    

"""
dataIdentifyTypeToName es un metodo dedicado a la lectura de una linea para
 detectar el patron especifico: tipo Dato, nombre Dato, y agrupar esos datos de forma individual
Parametros: 
(String) - text: linea a estructurar
Devolucion: 
- String : tipo de dato, nombre del dato, numero de Operacion de Estructuracion
"""
def dataIdentifyTypeToName(text): # ------------------------------- Operacion 2
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


"""
dataIdentifyNameToValue es un metodo dedicado a la lectura de una linea para
 detectar el patron especifico: nombre Dato y valor del dato, y agrupar esos datos de forma individual
Parametros: 
(String) - text: linea a estructurar
Devolucion: 
- String : nombre del dato,valor del dato, numero de Operacion de Estructuracion
"""
def dataIdentifyNameToValue(text): # ------------------------------- Operacion 3
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

"""
dataIdentifyNameToValue es un metodo dedicado a la lectura de una linea para
 detectar el patron especifico: nombre Dato y valor del dato, y agrupar esos datos de forma individual
Parametros: 
(String) - text: linea a estructurar
Devolucion: 
- String : nombre del dato,valor del dato, numero de Operacion de Estructuracion
"""
def dataIdentifyNameToName(text): # ------------------------------- Operacion 4
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
"""
dataIdentifyWithParenthesis es un metodo dedicado a la lectura de una linea para
 detectar el patron especifico: tipo de dato, nombre de funcion y parametros, y agrupar esos datos de forma individual
Parametros: 
(String) - text: linea a estructurar
Devolucion: 
- String : tipo de dato, nombre del dato, parametros, numero de Operacion de Estructuracion
"""
#tipo nombreFuncion(parametros) {
def dataIdentifyWithParenthesis(text): # ------------------------------- Operacion 5
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

"""
find_closing_brace es un metodo dedicado a la lectura de una linea para
 detectar si dentro de esa linea hay una llave de cierre
(String) - text: linea a leer
Devolucion: 
- String : Numero de Operacion de Estructuracion
"""
def find_closing_brace(line): # ------------------------------- Operacion 8
    if "}" in line:
        closing_brace_index = line.index("}")
        rest_of_line = line[closing_brace_index + 1:].strip()
        
        if rest_of_line == "":
            return "8"
        else:
            return None
    else:
        return None


def variablesDeLasFunciones(text): 
    parameters=[]
    line = text
    
    lineWords =  re.split('\s*,\s*|\s+', line)
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

"""
dataNametoOperation es un metodo dedicado a la lectura de una linea para
 detectar el patron especifico: nombre Dato y operaciones, y agrupar esos datos de forma individual
Parametros: 
(String) - text: linea a estructurar
Devolucion: 
- String : nombre del dato, numero de Operacion de Estructuracion
- Lista: Lista de los caracteres separadls por una operacion matematica
"""
def dataNametoOperation(text): # ------------------------------- Operacion 6
    try:
        patron = r"(\w+)\s*=\s*(([\w.]+(\s*[\+\-\*/]\s*[\w.]+)+))"
        resultado = re.search(patron, text)
        if resultado and resultado.start() == 0:
            dato = resultado.group(1)
            operacion = resultado.group(2)
            if not re.match(r'^[\w.]+(\s*[\+\-\*/]\s*[\w.]+)+$', operacion):
                return None
            operandos = re.split(r'\s*[\+\-\*/]\s*', operacion)
            return dato, operandos, "6"  
        else:
            return None
    except Exception:
        return None
    
"""
dataTypeNameToOperation es un metodo dedicado a la lectura de una linea para
 detectar el patron especifico: tipo de dato, nombre Dato y operaciones, y agrupar esos datos de forma individual
Parametros: 
(String) - text: linea a estructurar
Devolucion: 
- String : tipo de dato, nombre del dato, numero de Operacion de Estructuracion
- Lista: Lista de los caracteres separadls por una operacion matematica
"""
def dataTypeNameToOperation(text):# ------------------------------- Operacion 9
    try:
        patron = r"(\w+)\s+(\w+)\s*=\s*(([\w.]+(\s*[\+\-\*/]\s*[\w.]+)+))"
        resultado = re.search(patron, text)
        if resultado and resultado.start() == 0:
            dataType = resultado.group(1)
            nameData = resultado.group(2)
            operators = resultado.group(3)
            if not re.match(r'^[\w.]+(\s*[\+\-\*/]\s*[\w.]+)+$', operators):
                return None
            operators = re.split(r'\s*[\+\-\*/]\s*', operators)
            return dataType, nameData, operators, "9"  
        else:
            return None
    except Exception:
        return None

"""
conditionalDetection es un metodo dedicado a la lectura de una linea para
 detectar el patron especifico: if, valores a comparar, y agrupar esos datos de forma individual
Parametros: 
(String) - text: linea a estructurar
Devolucion: 
- String : if, valor 1, valor 2, numero de Operacion de Estructuracion
"""
def conditionalDetection(text):# ------------------------------- Operacion 10
    try: 
        patron = r"^\s*if\s*\(\s*(\w+)\s*([<>]=?|==|!=)\s*(\w+)\s*\)\s*{?$"
        resultado = re.search(patron, text) 
        if resultado: 
            value1 = resultado.group(1) 
            value2 = resultado.group(3) 
            return "if", value1, value2,"10" 
        else: 
            return None 
    except Exception: 
        return None 

"""
loopDetection es un metodo dedicado a la lectura de una linea para
 detectar el patron especifico: while, valores a comparar, y agrupar esos datos de forma individual
Parametros: 
(String) - text: linea a estructurar
Devolucion: 
- String : while, valor 1, valor 2, numero de Operacion de Estructuracion
"""
def loopDetection(text): # ------------------------------- Operacion 11
    try:
        patron = r"^\s*while\s*\(\s*(\w+)\s*([<>]=?|==|!=)\s*(\w+)\s*\)\s*{?$"
        resultado = re.search(patron, text)
        if resultado:
            value1 = resultado.group(1)
            value2 = resultado.group(3)
            return "while", value1, value2,"11"
        else:
            return None
    except Exception:
        return None

"""
dataToNameToFunction es un metodo dedicado a la lectura de una linea para
 detectar el patron especifico: tipo de dato, nombre de dato, nombre de funcion, parametros, y agrupar esos datos de forma individual
Parametros: 
(String) - text: linea a estructurar
Devolucion: 
- String : tipo de dato, nombre da dato, nombre de funcion, parametros de la funcion, numero de Operacion de Estructuracion
"""
def dataToNameToFunction(text): # ------------------------------- Operacion 12
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

"""
nameToFunction es un metodo dedicado a la lectura de una linea para
 detectar el patron especifico: nombre de dato, nombre de funcion, parametros de funcion, y agrupar esos datos de forma individual
Parametros: 
(String) - text: linea a estructurar
Devolucion: 
- String : nombre de dato, nombre de funcion, parametros de funcion, numero de Operacion de Estructuracion
"""
def nameToFunction(text): # ------------------------------- Operacion 13
    pattern = r"(\w+)\s*=\s*(\w+)\s*\(\s*(.*?)\s*\)"
    match = re.match(pattern, text)
    if match:
        variable_name = match.group(1)
        function_name = match.group(2)
        params_string = match.group(3)
        return variable_name, function_name, params_string, "13"
    else:
        return None
"""
returnDetect es un metodo dedicado a la lectura de una linea para
 detectar el patron especifico: return, lista de valores sea un unico valor o una operacion, y agrupar esos datos de forma individual
Parametros: 
(String) - text: linea a estructurar
Devolucion: 
- String : return, nombre de funcion, numero de Operacion de Estructuracion
- Lista : Lista de valores sea un unico valor o una operacion
"""
def returnDetect(text): # ------------------------------- Operacion 14
    try:
        patron = r"^\s*return\s+(['\"]?\w+['\"]?\s*[\+\-\*/]\s*(['\"]?\w+['\"]?)*)\s*$"
        resultado = re.search(patron, text)
        if resultado:
            expresion = resultado.group(1)
            # Verificar que no haya palabras antes o después del return y que los valores estén separados por operadores
            if re.match(r"^['\"]?\w+['\"]?(\s*[\+\-\*/]\s*['\"]?\w+['\"]?)*$", expresion):
                # Eliminar espacios en blanco de cada elemento antes de agregarlo a la lista
                valores = [valor.strip() for valor in re.split(r'[\+\-\*/]', expresion)]
                return valores, "14"
        return None
    except Exception:
        return None
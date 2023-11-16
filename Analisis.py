#Analisis Semantico
import re

tiposDatos = {'int' :(), 'float':(), 'string': (), 'void':() }
diccionarioGen = {}

"""
def tipoDato(word,dato): 
    
    if word in tiposDatos and isinstance(dato, tiposDatos[word]): 
        return "word"+str(dato)
    else: 
        return "error"
"""

def isTipo(word):
    if word in tiposDatos:
        return True
    else:  
        return False

def validateInt(value): 
    try: 
        int(value)
        return True
    except ValueError: 
        return False

def validateFloat(value): 
    try:
        float(value)
    except ValueError:
        return False
    else:
        return float(value) != int(float(value))
    
def validateString(word):
    if word[len(word)-1] == '"' and word[0]=='"':
        return True
    else:
        return False

def validateGeneral(tipo, valor):
    if tipo == "int": 
        return validateInt(valor)
    elif tipo == "float": 
        return validateFloat(valor)
    elif tipo == "string":
        return validateString(valor)
    else:
        return False

def addVariableGen(name,type): 
    diccionarioGen[name]= ("var",type)
# [0] es para "var", [1] para el tipo de variable
def addFunctionGen(name,type): 
    diccionarioGen[name] = ("fun",type, {})
#[0] es para "fun", [1] para tipo de funcion, [2] para subdiccionario donde se almacenan variables locales

def addVarFunction(nameFun, nameVar, type): 
    diccionarioGen[nameFun][2][nameVar]= (type)

def addReturnVal(nameFun): 
    diccionarioGen[nameFun][2]["return"]= (diccionarioGen[nameFun][1])

def KeyEnDiccionario(word):
    if word in diccionarioGen:
        return True
    else: 
        return False

def AllSearch(word): 
    prove = " "
    for key in diccionarioGen.keys():
        prove = diccionarioGen[key][0]
        if key == word:
            return True
        if diccionarioGen[key][0] == "fun":
            if KeyInFunction(key,word) == True:
                return True
    return False                

def KeyInFunction(funName, key):
    if key in diccionarioGen[funName][2]:
        return True
    else:
        return False

def TipoVarEnDiccionario(key):
    return  diccionarioGen[key][1]
    
def TipoValFuncionEnDiccionario(funName,key):
    return diccionarioGen[funName][2][key][1]



    
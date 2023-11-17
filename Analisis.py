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
def addIfGen():
    diccionarioGen["if"]=({})
#[0] es para subdiccionario

def addWhileGen():
    diccionarioGen["while"]=({})
#[0] es para subdiccionario

def addVarFunction(nameFun, nameVar, type): 
    diccionarioGen[nameFun][2][nameVar]= (type)


def addIfFunction(nameFun):
    diccionarioGen[nameFun][2]["if"]=({})
def addWhileFunction(nameFun):
    diccionarioGen[nameFun][2]["while"]=({})

def addVarIfGen(var,type):
    diccionarioGen["if"][var]=(type)
def addVarWhileGen(var,type):
    diccionarioGen["while"][var]=(type)

def addVarIfFun(funName,var,type):
    diccionarioGen[funName][2]["if"][var]=(type)

def addVarWhileFun(funName,var,type):
    diccionarioGen[funName][2]["while"][var]=(type)


#Accesos a valores if o while 
def accesIfGenValues(var):
    return diccionarioGen["if"][var]
def accesWhileGenValues(var):
    return diccionarioGen["while"][var]
def accesIfFuncValues(funName,var):
    return diccionarioGen[funName][2]["if"][var]

def accesWhileFuncValues(funName,var):
    return diccionarioGen[funName][2]["while"][var]


def addReturnVal(nameFun): 
    diccionarioGen[nameFun][2]["return"]= (diccionarioGen[nameFun][1])

def KeyInDiccionario(word):
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

def keyInIfGen(key):
    if key in diccionarioGen["if"]:
       return True
    else:
        return False       
def keyInWhileGen(key):
    if key in diccionarioGen["while"]:
        return True
    else:
        return False

def keyInIfFunc(funName,key):
    if key in diccionarioGen[funName][2]["if"]:
        return True
    else:
        return False

def keyInWhileFunc(funName,key):
    if key in diccionarioGen[funName][2]["while"]:
        return True
    else:
        return False
def TipoVarEnDiccionario(key):
    return  diccionarioGen[key][1]
    
def TipoValFuncionEnDiccionario(funName,key):
    return diccionarioGen[funName][2][key][1]

def insertValuesToFunction(nameFunction, values, numLine):
    i = 0
    while i < len(values):
        tipo = values[i]
        dato = values[i+1]
        if i+2 < len(values):
            posiblevalor = values[i+2]
            if isTipo(posiblevalor):
                if KeyInDiccionario(dato):
                    print("\nError en la linea "+str(numLine)+" El nombre de la variable '" + dato + "' ya existe\n")
                    i+=2
                elif KeyInFunction(nameFunction,dato):
                    print("\nError en la linea "+str(numLine)+" El nombre de la variable '" + dato + "' ya existe en la funcion\n")
                    i+=2      
                else:
                    addVarFunction(nameFunction,dato,tipo)
                    i+=2
            elif validateGeneral(tipo,posiblevalor):
                addVarFunction(nameFunction,dato,tipo)
                i+=3
            else:
                print("\nError en la linea "+str(numLine)+" El tipo de la variable '" + dato + "' no es compatible con su dato\n")
                i+=1
        elif isTipo(tipo):
            if KeyInDiccionario(dato):
                print("\nError en la linea "+str(numLine)+" El nombre de la variable '" + dato + "' ya existe\n")
                i+=2
            elif KeyInFunction(nameFunction,dato):
                print("\nError en la linea "+str(numLine)+" El nombre de la variable '" + dato + "' ya existe en la funcion\n")
                i+=2      
            else:
                addVarFunction(nameFunction,dato,tipo)
                i+=2
        else:
            print("\nError en la linea "+str(numLine)+" El tipo de variable '" + tipo + "' no es aceptado\n")
            i+=2

addVariableGen("a",'int')
addFunctionGen("sumar",'int')
lista = ['int','b','int','c','int','o','oo','string','nombre']
insertValuesToFunction("sumar",lista,1)

#addIfGen()
#addWhileGen()

#addVarWhileGen("messi","int")
#addVarIfGen("Cristiano","void")


#addFunctionGen("main","void")

#addIfFunction("main")
#addWhileFunction("main")



#addVarIfFun("main","diaz","float")
#addVarWhileFun("main","gabo","string")

#print(accesIfFuncValues("main","diaz"))
#print(accesWhileFuncValues("main","gabo"))
#print(accesIfGenValues("Cristiano"))
#print(accesWhileGenValues("messi"))

#print(keyInIfGen("Cristian"))
#print(keyInWhileGen("mess"))

#print(keyInIfFunc("main","dias"))
#print(keyInWhileFunc("main","gab"))



    
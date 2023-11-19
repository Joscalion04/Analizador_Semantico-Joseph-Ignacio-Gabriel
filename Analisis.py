#Analisis Semantico
import re
#Diccionario con los tipos de variables permitidas 
tiposDatos = {'int' :(), 'float':(), 'string': (), 'void':() }
#Diccionario General 
diccionarioGen = {}


#Metodos encargados de verificar si un tipo es 
#permitido o no, esto haciendo uso del diccionario tiposDatos
def isTipo(word):
    if word in tiposDatos:
        return True
    else:  
        return False

#Validates de los tipos de variable permitidas (int, float, string)
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
    patron = r"\s*('[^']*'|\"[^\"]*\")\s*$"
    resultado =  re.search(patron, word)
    if resultado:
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


#Funcion que con ayuda de la funcion verificationTypeVar y en 
# base a un vector de nombres o valores
#verifica que todos los datos del vector sean de un mismo 
# tipo previamente declarado
def verificateTypes(type, operations, functionName, lineNum):
    for operation in operations:
        if verificationTypeVar(type,operation,functionName, lineNum) == 3:
            if validateGeneral(type, operation) == False:
                print("Linea " + str(lineNum) + " Error: La variable " + str(operation) + " no es un valor valido")

#Verifica que el tipo de la variable es correcto, en caso de no ser una variable retorna un 3 para 
# que el metodo verificateTypes verifique el tipo del valor 
def verificationTypeVar(type, name, functionName, linenum): 
    if KeyInDiccionario(name): 
        if type != TipoVarEnDiccionario(name):
            print("Linea " + str(linenum) + " Error: La variable " + str(name) + " no es un valor valido")
            return 1
        else:
           return 2
    elif keyInIfGen(name)==True:
        if type!=accesIfGenValues(name):
            print ("Linea "+str(linenum)+" Error: La variable "+str(name)+" no es un valor valido")
            return 1
        else:
            return 2
    elif keyInWhileGen(name)==True:
        if type!=accesWhileGenValues(name):
            print ("Linea "+str(linenum)+" Error: La variable "+str(name)+" no es un valor valido")
        else:
            return 2
    elif functionName != None:
        if KeyInFunction(functionName,name) == True:
            if type != TipoValFuncionEnDiccionario(functionName, name): 
                print("Linea " + str(linenum) + " Error: La variable " + str(name) + " no es un valor valido")
                return 1 
        elif keyInIfFunc(functionName,name)==True:
            if type != accesIfFuncValues(functionName,name):
                print ("Linea "+str(linenum)+" Error: La variable "+str(name)+" no es un valor valido")
                return 1
            else: 
                return 2
        elif keyInWhileFunc(functionName,name)==True:
            if type != accesWhileFuncValues(functionName,name):
                print ("Linea "+str(linenum)+" Error: La variable "+str(name)+" no es un valor valido")
                return 1
            else: 
                return 2
    else: 
        return 3        

#Metodos para agregar datos al diccionario General
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

#Metodos para agregar datos a una funcion
def addVarFunction(nameFun, nameVar, type): 
    diccionarioGen[nameFun][2][nameVar]= (type)


def addIfFunction(nameFun):
    diccionarioGen[nameFun][2]["if"]=({})
def addWhileFunction(nameFun):
    diccionarioGen[nameFun][2]["while"]=({})

#Metodos para agregar datos a los if o while que NO esten en una funcion
def addVarIfGen(var,type):
    diccionarioGen["if"][var]=(type)
def addVarWhileGen(var,type):
    diccionarioGen["while"][var]=(type)

#Metodos para agregar datos a los if o while que estan en una funcion
def addVarIfFun(funName,var,type):
    diccionarioGen[funName][2]["if"][var]=(type)

def addVarWhileFun(funName,var,type):
    diccionarioGen[funName][2]["while"][var]=(type)


#Accesos a valores if o while 
def accesIfGenValues(var):
    return diccionarioGen["if"][var]
def accesWhileGenValues(var):
    return diccionarioGen["while"][var]

#Accesos a valores de una variable dentro de una funcion y un if o while
def accesIfFuncValues(funName,var):
    return diccionarioGen[funName][2]["if"][var]

def accesWhileFuncValues(funName,var):
    return diccionarioGen[funName][2]["while"][var]

#Metodo para añadir el tipo del return de una funcion
def addReturnVal(nameFun): 
    diccionarioGen[nameFun][2]["return"]= (diccionarioGen[nameFun][1])

#Metodo para verificar si una variable global o funcion esta en el diccionario
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

#Metodo que verifica que una llave (nombre de una variable) este en una funcion
def KeyInFunction(funName, key):
    if key in diccionarioGen[funName][2]:
        return True
    else:
        return False

#Metodo que verifica que una llave (nombre de una variable) este en un If
def keyInIfGen(key):
    if key in diccionarioGen["if"]:
       return True
    else:
        return False       
    
#Metodo que verifica que una llave (nombre de una variable) este en un while  
def keyInWhileGen(key):
    if key in diccionarioGen["while"]:
        return True
    else:
        return False

#Metodo que verifica que una llave (nombre de una variable) este en un If que esta dentro de 
# una funcion
def keyInIfFunc(funName,key):
    if key in diccionarioGen[funName][2]["if"]:
        return True
    else:
        return False

#Metodo que verifica que una llave (nombre de una variable) este en un While que esta dentro de 
#una funcion
def keyInWhileFunc(funName,key):
    if key in diccionarioGen[funName][2]["while"]:
        return True
    else:
        return False

#Metodo que devuelve el tipo de una variable
def TipoVarEnDiccionario(key):
    return  diccionarioGen[key][1]

#Metodo que devuelve el tipo de una variable que esta dentro de una funncion
def TipoValFuncionEnDiccionario(funName,key):
    return diccionarioGen[funName][2][key]

def insertValuesToFunction(nameFunction, values, numLine):
    i = 0
    while i < len(values):
        tipo = values[i]
        dato = values[i+1]
        if i+2 < len(values):
            posiblevalor = values[i+2]
            if isTipo(posiblevalor):
                if KeyInDiccionario(dato):
                    print("Error en la linea "+str(numLine)+" El nombre de la variable '" + dato + "' ya existe\n")
                    break
                elif KeyInFunction(nameFunction,dato):
                    print("Error en la linea "+str(numLine)+" El nombre de la variable '" + dato + "' ya existe en la funcion\n")
                    break      
                elif not isTipo(tipo):
                    print("Error en la linea "+str(numLine)+" El tipo de variable '" + tipo + "' no es aceptado\n")
                    break
                else:
                    addVarFunction(nameFunction,dato,tipo)
                    i+=2
            elif not isTipo(tipo):
                print("Error en la linea "+str(numLine)+" El tipo de variable '" + tipo + "' no es aceptado\n")
                break
            elif KeyInDiccionario(dato):
                print("Error en la linea "+str(numLine)+" El nombre de la variable '" + dato + "' ya existe\n")
                break
            elif KeyInDiccionario(posiblevalor):
                if TipoVarEnDiccionario(posiblevalor) == tipo:
                    addVarFunction(nameFunction,dato,tipo)
                    i+=3
                else:
                    print("Error en la linea "+str(numLine)+" El tipo de la variable '" + dato + "' no es compatible con su dato\n")
                    break
            elif validateGeneral(tipo,posiblevalor):
                addVarFunction(nameFunction,dato,tipo)
                i+=3
            else:
                print("Error en la linea "+str(numLine)+" El tipo de la variable '" + dato + "' no es compatible con su dato")
                break
        elif isTipo(tipo):
            if KeyInDiccionario(dato):
                print("Error en la linea "+str(numLine)+" El nombre de la variable '" + dato + "' ya existe\n")
                break
            elif KeyInFunction(nameFunction,dato):
                print("Error en la linea "+str(numLine)+" El nombre de la variable '" + dato + "' ya existe en la funcion\n")
                break      
            else:
                addVarFunction(nameFunction,dato,tipo)
                i+=2
        else:
            print("Error en la linea "+str(numLine)+" El tipo de variable '" + tipo + "' no es aceptado\n")
            break

def validateReturnValuesFunction(nameFunction, values, numLine):
    for value in values:
        if KeyInFunction(nameFunction,value):
           if TipoValFuncionEnDiccionario(nameFunction,value) != TipoVarEnDiccionario(nameFunction):
              print("Linea " + str(numLine) + " Error: La variable '" + str(value) + "' no es un valor de retorno correcto")
              break
        elif KeyInDiccionario(value):
            if TipoVarEnDiccionario(value)  != TipoVarEnDiccionario(nameFunction):
                print("Linea " + str(numLine) + " Error: La variable '" + str(value) + "' no es un valor de retorno correcto")
                break
        elif validateString(value):
            if TipoVarEnDiccionario(nameFunction) != 'string':
                print("Linea " + str(numLine) + " Error: La variable '" + str(value) + "' no es un valor de retorno correcto")
                break
        elif validateFloat(value):
            if TipoVarEnDiccionario(nameFunction) != 'float':
                print("Linea " + str(numLine) + " Error: La variable '" + str(value) + "' no es un valor de retorno correcto")
                break   
        elif validateInt(value):
            if TipoVarEnDiccionario(nameFunction) != 'int':
                print("Linea " + str(numLine) + " Error: La variable '" + str(value) + "' no es un valor de retorno correcto")
                break 


import Lectura

addVariableGen("aux",'int')
addFunctionGen("sumar",'int')
lista = ['string','a','string','b']
insertValuesToFunction("sumar",lista,1)

linea = 'return a + 32'
retornos,op = Lectura.returnDetect(linea)
validateReturnValuesFunction("sumar",retornos,2)

#addVariableGen("a",'int')
#addFunctionGen("sumar",'int')
#lista = ['int','b','x','int','c','int','o','32','string','nombre']
#insertValuesToFunction("sumar",lista,1)


#addVariableGen("uno","string")
#addVariableGen("dos","int")
#addVariableGen("tres","int")

#addFunctionGen("messi","void")
#addVarFunction("messi","cuatro","int")

#addIfGen()
#addIfFunction("messi")

#addVarIfGen("cinco","int")
#addVarIfFun("messi","seis","int")
#addWhileGen()
#addWhileFunction("messi")

#addVarWhileGen("siete","int")
#addVarWhileFun("messi","ocho","string")



#Operations=["uno","dos","tres","cuatro","cinco","seis","siete","ocho"]
#verificateTypes("int",Operations,"messi",2)
#print(TipoValFuncionEnDiccionario("messi","cuatro"))
#print(validateString('"pronar"   \t '))


    
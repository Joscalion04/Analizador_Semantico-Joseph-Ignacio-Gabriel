#Analisis Semantico
import re
#Diccionario con los tipos de variables permitidas 
tiposDatos = {'int' :(), 'float':(), 'string': (), 'void':() }
#Diccionario General 
diccionarioGen = {}

"""
Metodos encargados de verificar si un tipo es 
permitido o no, esto haciendo uso del diccionario tiposDatos

Parametros: 
-word(string): tipo de dato de una variable o tipo de retorno de una funcion

Devolucion: 
boolean: true-> el tipo es permitido, false-> el tipo no es permitido
"""
def isTipo(word):
    if word in tiposDatos:
        return True
    else:  
        return False
    
def isTipoVar(word):
    if word in tiposDatos and word !='void':
        return True
    else:
        return False

"""
Validaciones  para los tipos de variables permitidas

Parametros: 
-value (string): valor que se desea validar

Devolucion: 
-boolean: true-> el valor corresponde con el tipo , false-> el valor no corresponde con el tipo 
"""
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

"""
Metodo que utilizando los metodos validateInt, validateFloat, validateString valida que el valor 
corresponde con el tipo, tanto el valor como el tipo entran como parametro

Parametros: 
-tipo(string): tipo de dato de una variable o tipo de retorno de una funcion
-valor(string): valor que se desea validar
Devolucion: 
boolean: true-> el tipo de dato es correcto para el valor , false-> el tipo de dato no es correcto para el valor 
"""
def validateGeneral(tipo, valor):
    if tipo == "int": 
        return validateInt(valor)
    elif tipo == "float": 
        return validateFloat(valor)
    elif tipo == "string":
        return validateString(valor)
    else:
        return False

"""
Funcion que con ayuda de la funcion verificationTypeVar y en base a una lista de variables o valores
verifica que todos los datos del vector sean de un mismo tipo previamente declarado
Parametros: 
-type (string): tipo de dato usado como criterio para verificar 
-operations (lista): lista con los valores o variables a comparar 
-functionName(string o null): nombre de posible funcion
-lineNum(int): numero de linea que se esta procesando

Devolucion: 
string o none: imprime el error que detecto o no imprime nada si no hay error 
"""
def verificateTypes(type, operations, functionName, lineNum):
    for operation in operations:
        if verificationTypeVar(type,operation,functionName, lineNum) == 3:
            if validateGeneral(type, operation) == False:
                print("Linea " + str(lineNum) + " Error: La variable " + str(operation) + " no es un valor valido")


"""
Funcion que verifica el tipo de una variable sea correcto 
Parametros: 
-type (string): tipo de dato usado como criterio para verificar 
-name(string): nombre de la variable que se desea verificar
-functionName(string o null): nombre de posible funcion
-lineNum(int): numero de linea que se esta procesando

Devolucion: 
string o int : imprime el error que detecto o retorna un 3 para que la funcion verificateTypes
verifique el dato como un valor y no como una variable
"""
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
    else: 
        return 3        

"""
addVariableGen, addFunctionGen, son metodos para agregar variables o funciones al diccionario General
Parametros: 
-name(string): nombre de la variable 
-type(string): tipo de la variable 

Devolucion: 
-None
"""
def addVariableGen(name,type): 
    diccionarioGen[name]= ("var",type)
# [0] es para "var", [1] para el tipo de variable
def addFunctionGen(name,type): 
    diccionarioGen[name] = ("fun",type, {})
#[0] es para "fun", [1] para tipo de funcion, [2] para subdiccionario donde se almacenan variables locales
"""
 addIfGen, addWhileGen, son metodos para agregar if o while al diccionario General
Parametros: 
-None

Devolucion: 
-None
"""
def addIfGen():
    diccionarioGen["if"]=({})
#[0] es para subdiccionario

def addWhileGen():
    diccionarioGen["while"]=({})
#[0] es para subdiccionario

"""
addVarFunction metodo para agregar variables a funciones
Parametros: 
-nameFun(string): nombre de la funcion donde se quiere ingresar la variable
-nameVar(string): nombre de la variable 
-type(string): tipo de la variable 

Devolucion: 
-None
"""
def addVarFunction(nameFun, nameVar, type): 
    diccionarioGen[nameFun][2][nameVar]= (type)

"""
metodo para agregar if a funciones
Parametros: 
-nameFun(string): nombre de la funcion donde se quiere ingresar la variable
Devolucion: 
-None
"""
def addIfFunction(nameFun):
    diccionarioGen[nameFun][2]["if"]=({})


"""
metodo para agregar while a funciones
Parametros: 
-nameFun(string): nombre de la funcion donde se quiere ingresar la variable
Devolucion: 
-None
"""
def addWhileFunction(nameFun):
    diccionarioGen[nameFun][2]["while"]=({})

"""
 addVarIfGen y addVarWhileGen son metodos para agregar variables a los if o while que no se encuentren dentor de una funcion
Parametros: 
-name(string): nombre de la variable 
-type(string): tipo de la variable 
Devolucion: 
-None
"""
def addVarIfGen(var,type):
    diccionarioGen["if"][var]=(type)
def addVarWhileGen(var,type):
    diccionarioGen["while"][var]=(type)

"""
 addVarIfFun y addVarWhileFun son metodos para agregar variables a los if o while que se encuentren dentor de una funcion
Parametros: 
-nameFun(string): nombre de la función donde se encuentra el if o while
-name(string): nombre de la variable 
-type(string): tipo de la variable 
Devolucion: 
-None
"""
def addVarIfFun(funName,var,type):
    diccionarioGen[funName][2]["if"][var]=(type)

def addVarWhileFun(funName,var,type):
    diccionarioGen[funName][2]["while"][var]=(type)


"""
 accesIfGenValues y accesWhileGenValues son metodos para acceder al tipo de una variable de un if o while que no se encuentren dentor de una funcion
Parametros: 
-var(string): nombre de la variable 
Devolucion: 
-None
"""
def accesIfGenValues(var):
    return diccionarioGen["if"][var]
def accesWhileGenValues(var):
    return diccionarioGen["while"][var]

"""
 accesIfFuncValues y accesWhileFuncValues son metodos para acceder al tipo de una variable de un if o while que se encuentren dentor de una funcion
Parametros: 
-funName(string): Nombre de la funcion donde se encuentra el if o el while
-var(string): nombre de la variable 
Devolucion: 
-None
"""
def accesIfFuncValues(funName,var):
    return diccionarioGen[funName][2]["if"][var]

def accesWhileFuncValues(funName,var):
    return diccionarioGen[funName][2]["while"][var]

"""
 Metodo para agregar el tipo de return de una funcion
Parametros: 
-funName(string): Nombre de la funcion
Devolucion: 
-None
"""
def addReturnVal(nameFun): 
    diccionarioGen[nameFun][2]["return"]= (diccionarioGen[nameFun][1])

"""
 metodo que verifica si una variable global o funcion existe 
Parametros: 
-word(string): Nombre de la funcion o varable
Devolucion: 
-boolean: True->Existe, False->No existe
"""
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

"""
 metodo que verifica si una variable esta en una funcion 
Parametros: 
-key(string): Nombre de la funcion o varable
-funName(string): Nombre de la funcion
Devolucion: 
-boolean: True->Existe, False->No existe
"""
def KeyInFunction(funName, key):
    if key in diccionarioGen[funName][2]:
        return True
    else:
        return False

"""
keyInIfGen y keyInWhileGen son metodos que verifican si una variable esta en un If o while que no 
se encuentra dentro de una funcion  
Parametros: 
-key(string): Nombre de la varable
Devolucion: 
-boolean: True->Existe, False->No existe
"""
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

"""
keyInIfGen y keyInWhileGen son metodos que verifican si una variable esta en un If o while que 
se encuentra dentro de una funcion  
Parametros: 
-key(string): Nombre de la varable
Devolucion: 
-boolean: True->Existe, False->No existe
"""
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

"""
Metodo que retorna el tipo de una variable global 
Parametros: 
-key(string): Nombre de la varable
Devolucion: 
-string: tipo de la variable
"""
def TipoVarEnDiccionario(key):
    return  diccionarioGen[key][1]
"""
Metodo que devuelve el tipo de una variable que esta dentro de una funncion 
Parametros: 
-key(string): Nombre de la varable
Devolucion: 
-string: tipo de la variable
"""
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


addVariableGen("uno","int")
addVariableGen("dos","int")
addVariableGen("tres","int")

addFunctionGen("messi","void")
addVarFunction("messi","cuatro","int")

addIfGen()
addIfFunction("messi")

addVarIfGen("cinco","int")
addVarIfFun("messi","seis","int")
addWhileGen()
addWhileFunction("messi")

addVarWhileGen("siete","int")
addVarWhileFun("messi","ocho","int")



#Operations=["uno","3.9","'ou'","cuatro","5","seis","siete","8"]
#verificateTypes("string",Operations,"messi",2)
#print(isTipoVar('void'))
#print(TipoValFuncionEnDiccionario("messi","cuatro"))
#print(validateString('"pronar"   \t '))


    
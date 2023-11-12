#Analisis Semantico


tiposDatos = {'int' :(int,), 'float':(float,), 'string': (str,), 'void':(type(None),) }
diccionarioGen = {}

def tipoDato(word,dato): 
    
    if word in tiposDatos and isinstance(dato, tiposDatos[word]): 
        return "word"+str(dato)
    else: 
        return "error"

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
        return True
    except ValueError: 
        return False
    
def validateString(word):
    if word[len(word)-1] == '"' and word[0]=='"':
        return True
    else:
        return False

def addVariableGen(name,type,value): 
    diccionarioGen[name]= ("var",type,value)
# [0] es para "var", [1] para el tipo de variable, [2] para el valor que almacena 
def addFunctionGen(name,type): 
    diccionarioGen[name] = ("fun",type, {})
#[0] es para "fun", [1] para tipo de funcion, [2] para subdiccionario donde se almacenan variables locales

def addVarFunction(nameFun, nameVar, type, value): 
    diccionarioGen[nameFun][2][nameVar]= (type,value)

def addReturnVal(nameFun, value): 
    


addFunctionGen("prueba1", "int")
print(diccionarioGen)

print(diccionarioGen["prueba1"][2]["return"])


     

    
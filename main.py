#Proyecto 2, Estructura de Datos, Ignacio Bonilla - Joseph Leon - Gabriel Robleto  
import Lectura
import Analisis

def lectura(linea, num, operacion, function, functionName):
    tipo = ""
    nombre = ""
    valor = ""
    error = "Linea " + str(num) + " exitosa"

    

    try:
        tipo , nombre, valor, operacion = Lectura.dataIdentifyTypeToNameToValue(linea)
        if Analisis.isTipo(tipo) == False: 
            error = "Linea " + str(num) + " Error: "+ str(tipo) + " no es un tipo de dato aceptado"
        elif Analisis.validateGeneral(tipo,valor) == False: 
            error = "Linea " + str(num) + " Error: "+ str(valor) + " no es un dato aceptable para una variable de tipo " + str(tipo)
            if function ==True:
                if Analisis.KeyInFunction(functionName, nombre) == False:
                    Analisis.addVarFunction(functionName, nombre,tipo)
                else:
                    error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
            else: 
                if Analisis.KeyInDiccionario(nombre)==False:
                    Analisis.addVariableGen(nombre,tipo)
                else: 
                     error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
    except Exception: 
       print("linea sin poder leerse 1")
       pass

    try:
        tipo, nombre, operacion = Lectura.dataIdentifyTypeToName(line)
        if Analisis.isTipo(tipo) == False: 
            error = "Linea " + str(num) + " Error: "+ str(tipo) + " no es un tipo de dato aceptado"
        else: 
            if function ==True:
                if Analisis.KeyInFunction(functionName, nombre) == False:
                    Analisis.addVarFunction(functionName, nombre,tipo)
                else:
                    error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
            else: 
                if Analisis.KeyInDiccionario(nombre)==False:
                    Analisis.addVariableGen(nombre,tipo)
                else: 
                     error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
    except Exception: 
        print("linea sin poder leerse 2")
        pass  
    
    try:
        nombre, valor, operacion = Lectura.dataIdentifyNameToValue(line)
        if Analisis.KeyInDiccionario(nombre) == True: 
            if Analisis.validateGeneral(Analisis.TipoVarEnDiccionario(nombre),valor) == False:
                error = "Linea " + str(num) + " Error: "+ str(valor) + " no es un dato aceptable para una variable de tipo " + str(tipo)
        elif function == True: 
            if Analisis.KeyInFunction(functionName, nombre) == True:
                if Analisis.validateGeneral(Analisis.TipoValFuncionEnDiccionario(functionName, nombre)) == False:
                    error = "Linea " + str(num) + " Error: "+ str(valor) + " no es un dato aceptable para una variable de tipo " + str(tipo)
    except Exception:
        print("linea sin poder leerse 3")
        pass
  
    try:
        nombre, valor, operacion = Lectura.dataIdentifyNameToName(line)
        if Analisis.KeyInDiccionario(nombre) == True: 
            if Analisis.KeyInDiccionario(valor) == True:
                if Analisis.validateGeneral(Analisis.TipoVarEnDiccionario(nombre), Analisis.TipoVarEnDiccionario(valor)) == False:
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(valor) + " no son compatibles"
            elif function ==True:
                    if Analisis.KeyInFunction(functionName, valor) == True:
                        if Analisis.validateGeneral(Analisis.TipoVarEnDiccionario(nombre), Analisis.TipoValFuncionEnDiccionario(functionName,valor)) == False:
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(valor) + " no son compatibles"
            else: 
                error = "Linea " + str(num) + " Error: La variable " + str(valor) + "  no ha sido declarada"
        elif function == True:
            if Analisis.KeyInFunction(functionName, nombre) == True:
                if Analisis.KeyInDiccionario(valor) == True:
                    if Analisis.validateGeneral(Analisis.TipoValFuncionEnDiccionario(functionName,valor), Analisis.TipoVarEnDiccionario(valor)) == False:
                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(valor) + " no son compatibles"
                elif function ==True:
                    if Analisis.KeyInFunction(functionName, valor) == True:
                        if Analisis.validateGeneral(Analisis.TipoValFuncionEnDiccionario(functionName,valor), Analisis.TipoValFuncionEnDiccionario(functionName,valor)) == False:
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(valor) + " no son compatibles"
                else: 
                    error = "Linea " + str(num) + " Error: La variable " + str(valor) + "  no ha sido declarada"
        else : 
            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + "  no ha sido declarada"    
    except Exception:
        print("linea sin poder leerse 4")
        pass

    try: #Incompleto falta agregar el que hacer con los  parametros 
        tipo,nombre,parametros,operacion = Lectura.dataIdentifyWithParenthesis(line)
        if Analisis.isTipo(tipo) == False: 
            error = "Linea " + str(num) + " Error: "+ str(tipo) + " no es un tipo de dato aceptado"
        elif Analisis.KeyInDiccionario(nombre)==True:
            error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
        else: 
            Analisis.addFunctionGen(nombre,tipo)
            function=True
            functionName=nombre        
    except Exception:
        print("linea sin poder leerse 5")
        pass
    
    if Lectura.find_closing_brace(line) == "8": 
        function = False
        functionName=None
    else: 
        print("linea sin poder leerse 6")

    try: 
        nombre, operations, operacion = Lectura.dataNametoOperation(line)
        if Analisis.KeyInDiccionario(nombre) ==True:
            tipo = Analisis.TipoVarEnDiccionario(nombre)
            verificateTypes(tipo, operations, None, num)
        elif function == True:
            if Analisis.KeyInFunction(functionName, nombre):
                tipo = Analisis.TipoValFuncionEnDiccionario(functionName, nombre)
                verificateTypes(tipo, operations, functionName, num)
                

    except Exception:
        print("linea sin poder leerse 7")
        pass

    return error,operacion, function, functionName


def verificateTypes(type, operations, functionName, lineNum):
    for operation in operations:
        if verificationTypeVar(type,operation,functionName, lineNum) != False:
            if Analisis.validateGeneral(type, operation) == False:
                print("Linea " + str(lineNum) + "Error: La variable" + str(operation) + " no es un valor valido")

def verificationTypeVar(type, name, functionName, linenum): 
    if Analisis.KeyInDiccionario(name): 
        if type != Analisis.TipoVarEnDiccionario(name):
            print("Linea " + str(linenum) + "Error: La variable" + str(name) + " no es un valor valido")
            return False
    elif functionName != None:
        if Analisis.KeyInFunction(functionName,name) == True:
            if type != Analisis.TipoValFuncionEnDiccionario(functionName, name): 
                print("Linea " + str(linenum) + "Error: La variable" + str(name) + " no es un valor valido")
                return False
    else: 
        return True        

lineas = Lectura.read("Codigo.txt") 
numLine = 1 
operacion = ""
function = False
functionName = None
for line in lineas: 
    error, operacion, function, functionName = lectura(line,numLine, operacion,function, functionName)
    print(error)
    numLine += 1

print(Analisis.diccionarioGen)


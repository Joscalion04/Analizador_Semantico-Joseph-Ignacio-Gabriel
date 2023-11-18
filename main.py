#Proyecto 2, Estructura de Datos, Ignacio Bonilla - Joseph Leon - Gabriel Robleto  
import Lectura
import Analisis

def lectura(linea, num, operacion, function, functionName, conditional):
    tipo = ""
    nombre = ""
    valor = ""
    operations = None
    nombre2 = ""
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
        nombre, nombre2, operacion = Lectura.dataIdentifyNameToName(line) #Arreglar pq no esta verificando correctamente la comparacion de tipos 
        if Analisis.KeyInDiccionario(nombre) == True: 
            if Analisis.KeyInDiccionario(nombre2) == True:
                if Analisis.TipoVarEnDiccionario(nombre)!= Analisis.TipoVarEnDiccionario(nombre2) :
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
            elif function ==True:
                    if Analisis.KeyInFunction(functionName, nombre2) == True:
                        if Analisis.TipoVarEnDiccionario(nombre) != Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
            else: 
                error = "Linea " + str(num) + " Error: La variable " + str(valor) + "  no ha sido declarada"
        elif function == True:
            if Analisis.KeyInFunction(functionName, nombre) == True:
                if Analisis.KeyInDiccionario(valor) == True:
                    if Analisis.TipoValFuncionEnDiccionario(functionName,valor) != Analisis.TipoVarEnDiccionario(valor):
                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(valor) + " no son compatibles"
                elif function ==True:
                    if Analisis.KeyInFunction(functionName, valor) == True:
                        if Analisis.TipoValFuncionEnDiccionario(functionName,valor)!= Analisis.TipoValFuncionEnDiccionario(functionName,valor):
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
        nombre, operations, operacion = Lectura.dataNametoOperation(line) #Failing is cuting 22.6 and the next one too
        if Analisis.KeyInDiccionario(nombre) ==True:
            tipo = Analisis.TipoVarEnDiccionario(nombre)
            Analisis.verificateTypes(tipo, operations, functionName, num)
        elif function == True:
            if Analisis.KeyInFunction(functionName, nombre):
                tipo = Analisis.TipoValFuncionEnDiccionario(functionName, nombre)
                Analisis.verificateTypes(tipo, operations, functionName, num)
        else:
            error =  "Linea " + str(num) + " Error: "+ nombre + " no es una variable que haya sido declarada"
    except Exception:
        print("linea sin poder leerse 7")
        pass
    
    try:
        tipo, nombre, operations, operacion = Lectura.dataTypeNameToOperation(line)
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
        Analisis.verificateTypes(tipo, operations, functionName, num)
    except Exception:
        print("linea sin poder leerse 8")
        pass

    try:
        tipo, nombre, nombre2, operacion = Lectura.conditionalDetection(line)
        if Analisis.KeyInDiccionario(nombre) == True: 
            if Analisis.KeyInDiccionario(nombre2) == True:
                if Analisis.TipoVarEnDiccionario(nombre)!= Analisis.TipoVarEnDiccionario(nombre2) :
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
            elif function ==True:
                    if Analisis.KeyInFunction(functionName, nombre2) == True:
                        if Analisis.TipoVarEnDiccionario(nombre) != Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
            else: 
                error = "Linea " + str(num) + " Error: La variable " + str(valor) + "  no ha sido declarada"
        elif function == True:
            if Analisis.KeyInFunction(functionName, nombre) == True:
                if Analisis.KeyInDiccionario(valor) == True:
                    if Analisis.TipoValFuncionEnDiccionario(functionName,valor) != Analisis.TipoVarEnDiccionario(valor):
                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(valor) + " no son compatibles"
                elif function ==True:
                    if Analisis.KeyInFunction(functionName, valor) == True:
                        if Analisis.TipoValFuncionEnDiccionario(functionName,valor)!= Analisis.TipoValFuncionEnDiccionario(functionName,valor):
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(valor) + " no son compatibles"
                else: 
                    error = "Linea " + str(num) + " Error: La variable " + str(valor) + "  no ha sido declarada"
        else : 
            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + "  no ha sido declarada"   
        if function ==False:
            Analisis.addIfGen()
        elif function == True:
            Analisis.addIfFunction(functionName)
            conditional=True
    except Exception:
        print("linea sin poder leerse 9")
        pass

    return error,operacion, function, functionName, conditional



lineas = Lectura.read("Codigo.txt") 
numLine = 1 
operacion = ""
function = False
functionName = None
condLoop = False
for line in lineas: 
    error, operacion, function, functionName, conditional = lectura(line,numLine, operacion,function, functionName, condLoop )
    print(error)
    numLine += 1

print(Analisis.diccionarioGen)


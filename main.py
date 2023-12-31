#Proyecto 2, Estructura de Datos, Ignacio Bonilla - Joseph Leon - Gabriel Robleto  
import Lectura
import Analisis

"""
En caso de no compilar debido a la direccion del Codigo.txt, copiar la dirección relativa del archivo y pegarla en 
el parametro del metodo Lectura.read(aqui va la direccion) en la linea 877

Limitaciones del proyecto

No verifica los parametros de una funcion cuando esta se llama

bug si una funcion contiene 2 condiconales 


"""

def lectura(linea, num, operacion, function, functionName, conditional):
    tipo = ""
    nombre = ""
    valor = ""
    operations = None
    nombre2 = ""
    error = " "
    
    try:
        tipo , nombre, valor, operacion = Lectura.dataIdentifyTypeToNameToValue(linea)
        if Analisis.isTipo(tipo) == False and tipo !="return": 
            error = "Linea " + str(num) + " Error: "+ str(tipo) + " no es un tipo de dato aceptado"
        else: 
            if function ==True:
                if Analisis.KeyInFunction(functionName, nombre) == False:
                    if conditional == True:
                        if Analisis.KeyInFunction(functionName,"if")==True:
                            if Analisis.keyInIfFunc(functionName, nombre) == False and Analisis.KeyInDiccionario(nombre) == False and Analisis.KeyInFunction(functionName,nombre)==False:
                                Analisis.addVarIfFun(functionName, nombre, tipo)
                        elif Analisis.KeyInFunction(functionName,"while")==True:
                            if Analisis.keyInWhileFunc(functionName, nombre) == False and Analisis.KeyInDiccionario(nombre) == False and Analisis.KeyInFunction(functionName,nombre)==False:
                                Analisis.addVarWhileFun(functionName,nombre, tipo)
                        else: 
                            error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
                    else:
                        Analisis.addVarFunction(functionName, nombre,tipo)
            elif Analisis.validateGeneral(tipo,valor) == False: 
                error = "Linea " + str(num) + " Error: "+ str(valor) + " no es un dato aceptable para una variable de tipo " + str(tipo)
            if Analisis.KeyInDiccionario(nombre)==False:
                if conditional == True:
                    if Analisis.KeyInDiccionario("if")==True:
                        if Analisis.keyInIfGen(nombre)==False:
                            Analisis.addVarIfGen(nombre,tipo)
                        else:
                          error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
                    if Analisis.KeyInDiccionario("while")==True:
                        if Analisis.keyInWhileGen(nombre)==False:
                            Analisis.addVarWhileGen(nombre,tipo)
                        else:
                             error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
                else: 
                    Analisis.addVariableGen(nombre,tipo) 
            
            else:
                error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"                
    except Exception: 
       pass

    try:
        tipo, nombre, operacion = Lectura.dataIdentifyTypeToName(line)
        if Analisis.isTipo(tipo) == False and tipo !="return": 
            error = "Linea " + str(num) + " Error: "+ str(tipo) + " no es un tipo de dato aceptado"
            
        elif tipo!="return": 
            if function ==True:
                if Analisis.KeyInFunction(functionName, nombre) == False:
                    if conditional == True:
                        if Analisis.KeyInFunction(functionName,"if")==True:
                            if Analisis.keyInIfFunc(functionName, nombre) == False:
                                Analisis.addVarIfFun(functionName, nombre, tipo)
                            else: 
                               error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada" 
                        elif Analisis.KeyInFunction(functionName,"while")==True:
                            if Analisis.keyInWhileFunc(functionName, nombre) == False:
                                Analisis.addVarWhileFun(functionName,nombre, tipo)
                            else: 
                               error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada" 
                        else: 
                            error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
                    else:
                        Analisis.addVarFunction(functionName, nombre,tipo)
                else:
                    error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
            else: 
                if Analisis.KeyInDiccionario(nombre)==False:
                    if conditional == True:
                        if Analisis.KeyInDiccionario("while") ==True:
                            if Analisis.keyInWhileGen(nombre)==True:
                                if Analisis.keyInIfGen(nombre) == False:
                                    Analisis.addVarIfGen(nombre, tipo)
                        elif Analisis.KeyInDiccionario("if")==True:
                            if Analisis.keyInIfGen(nombre)==True:
                                if Analisis.keyInWhileGen(nombre) == False:
                                    Analisis.addVarWhileGen(nombre,tipo)
                        else: 
                            error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
                    else:
                        Analisis.addVariableGen(nombre,tipo)
                else: 
                    error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
    except Exception: 
        pass  
    
    try:
        nombre, valor, operacion = Lectura.dataIdentifyNameToValue(line)
        if Analisis.KeyInDiccionario(nombre) == True: 
            if Analisis.validateGeneral(Analisis.TipoVarEnDiccionario(nombre),valor) == False:
                error = "Linea " + str(num) + " Error: "+ str(valor) + " no es un dato aceptable para una variable de tipo " + str(Analisis.TipoVarEnDiccionario(nombre))
        elif function == True: 
            if Analisis.KeyInFunction(functionName, nombre) == True:
                if Analisis.validateGeneral(Analisis.TipoValFuncionEnDiccionario(functionName, nombre),valor) == False:
                    error = "Linea " + str(num) + " Error: "+ str(valor) + " no es un dato aceptable para una variable de tipo " + str(Analisis.TipoValFuncionEnDiccionario(functionName, nombre))
            elif conditional == True:
                if Analisis.KeyInFunction(functionName,"if")==True:
                    if Analisis.keyInIfFunc(functionName, nombre) == True:
                        if Analisis.validateGeneral(Analisis.accesIfFuncValues(functionName, nombre),valor) == False:
                            error = "Linea " + str(num) + " Error: "+ str(valor) + " no es un dato aceptable para una variable de tipo " + str(Analisis.accesIfFuncValues(functionName, nombre))
                elif Analisis.KeyInFunction(functionName,"while")==True:
                    if Analisis.keyInWhileFunc(functionName, nombre) == True:
                        if Analisis.validateGeneral(Analisis.accesWhileFuncValues(functionName, nombre),valor)==False:
                            error = "Linea " + str(num) + " Error: "+ str(valor) + " no es un dato aceptable para una variable de tipo " + str(Analisis.accesWhileFuncValues(functionName, nombre))
        elif conditional ==True:
            if Analisis.KeyInDiccionario("while") ==True:
                if Analisis.keyInWhileGen(nombre)==True:
                    if Analisis.keyInIfGen(nombre) == True:
                         if Analisis.validateGeneral(Analisis.accesIfGenValues(nombre),valor) == False:
                            error = "Linea " + str(num) + " Error: "+ str(valor) + " no es un dato aceptable para una variable de tipo " + str(tipo)
            elif Analisis.KeyInDiccionario("if")==True:
                if Analisis.keyInIfGen(nombre)==True:
                    if Analisis.keyInWhileGen(nombre) == True:
                        if Analisis.validateGeneral(Analisis.accesWhileGenValues(nombre),valor) ==False:
                            error = "Linea " + str(num) + " Error: "+ str(valor) + " no es un dato aceptable para una variable de tipo " + str(Analisis.accesWhileGenValues(nombre))
        else:
            error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que no ha sido declarada"
    except Exception:
        pass

  #ready if 
    try: #Revisar 
        nombre, nombre2, operacion = Lectura.dataIdentifyNameToName(line) 
        if Analisis.KeyInDiccionario(nombre) == True: 
            if Analisis.KeyInDiccionario(nombre2) == True:
                if Analisis.TipoVarEnDiccionario(nombre)!= Analisis.TipoVarEnDiccionario(nombre2) :
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
            elif conditional ==True: 
                if Analisis.KeyInDiccionario("if") ==True:
                    if Analisis.keyInIfGen(nombre2) == True :
                        if Analisis.TipoVarEnDiccionario(nombre) != Analisis.accesIfGenValues(nombre2):
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif Analisis.KeyInDiccionario("while") == True:
                    if Analisis.keyInWhileGen(nombre2) ==True:
                        if Analisis.TipoVarEnDiccionario(nombre) != Analisis.accesWhileGenValues(nombre2):
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"           
            elif function ==True:
                if Analisis.KeyInFunction(functionName, nombre2) == True:
                    if Analisis.TipoVarEnDiccionario(nombre) != Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif conditional == True:
                    if Analisis.KeyInFunction(functionName, "if")==True:
                        if Analisis.keyInIfFunc(functionName, nombre2) == True: 
                            if Analisis.TipoVarEnDiccionario(nombre) != Analisis.accesIfFuncValues(functionName, nombre2): 
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif Analisis.KeyInFunction(functionName, "while")==True: 
                        if Analisis.keyInWhileFunc(functionName, nombre2) == True:
                            if Analisis.TipoVarEnDiccionario(nombre) != Analisis.accesWhileFuncValues(functionName, nombre2):
                                 error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
            else: 
                error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
        elif function == True:
            if Analisis.KeyInFunction(functionName, nombre) == True:
                if Analisis.KeyInDiccionario(nombre2) == True:
                    if Analisis.TipoValFuncionEnDiccionario(functionName,nombre) != Analisis.TipoVarEnDiccionario(nombre2):
                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif conditional ==True: 
                    if Analisis.KeyInDiccionario("if"):
                        if Analisis.keyInIfGen(nombre2) == True :
                            if Analisis.TipoValFuncionEnDiccionario(nombre) != Analisis.accesIfGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif Analisis.KeyInDiccionario("while"): 
                        if Analisis.keyInWhileGen(nombre2) ==True:
                            if Analisis.TipoValFuncionEnDiccionario(nombre) != Analisis.accesWhileGenValues(nombre2): 
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif Analisis.KeyInFunction(functionName, nombre2) == True:
                        if Analisis.TipoValFuncionEnDiccionario(functionName,nombre)!= Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif conditional ==True: 
                    if Analisis.KeyInFunction(functionName, "if")==True:
                        if Analisis.keyInIfFunc(functionName, nombre2) == True:
                            if Analisis.TipoValFuncionEnDiccionario(functionName, nombre) != Analisis.accesIfFuncValues(functionName, nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif Analisis.KeyInFunction("while") ==True:
                        if Analisis.keyInWhileFunc(functionName,nombre2)==True:
                            if Analisis.TipoValFuncionEnDiccionario(functionName, nombre) != Analisis.accesWhileFuncValues(functionName,nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                else: 
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
            elif conditional == True: 
                if Analisis.KeyInFunction(functionName,"if") == True:
                    if Analisis.keyInIfFunc(functionName,nombre) == True:
                        if Analisis.KeyInDiccionario(nombre2) == True:
                            if Analisis.accesIfFuncValues(functionName,nombre) != Analisis.TipoVarEnDiccionario(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif Analisis.KeyInDiccionario("if")==True:
                            if Analisis.keyInIfGen(nombre2) == True :
                                if Analisis.accesIfFuncValues(functionName,nombre) != Analisis.accesIfGenValues(nombre2):
                                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif Analisis.KeyInDiccionario("while")==True: 
                            if Analisis.keyInWhileGen(nombre2):
                                if Analisis.accesIfFuncValues(functionName,nombre) != Analisis.accesWhileGenValues(nombre2):
                                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif function == True:
                            if Analisis.KeyInFunction(functionName, nombre2) == True:
                                if Analisis.accesIfFuncValues(functionName,nombre)!= Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                            elif Analisis.KeyInFunction(functionName, "if")==True:
                                if Analisis.keyInIfFunc(functionName, nombre2) == True:
                                    if Analisis.accesIfFuncValues(functionName, nombre) != Analisis.accesIfFuncValues(functionName, nombre2):
                                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                            elif Analisis.KeyInFunction(functionName, "while") == True:
                                if Analisis.keyInWhileFunc(functionName, nombre2) ==True:
                                    if Analisis.accesIfFuncValues(functionName, nombre) != Analisis.accesWhileFuncValues(functionName, nombre2):
                                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        else: 
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
                elif Analisis.KeyInFunction(functionName,"while") ==True:
                    if Analisis.keyInWhileFunc(functionName,nombre) == True:
                        if Analisis.KeyInDiccionario(nombre2) == True:
                            if Analisis.accesWhileFuncValues(functionName,nombre) != Analisis.TipoVarEnDiccionario(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif Analisis.keyInIfGen(nombre2) == True :
                            if Analisis.accesWhileFuncValues(nombre) != Analisis.accesIfGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif Analisis.KeyInFunction(functionName, nombre2) == True:
                            if Analisis.accesWhileFuncValues(functionName,nombre)!= Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif Analisis.KeyInFunction("if") == True:
                            if Analisis.keyInIfFunc(functionName, nombre2) == True:
                                if Analisis.accesWhileFuncValues(functionName, nombre) != Analisis.accesIfFuncValues(functionName, nombre2):
                                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif Analisis.KeyInFunction("while") == True:
                            if Analisis.keyInWhileFunc(functionName, nombre2)==True:
                                if Analisis.accesWhileFuncValues(functionName, nombre) != Analisis.accesWhileFuncValues(functionName, nombre2):
                                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        else: 
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
        elif Analisis.KeyInDiccionario("if"):
            if Analisis.keyInIfGen(nombre) == True:
                if Analisis.KeyInDiccionario(nombre2) == True:
                    if Analisis.accesIfGenValues(nombre)!= Analisis.TipoVarEnDiccionario(nombre2) :
                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif conditional ==True: 
                    if Analisis.KeyInDiccionario("if")==True:
                        if Analisis.keyInIfGen(nombre2) == True :
                            if Analisis.accesIfGenValues(nombre) != Analisis.accesIfGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    if Analisis.KeyInDiccionario("while") ==True:
                        if Analisis.keyInWhileGen(nombre2):
                            if Analisis.accesIfGenValues(nombre) != Analisis.accesWhileGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif function ==True:
                        if Analisis.KeyInFunction(functionName, nombre2) == True:
                            if Analisis.accesIfGenValues(nombre) != Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif conditional == True:
                            if Analisis.KeyInFunction("if")==True:
                                if Analisis.keyInIfFunc(functionName, nombre2) == True: 
                                    if Analisis.accesIfGenValues(nombre) != Analisis.accesIfFuncValues(functionName, nombre2): 
                                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif Analisis.KeyInFunction("while")==True:
                            if Analisis.keyInWhileFunc(functionName, nombre2) == True: 
                                if Analisis.accesIfGenValues(nombre) != Analisis.accesWhileFuncValues(functionName, nombre2): 
                                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                else: 
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
        elif Analisis.KeyInDiccionario("while"):
            if Analisis.keyInWhileGen(nombre) == True:
                if Analisis.KeyInDiccionario(nombre2) == True:
                    if Analisis.accesWhileGenValues(nombre)!= Analisis.TipoVarEnDiccionario(nombre2) :
                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif conditional ==True: 
                    if Analisis.KeyInDiccionario("if") == True:
                        if Analisis.keyInIfGen(nombre2) == True :
                            if Analisis.accesWhileGenValues(nombre) != Analisis.accesIfGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    if Analisis.KeyInDiccionario("while") ==True:
                        if Analisis.keyInWhileGen(nombre2):
                            if Analisis.accesWhileGenValues(nombre) != Analisis.accesWhileGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif function ==True:
                        if Analisis.KeyInFunction(functionName, nombre2) == True:
                            if Analisis.accesWhileGenValues(nombre) != Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif conditional == True:
                            if Analisis.KeyInFunction("if")==True:
                                if Analisis.keyInIfFunc(functionName, nombre2) == True: 
                                    if Analisis.accesWhileGenValues(nombre) != Analisis.accesIfFuncValues(functionName, nombre2): 
                                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif Analisis.KeyInFunction("while")==True:
                            if Analisis.keyInWhileFunc(functionName, nombre2) == True: 
                                if Analisis.accesWhileGenValues(nombre) != Analisis.accesWhileFuncValues(functionName, nombre2): 
                                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                else: 
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
        else : 
            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + "  no ha sido declarada"    
    except Exception:
        pass

    try: 
        tipo,nombre,parametros,operacion = Lectura.dataIdentifyWithParenthesis(line)
        if Analisis.isTipo(tipo) == False and tipo !="return": 
            error = "Linea " + str(num) + " Error: "+ str(tipo) + " no es un tipo de dato aceptado"
        elif Analisis.KeyInDiccionario(nombre)==True:
            error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
        else: 
            Analisis.addFunctionGen(nombre,tipo)
            Analisis.insertValuesToFunction(nombre,Lectura.variablesDeLasFunciones(parametros),num)
            function=True
            functionName=nombre        
    except Exception:
        pass
    
    if Lectura.find_closing_brace(line) == "8": 
        if conditional==True:
            conditional=False
        else: 
            function = False
            functionName=None
    else: 
        pass

    try: 
        nombre, operations, operacion = Lectura.dataNametoOperation(line) 
        if Analisis.KeyInDiccionario(nombre) ==True:
            tipo = Analisis.TipoVarEnDiccionario(nombre)
            Analisis.verificateTypes(tipo, operations, functionName, num)
        elif function == True:
            if conditional == True:
                if Analisis.KeyInFunction(functionName, "if"):
                    if Analisis.keyInIfFunc(functionName, nombre) == True:
                        tipo = Analisis.accesIfFuncValues(functionName, nombre)
                        Analisis.verificateTypes(tipo, operations, functionName, num)
                    else: 
                     error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
                elif Analisis.KeyInFunction(functionName, "while"):
                    if Analisis.keyInWhileFunc(functionName, nombre) == True:
                        tipo = Analisis.accesWhileFuncValues(functionName, nombre)
                        Analisis.verificateTypes(tipo, operations, functionName, num) 
                    else: 
                     error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
                else: 
                     error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
            elif Analisis.KeyInFunction(functionName, nombre):
                tipo = Analisis.TipoValFuncionEnDiccionario(functionName, nombre)
                Analisis.verificateTypes(tipo, operations, functionName, num)
        elif conditional == True:
            if Analisis.KeyInDiccionario("if"):
                if Analisis.keyInIfGen(nombre) ==True:
                    tipo = Analisis.accesIfGenValues(nombre)
                    Analisis.verificateTypes(tipo, operations, functionName, num)
                else: 
                     error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
            if Analisis.KeyInDiccionario("while"):
                if Analisis.keyInWhileGen(nombre) ==True:
                    tipo = Analisis.accesWhileGenValues(nombre)
                    Analisis.verificateTypes(tipo, operations, functionName, num)
                else: 
                     error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
        
        else:
            error =  "Linea " + str(num) + " Error: "+ nombre + " no es una variable que haya sido declarada"
    except Exception:
        pass
    
    try:
        tipo, nombre, operations, operacion = Lectura.dataTypeNameToOperation(line)
        if Analisis.isTipo(tipo) == False and tipo !="return": 
            error = "Linea " + str(num) + " Error: "+ str(tipo) + " no es un tipo de dato aceptado"
        else:
            if function ==True:
                if conditional ==True:
                    if Analisis.KeyInFunction(functionName,"if"): 
                        if Analisis.keyInIfFunc(functionName, nombre) == False:
                            Analisis.addVarIfFun(functionName, nombre,tipo)
                        else:
                            error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
                    elif Analisis.KeyInFunction(functionName,"while"):
                        if Analisis.keyInWhileFunc(functionName,nombre)==False:
                            Analisis.addVarWhileFun(functionName,nombre,tipo)
                elif Analisis.KeyInFunction(functionName, nombre) == False:
                    Analisis.addVarFunction(functionName, nombre,tipo)
                else:
                    error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
            else: 
                if conditional ==True:
                    if Analisis.KeyInDiccionario("if")==True:
                        if Analisis.keyInIfGen(nombre) == False:
                            Analisis.addVarIfGen(nombre,tipo)
                    elif Analisis.KeyInDiccionario("while")==True:
                        if Analisis.keyInWhileGen(nombre)==True:
                            Analisis.addVarWhileGen(nombre,tipo)
                elif Analisis.KeyInDiccionario(nombre)==False:
                    Analisis.addVariableGen(nombre,tipo)
                else: 
                     error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
        Analisis.verificateTypes(tipo, operations, functionName, num)
    except Exception:
        pass

    try:
        tipo, nombre, nombre2, operacion = Lectura.conditionalDetection(line)
        if Analisis.KeyInDiccionario(nombre) == True: 
            if Analisis.KeyInDiccionario(nombre2) == True:
                if Analisis.TipoVarEnDiccionario(nombre)!= Analisis.TipoVarEnDiccionario(nombre2) :
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
            elif conditional ==True: 
                if Analisis.KeyInDiccionario("if"):
                    if Analisis.keyInIfGen(nombre2) == True :
                        if Analisis.TipoVarEnDiccionario(nombre) != Analisis.accesIfGenValues(nombre2):
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                if Analisis.KeyInDiccionario("while"):
                    if Analisis.keyInWhileGen(nombre2)==True:
                        if Analisis.TipoVarEnDiccionario(nombre) != Analisis.accesWhileGenValues(nombre2):
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
            elif function ==True:
                    if Analisis.KeyInFunction(functionName, nombre2) == True:
                        if Analisis.TipoVarEnDiccionario(nombre) != Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif conditional == True:
                        if Analisis.KeyInFunction(functionName, "if"):
                            if Analisis.keyInIfFunc(functionName, nombre2) == True: 
                                if Analisis.TipoVarEnDiccionario(nombre) != Analisis.accesIfFuncValues(functionName, nombre2): 
                                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif Analisis.KeyInFunction(functionName,"while"):
                            if Analisis.keyInWhileFunc(functionName,nombre2)==True:
                                if Analisis.TipoVarEnDiccionario(nombre) != Analisis.accesWhileFuncValues(functionName, nombre2):
                                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
            elif Analisis.validateGeneral(Analisis.TipoVarEnDiccionario(nombre),nombre2)==False:
                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y el valor " + str(nombre2) + " no son compatibles"
            elif Analisis.validateGeneral(Analisis.TipoVarEnDiccionario(nombre),nombre2)==True:
               error =" "
            else: 
                error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
        elif function == True:
            if Analisis.KeyInFunction(functionName, nombre) == True:
                if Analisis.KeyInDiccionario(nombre2) == True:
                    if Analisis.TipoValFuncionEnDiccionario(functionName,nombre) != Analisis.TipoVarEnDiccionario(nombre2):
                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif conditional ==True: 
                    if Analisis.KeyInDiccionario("if"):
                        if Analisis.keyInIfGen(nombre2) == True :
                            if Analisis.TipoValFuncionEnDiccionario(nombre) != Analisis.accesIfGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    if Analisis.KeyInDiccionario("while"):
                        if Analisis.keyInWhileGen(nombre2) == True :
                            if Analisis.TipoValFuncionEnDiccionario(nombre) != Analisis.accesWhileGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"                
                elif Analisis.KeyInFunction(functionName, nombre2) == True:
                        if Analisis.TipoValFuncionEnDiccionario(functionName,nombre)!= Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif conditional ==True: 
                    if Analisis.KeyInFunction(functionName, "if"):
                        if Analisis.keyInIfFunc(functionName, nombre2) == True:
                            if Analisis.TipoValFuncionEnDiccionario(functionName, nombre) != Analisis.accesIfFuncValues(functionName, nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    if Analisis.KeyInFunction(functionName, "while"):
                        if Analisis.keyInWhileFunc(functionName, nombre2) == True:
                            if Analisis.TipoValFuncionEnDiccionario(functionName, nombre) != Analisis.accesWhileFuncValues(functionName, nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif Analisis.validateGeneral(Analisis.TipoValFuncionEnDiccionario(functionName,nombre),nombre2)==False:
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y el valor " + str(nombre2) + " no son compatibles"
                elif Analisis.validateGeneral(Analisis.TipoValFuncionEnDiccionario(functionName,nombre),nombre2)==True:
                    error = " "
                else: 
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
            elif conditional == True: 
                if Analisis.KeyInFunction(functionName,"if"):
                    if Analisis.keyInIfFunc(functionName, nombre) == True:
                        if Analisis.KeyInDiccionario(nombre2) == True:
                            if Analisis.accesIfFuncValues(functionName,nombre) != Analisis.TipoVarEnDiccionario(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif Analisis.keyInIfGen(nombre2) == True :
                            if Analisis.accesIfFuncValues(nombre) != Analisis.accesIfGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif function ==True:
                            if Analisis.KeyInFunction(functionName, nombre2) == True:
                                if Analisis.accesIfFuncValues(functionName,nombre)!= Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                            elif conditional==True:
                                if Analisis.KeyInFunction("if") ==True:
                                    if Analisis.keyInIfFunc(functionName, nombre2) == True:
                                        if Analisis.accesIfFuncValues(functionName, nombre) != Analisis.accesIfFuncValues(functionName, nombre2):
                                         error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                                if Analisis.KeyInFunction("while") ==True:
                                    if Analisis.keyInWhileFunc(functionName, nombre2) == True:
                                        if Analisis.accesIfFuncValues(functionName, nombre) != Analisis.accesWhileFuncValues(functionName, nombre2):
                                         error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"                      
                        elif Analisis.validateGeneral(Analisis.accesIfFuncValues(functionName,nombre),nombre2)==False:
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y el valor " + str(nombre2) + " no son compatibles"
                        elif Analisis.validateGeneral(Analisis.accesIfFuncValues(functionName,nombre),nombre2)==False:
                            error = " "
                        else: 
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
                if Analisis.KeyInFunction(functionName,"while"):
                    if Analisis.keyInWhileFunc(functionName, nombre) == True:
                        if Analisis.KeyInDiccionario(nombre2) == True:
                            if Analisis.accesWhileFuncValues(functionName,nombre) != Analisis.TipoVarEnDiccionario(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif Analisis.keyInIfGen(nombre2) == True :
                            if Analisis.accesWhileFuncValues(nombre) != Analisis.accesIfGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif function ==True:
                            if Analisis.KeyInFunction(functionName, nombre2) == True:
                                if Analisis.accesWhileFuncValues(functionName,nombre)!= Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                            elif conditional==True:
                                if Analisis.KeyInFunction("if") ==True:
                                    if Analisis.keyInIfFunc(functionName, nombre2) == True:
                                        if Analisis.accesWhileFuncValues(functionName, nombre) != Analisis.accesIfFuncValues(functionName, nombre2):
                                         error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                                if Analisis.KeyInFunction("while") ==True:
                                    if Analisis.keyInWhileFunc(functionName, nombre2) == True:
                                        if Analisis.accesWhileFuncValues(functionName, nombre) != Analisis.accesWhileFuncValues(functionName, nombre2):
                                         error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"                      
                        elif Analisis.validateGeneral(Analisis.accesWhileFuncValues(functionName,nombre),nombre2)==False:
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y el valor " + str(nombre2) + " no son compatibles"
                        elif Analisis.validateGeneral(Analisis.accesWhileFuncValues(functionName,nombre),nombre2)==False:
                            error = "  "
                    else: 
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
        elif conditional ==True:
            if Analisis.KeyInDiccionario("if")==True:
                if Analisis.keyInIfGen(nombre) == True:
                    if Analisis.KeyInDiccionario(nombre2) == True:
                        if Analisis.accesIfGenValues(nombre)!= Analisis.TipoVarEnDiccionario(nombre2) :
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif Analisis.keyInIfGen(nombre2) == True :
                            if Analisis.accesIfGenValues(nombre) != Analisis.accesIfGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif Analisis.KeyInDiccionario("while")==True:
                        if Analisis.keyInWhileGen(nombre) == True:
                            if Analisis.accesIfGenValues(nombre) != Analisis.accesWhileGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif function ==True:
                        if Analisis.KeyInFunction(functionName, nombre2) == True:
                            if Analisis.accesIfGenValues(nombre) != Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif conditional == True:
                            if Analisis.KeyInFunction("if")==True:
                                if Analisis.keyInIfFunc(functionName, nombre2) == True: 
                                    if Analisis.accesIfGenValues(nombre) != Analisis.accesIfFuncValues(functionName, nombre2): 
                                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                            if Analisis.KeyInFunction("while")==True:
                                if Analisis.keyInWhileFunc(functionName, nombre2) == True: 
                                    if Analisis.accesIfGenValues(nombre) != Analisis.accesWhileFuncValues(functionName, nombre2): 
                                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif Analisis.validateGeneral(Analisis.accesIfGenValues(nombre),nombre2)==False:
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y el valor " + str(nombre2) + " no son compatibles"
                elif Analisis.validateGeneral(Analisis.accesIfGenValues(nombre),nombre2)==False:
                    error = " "
                else: 
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
            elif Analisis.KeyInDiccionario("while")==True:
                if Analisis.keyInWhileGen(nombre) == True:
                    if Analisis.KeyInDiccionario(nombre2) == True:
                        if Analisis.accesIfWhileGenValues(nombre)!= Analisis.TipoVarEnDiccionario(nombre2) :
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif Analisis.keyInIfGen(nombre2) == True :
                            if Analisis.accesWhileGenValues(nombre) != Analisis.accesIfGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif Analisis.KeyInDiccionario("while")==True:
                        if Analisis.keyInWhileGen(nombre) == True:
                            if Analisis.accesWhileGenValues(nombre) != Analisis.accesWhileGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif function ==True:
                        if Analisis.KeyInFunction(functionName, nombre2) == True:
                            if Analisis.accesWhileGenValues(nombre) != Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif conditional == True:
                            if Analisis.KeyInFunction("if")==True:
                                if Analisis.keyInIfFunc(functionName, nombre2) == True: 
                                    if Analisis.accesWhileGenValues(nombre) != Analisis.accesIfFuncValues(functionName, nombre2): 
                                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                            if Analisis.KeyInFunction("while")==True:
                                if Analisis.keyInWhileFunc(functionName, nombre2) == True: 
                                    if Analisis.accesWhileGenValues(nombre) != Analisis.accesWhileFuncValues(functionName, nombre2): 
                                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif Analisis.validateGeneral(Analisis.accesIfGenValues(nombre),nombre2)==False:
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y el valor " + str(nombre2) + " no son compatibles"
                elif Analisis.validateGeneral(Analisis.accesIfGenValues(nombre),nombre2)==False:
                    error = " "
            else: 
                error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
        else : 
            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + "  no ha sido declarada"  
        if function ==False:
            Analisis.addIfGen()
            conditional=True
        elif function == True:
            Analisis.addIfFunction(functionName)
            conditional=True
    except Exception:
        pass

    try:
        tipo, nombre, nombre2, operacion = Lectura.loopDetection(line)
        if Analisis.KeyInDiccionario(nombre) == True: 
            if Analisis.KeyInDiccionario(nombre2) == True:
                if Analisis.TipoVarEnDiccionario(nombre)!= Analisis.TipoVarEnDiccionario(nombre2) :
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
            elif conditional ==True: 
                if Analisis.KeyInDiccionario("if"):
                    if Analisis.keyInIfGen(nombre2) == True :
                        if Analisis.TipoVarEnDiccionario(nombre) != Analisis.accesIfGenValues(nombre2):
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                if Analisis.KeyInDiccionario("while"):
                    if Analisis.keyInWhileGen(nombre2)==True:
                        if Analisis.TipoVarEnDiccionario(nombre) != Analisis.accesWhileGenValues(nombre2):
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
            elif function ==True:
                    if Analisis.KeyInFunction(functionName, nombre2) == True:
                        if Analisis.TipoVarEnDiccionario(nombre) != Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif conditional == True:
                        if Analisis.KeyInFunction(functionName, "if"):
                            if Analisis.keyInIfFunc(functionName, nombre2) == True: 
                                if Analisis.TipoVarEnDiccionario(nombre) != Analisis.accesIfFuncValues(functionName, nombre2): 
                                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif Analisis.KeyInFunction(functionName,"while"):
                            if Analisis.keyInWhileFunc(functionName,nombre2)==True:
                                if Analisis.TipoVarEnDiccionario(nombre) != Analisis.accesWhileFuncValues(functionName, nombre2):
                                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
            elif Analisis.validateGeneral(Analisis.TipoVarEnDiccionario(nombre),nombre2)==False:
                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y el valor " + str(nombre2) + " no son compatibles"
            elif Analisis.validateGeneral(Analisis.TipoVarEnDiccionario(nombre),nombre2)==True:
               error = " "
            else: 
                error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
        elif function == True:
            if Analisis.KeyInFunction(functionName, nombre) == True:
                if Analisis.KeyInDiccionario(nombre2) == True:
                    if Analisis.TipoValFuncionEnDiccionario(functionName,nombre) != Analisis.TipoVarEnDiccionario(nombre2):
                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif conditional ==True: 
                    if Analisis.KeyInDiccionario("if"):
                        if Analisis.keyInIfGen(nombre2) == True :
                            if Analisis.TipoValFuncionEnDiccionario(nombre) != Analisis.accesIfGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    if Analisis.KeyInDiccionario("while"):
                        if Analisis.keyInWhileGen(nombre2) == True :
                            if Analisis.TipoValFuncionEnDiccionario(nombre) != Analisis.accesWhileGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"                
                elif Analisis.KeyInFunction(functionName, nombre2) == True:
                        if Analisis.TipoValFuncionEnDiccionario(functionName,nombre)!= Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif conditional ==True: 
                    if Analisis.KeyInFunction(functionName, "if"):
                        if Analisis.keyInIfFunc(functionName, nombre2) == True:
                            if Analisis.TipoValFuncionEnDiccionario(functionName, nombre) != Analisis.accesIfFuncValues(functionName, nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    if Analisis.KeyInFunction(functionName, "while"):
                        if Analisis.keyInWhileFunc(functionName, nombre2) == True:
                            if Analisis.TipoValFuncionEnDiccionario(functionName, nombre) != Analisis.accesWhileFuncValues(functionName, nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif Analisis.validateGeneral(Analisis.TipoValFuncionEnDiccionario(functionName,nombre),nombre2)==False:
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y el valor " + str(nombre2) + " no son compatibles"
                elif Analisis.validateGeneral(Analisis.TipoValFuncionEnDiccionario(functionName,nombre),nombre2)==True:
                    error = " "
                else: 
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
            elif conditional == True: 
                if Analisis.KeyInFunction(functionName,"if"):
                    if Analisis.keyInIfFunc(functionName, nombre) == True:
                        if Analisis.KeyInDiccionario(nombre2) == True:
                            if Analisis.accesIfFuncValues(functionName,nombre) != Analisis.TipoVarEnDiccionario(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif Analisis.keyInIfGen(nombre2) == True :
                            if Analisis.accesIfFuncValues(nombre) != Analisis.accesIfGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif function ==True:
                            if Analisis.KeyInFunction(functionName, nombre2) == True:
                                if Analisis.accesIfFuncValues(functionName,nombre)!= Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                            elif conditional==True:
                                if Analisis.KeyInFunction("if") ==True:
                                    if Analisis.keyInIfFunc(functionName, nombre2) == True:
                                        if Analisis.accesIfFuncValues(functionName, nombre) != Analisis.accesIfFuncValues(functionName, nombre2):
                                         error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                                if Analisis.KeyInFunction("while") ==True:
                                    if Analisis.keyInWhileFunc(functionName, nombre2) == True:
                                        if Analisis.accesIfFuncValues(functionName, nombre) != Analisis.accesWhileFuncValues(functionName, nombre2):
                                         error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"                      
                        elif Analisis.validateGeneral(Analisis.accesIfFuncValues(functionName,nombre),nombre2)==False:
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y el valor " + str(nombre2) + " no son compatibles"
                        elif Analisis.validateGeneral(Analisis.accesIfFuncValues(functionName,nombre),nombre2)==False:
                            error = " "
                        else: 
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
                if Analisis.KeyInFunction(functionName,"while"):
                    if Analisis.keyInWhileFunc(functionName, nombre) == True:
                        if Analisis.KeyInDiccionario(nombre2) == True:
                            if Analisis.accesWhileFuncValues(functionName,nombre) != Analisis.TipoVarEnDiccionario(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif Analisis.keyInIfGen(nombre2) == True :
                            if Analisis.accesWhileFuncValues(nombre) != Analisis.accesIfGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif function ==True:
                            if Analisis.KeyInFunction(functionName, nombre2) == True:
                                if Analisis.accesWhileFuncValues(functionName,nombre)!= Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                            elif conditional==True:
                                if Analisis.KeyInFunction("if") ==True:
                                    if Analisis.keyInIfFunc(functionName, nombre2) == True:
                                        if Analisis.accesWhileFuncValues(functionName, nombre) != Analisis.accesIfFuncValues(functionName, nombre2):
                                         error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                                if Analisis.KeyInFunction("while") ==True:
                                    if Analisis.keyInWhileFunc(functionName, nombre2) == True:
                                        if Analisis.accesWhileFuncValues(functionName, nombre) != Analisis.accesWhileFuncValues(functionName, nombre2):
                                         error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"                      
                        elif Analisis.validateGeneral(Analisis.accesWhileFuncValues(functionName,nombre),nombre2)==False:
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y el valor " + str(nombre2) + " no son compatibles"
                        elif Analisis.validateGeneral(Analisis.accesWhileFuncValues(functionName,nombre),nombre2)==False:
                            error = " "
                    else: 
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
        elif conditional ==True:
            if Analisis.KeyInDiccionario("if")==True:
                if Analisis.keyInIfGen(nombre) == True:
                    if Analisis.KeyInDiccionario(nombre2) == True:
                        if Analisis.accesIfGenValues(nombre)!= Analisis.TipoVarEnDiccionario(nombre2) :
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif Analisis.keyInIfGen(nombre2) == True :
                            if Analisis.accesIfGenValues(nombre) != Analisis.accesIfGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif Analisis.KeyInDiccionario("while")==True:
                        if Analisis.keyInWhileGen(nombre) == True:
                            if Analisis.accesIfGenValues(nombre) != Analisis.accesWhileGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif function ==True:
                        if Analisis.KeyInFunction(functionName, nombre2) == True:
                            if Analisis.accesIfGenValues(nombre) != Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif conditional == True:
                            if Analisis.KeyInFunction("if")==True:
                                if Analisis.keyInIfFunc(functionName, nombre2) == True: 
                                    if Analisis.accesIfGenValues(nombre) != Analisis.accesIfFuncValues(functionName, nombre2): 
                                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                            if Analisis.KeyInFunction("while")==True:
                                if Analisis.keyInWhileFunc(functionName, nombre2) == True: 
                                    if Analisis.accesIfGenValues(nombre) != Analisis.accesWhileFuncValues(functionName, nombre2): 
                                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif Analisis.validateGeneral(Analisis.accesIfGenValues(nombre),nombre2)==False:
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y el valor " + str(nombre2) + " no son compatibles"
                elif Analisis.validateGeneral(Analisis.accesIfGenValues(nombre),nombre2)==False:
                    error = " "
                else: 
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
            elif Analisis.KeyInDiccionario("while")==True:
                if Analisis.keyInWhileGen(nombre) == True:
                    if Analisis.KeyInDiccionario(nombre2) == True:
                        if Analisis.accesIfWhileGenValues(nombre)!= Analisis.TipoVarEnDiccionario(nombre2) :
                            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif Analisis.keyInIfGen(nombre2) == True :
                            if Analisis.accesWhileGenValues(nombre) != Analisis.accesIfGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif Analisis.KeyInDiccionario("while")==True:
                        if Analisis.keyInWhileGen(nombre) == True:
                            if Analisis.accesWhileGenValues(nombre) != Analisis.accesWhileGenValues(nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                    elif function ==True:
                        if Analisis.KeyInFunction(functionName, nombre2) == True:
                            if Analisis.accesWhileGenValues(nombre) != Analisis.TipoValFuncionEnDiccionario(functionName,nombre2):
                                error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                        elif conditional == True:
                            if Analisis.KeyInFunction("if")==True:
                                if Analisis.keyInIfFunc(functionName, nombre2) == True: 
                                    if Analisis.accesWhileGenValues(nombre) != Analisis.accesIfFuncValues(functionName, nombre2): 
                                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                            if Analisis.KeyInFunction("while")==True:
                                if Analisis.keyInWhileFunc(functionName, nombre2) == True: 
                                    if Analisis.accesWhileGenValues(nombre) != Analisis.accesWhileFuncValues(functionName, nombre2): 
                                        error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y la variable " + str(nombre2) + " no son compatibles"
                elif Analisis.validateGeneral(Analisis.accesIfGenValues(nombre),nombre2)==False:
                    error = "Linea " + str(num) + " Error: La variable " + str(nombre) + " y el valor " + str(nombre2) + " no son compatibles"
                elif Analisis.validateGeneral(Analisis.accesIfGenValues(nombre),nombre2)==False:
                    error = " "
            else: 
                error = "Linea " + str(num) + " Error: La variable " + str(nombre2) + "  no ha sido declarada"
        else : 
            error = "Linea " + str(num) + " Error: La variable " + str(nombre) + "  no ha sido declarada"  
        if function ==False:
            Analisis.addWhileGen()
        elif function == True:
            Analisis.addWhileFunction(functionName)
        conditional=True
    except Exception: 
        pass
    
    try: # int x = suma(x,y,z) 
        tipo, nombre, nombre_Func, params_string , num = Lectura.dataToNameToFunction(linea)

        if function ==True:
            if Analisis.KeyInFunction(functionName, nombre) == False:
                if conditional == True:
                    if Analisis.KeyInFunction(functionName,"if")==True:
                        if Analisis.keyInIfFunc(functionName, nombre) == False and Analisis.KeyInDiccionario(nombre) == False and Analisis.KeyInFunction(functionName,nombre)==False:
                            Analisis.addVarIfFun(functionName, nombre, tipo)
                    elif Analisis.KeyInFunction(functionName,"while")==True:
                        if Analisis.keyInWhileFunc(functionName, nombre) == False and Analisis.KeyInDiccionario(nombre) == False and Analisis.KeyInFunction(functionName,nombre)==False:
                            Analisis.addVarWhileFun(functionName,nombre, tipo)
                    else: 
                            error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
                else:
                    Analisis.addVarFunction(functionName, nombre,tipo)
            elif Analisis.validateGeneral(tipo,valor) == False: 
                error = "Linea " + str(num) + " Error: "+ str(valor) + " no es un dato aceptable para una variable de tipo " + str(tipo)
            if Analisis.KeyInDiccionario(nombre)==False:
                if conditional == True:
                    if Analisis.KeyInDiccionario("if")==True:
                        if Analisis.keyInIfGen(nombre)==False:
                            Analisis.addVarIfGen(nombre,tipo)
                        else:
                          error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
                    if Analisis.KeyInDiccionario("while")==True:
                        if Analisis.keyInWhileGen(nombre)==False:
                            Analisis.addVarWhileGen(nombre,tipo)
                        else:
                             error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada"
                else: 
                    Analisis.addVariableGen(nombre,tipo)  
        else:
            error =  "Linea " + str(num) + " Error: "+ nombre + " es una variable que ya ha sido creada" 
        if Analisis.KeyInDiccionario(nombre):
            error  = "Linea " + str(num) + " Error: La variable " + str(nombre) + "  ya ha sido declarada"
        elif not Analisis.KeyInDiccionario(nombre_Func):
            error  = "Linea " + str(num) + " Error: La funcion " + str(nombre_Func) + "  no ha sido declarada"
        elif Analisis.TipoVarEnDiccionario(nombre_Func) == 'void':
            error  = "Linea " + str(num) + " Error: La funcion " + str(nombre_Func) + "  no retorna un valor"
        elif Analisis.TipoVarEnDiccionario(nombre_Func) != tipo:
             error  = "Linea " + str(num) + " Error: La funcion " + str(nombre_Func) + "  retorna un tipo de valor incompatible con '"+nombre+"' "
        else:
            error  = "Linea " + str(num) + " Error: El tipo de dato " + str(tipo) + "  no existe"
    except Exception: 
        pass
    
    try:
        valores, num = Lectura.returnDetect(linea)
        Analisis.validateReturnValuesFunction(functionName,valores,numLine)
    except Exception:
        pass

    try: #x = suma(x,y,z ) terminar de probar 
        nombre, nombre_funcio, params_string, num = Lectura.nameToFunction(linea)
        if Analisis.KeyInDiccionario(nombre):
            if not Analisis.KeyInDiccionario(nombre_funcio):
                error  = "Linea " + str(num) + " Error: La funcion " + str(nombre_funcio) + "  no ha sido declarada"
            elif Analisis.TipoVarEnDiccionario(nombre_funcio) == 'void':
                error  = "Linea " + str(num) + " Error: La funcion " + str(nombre_funcio) + "  no retorna un valor"
            elif Analisis.TipoVarEnDiccionario(nombre_funcio) != Analisis.TipoVarEnDiccionario(nombre):
                 error  = "Linea " + str(num) + " Error: La funcion " + str(nombre_funcio) + "  retorna un tipo de valor incompatible con '"+nombre+"' "
        else:
            error  = "Linea " + str(num) + " Error: La variable '" + str(nombre) + "'  no existe"
    except Exception:
        pass

    return error,operacion, function, functionName, conditional


#En caso de que falle la direccion del codigo al descargarlo desde github, copiar y pegar la direccion relativa del Codigo.txt
lineas = Lectura.read("Codigo.txt") 
numLine = 1 
operacion = ""
function = False
functionName = None
condLoop = False
for line in lineas: 
    error, operacion, function, functionName, condLoop = lectura(line,numLine, operacion,function, functionName, condLoop )
    if error != " ":
        print(error)
    numLine += 1

print(Analisis.diccionarioGen)




    

   
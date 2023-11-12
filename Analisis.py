#Analisis Semantico


tiposDatos = {'int' :(int,), 'float':(float,), 'string': (str,), 'void':(type(None),) }
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

    
#def sameType(var1, var2):
     

    
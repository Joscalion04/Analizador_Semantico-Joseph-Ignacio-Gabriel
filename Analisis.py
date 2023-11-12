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

def transform(word, dato): 
    
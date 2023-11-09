#Analisis Semantico



def tipoDato(word,dato): 
    tiposDatos = {'int' :(int,), 'float':(float,), 'string': (str,), 'void':(type(None),) }
    if word in tiposDatos and isinstance(dato, tiposDatos[word]): 
        return "word"+str(dato)
    else: 
        return "error"

def comparar(palabra, cadena):
    """ Compara caracteres de palabras para saber si estan contenidos en cadenas
    (str,str) -> bool
    """
    encuentra = True
    i = 0
    cont = 0 
    while i < len(palabra) and encuentra:
        if palabra[i] in cadena and \
           palabra.count(palabra[i]) <= cadena.count(palabra[i]):
            cont += 1
        else:
            encuentra = False
        i += 1        
    return encuentra
        

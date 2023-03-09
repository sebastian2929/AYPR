#sebastian David Blanco Rodriguez
def validar(secuencia):
    """Verifica si la cadena es un gen valido
    (str) -> (bool)
    """
    long = len(secuencia)
    if long % 3 != 0:
        return False
    if secuencia[0:3] != "ATG":
        return False
    if secuencia[-3:] != "TAG" and secuencia[-3:] != "TAA" and secuencia[-3:] != "TGA":
        return False
    for i in range(3,len(secuencia)-3,3):
        if secuencia[i:i+3] == "TAG" or secuencia[i:i+3] == "TAA" or secuencia[i:i+3] == "TGA":
            return False
    return True 
#
def main():
    """ funcion principal"""
    secuencia = input("Digite la cadena de genes: ")
    
main()

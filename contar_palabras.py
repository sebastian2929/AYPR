#Sebastian David Blanco Rodriguez
#Cristian David Naranjo Orjuela

def contar(oracion, final):
    """ cuanta la cantidad de veces que sale una palabra en la oracion 
    (list, str) -> none
    """
    i = 0
    while i < len(oracion):
        if oracion[i] != oracion[i-1]:
            final = oracion.count(oracion[i])
            print(final, oracion[i])
        i =+ 1
#
def main():
    """ Funcion principal """
    final = ""
    oracion = input("Escriba la oracion: ")
    oracion = oracion[:-1]
    oracion = oracion.lower()
    oracion = oracion.split(" ")
    oracion.sort()
    contar(oracion, final)
#
main()


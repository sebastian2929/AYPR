#Sebastian David Blanco Rodriguez

def normalizacion(arreglo):
    """ funcion para normalizar los valores que se
        encuentran dentro de un arreglo
        (lista de flotantes) -> (listas de flotantes)
    """
    mayor = 0
    menor = 0
    i = 0
    x = 0 
    while i < len(arreglo):
        if arreglo[i] > mayor:
            mayor = arreglo[i]
        if arreglo[i] < menor:
            menor = arreglo[i]
        i = i + 1
    
    divisor = mayor - menor

    while x < len(arreglo):
        arreglo[i] = arreglo[i] / divisor
        x = x + 1
    return arreglo[i]

def main():
    """funcion para pasar los datos de una lista a numeros tipo float
        y dar como resultado una lista de numeros tipo float
    """
Lista3 = [0 for i in range(0,20)]



    
    

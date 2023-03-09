def sumalist_rec(arreglo):
    """funcion obtiene la suma de los valores en un arreglo de manera recurrente
    (list) -> int
    """
    print(arreglo)
    if len(arreglo) > 1:   #caso recurrente
        return arreglo[0] + sumalist_rec(arreglo[1:])
    elif len(arreglo) == 1:   #caso base
        return arreglo[0]
    

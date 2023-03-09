def burbuja(arreglo):
    """ Ordenamiento burbuja
    (list) -> (list)
    """
    for i in range(len(arreglo)-1):
        for j in range(len(arreglo)-1):
            if arreglo[j] > arreglo[j+1]:
                temp = arreglo[j]
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = temp
                
    return arreglo
#
def main():
    """ Funcion Principal """
    arreglo = [[5],[4],[9],[7],[2],[9],[8]]
    arreglo = burbuja(arreglo)
    print(arreglo)
#
main()

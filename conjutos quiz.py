#Sebastian David Blanco Rodriguez
def interseccion(conj_1,conj_2):
    """ Esta funcion encuentra los numeros en comun dentro de dos listas
    (list1D, list1D) -> list1D
    """
    interseccion = []
    for i in conj_1:
        for j in conj_2:
            if i is not conj_2:
                interseccion.append(i)
            if j is not conj_1:
                interseccion.append(j)
    return interseccion

#
def main():
    """ Funcion Principal """
    inter = []
    conj_1 = input("Primer conjunto: ").split(",")
    conj_2 = input("Segundo conjunto: ").split(",")
    conj_1 = [int(i) for i in conj_1]
    conj_2 = [int(i) for i in conj_2]
    inter = interseccion(conj_1,conj_2)
    if inter == []:
        print("No existe una interseccion entre los 2 conjuntos")
    else:
        print(*inter)
main()


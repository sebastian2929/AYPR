#Cristian David Naranjo Orjuela
#Sebastian David Blanco Rodriguez

def crear_matriz_uno(fila, columna):
    """ crea la matriz uno
    (int, int) -> list2D
    """
    matriz = []
    for i in range(fila):
            filas = input("digite los valores separados por comas:").split(",")
            filas = [int(i) for i in filas]
            matriz.append(filas)
    return matriz
#
def crear_matriz_dos(fila2, columna2):
    """ crea la matriz dos
    (int, int) -> list2D
    """
    matriz = []
    for i in range(fila2):
            filas = input("digite los valores separados por comas:").split(",")
            filas = [int(i) for i in filas]
            matriz.append(filas)
    return matriz
#
def multiplicar(matriz_uno, matriz_dos, columna, fila2, columna2, fila):
    """
    realiza la multiplicacion de dos matrices
    (list2D, list2D, int, int, int) -> list2D
    """
    matriz_final = [[0 for j in range(columna2)] for i in range(fila)]
    for i in range(len(matriz_uno)):
        for j in range(len(matriz_dos[0])):
            for k in range(len(matriz_dos)):
                matriz_final[i][j] += matriz_uno[i][k] * matriz_dos[k][j]
    return matriz_final
            
def main():
    """ Funcion Principal """
    matriz_uno = input("fila, columna (matriz uno): ").split(",")
    fila = int(matriz_uno[0])
    columna = int(matriz_uno[1])
    matriz_uno = crear_matriz_uno(fila, columna)
    print(matriz_uno)
    matriz_dos = input("fila, columna (matriz dos): ").split(",")
    fila2 = int(matriz_dos[0])
    columna2 = int(matriz_dos[1])
    matriz_dos = crear_matriz_dos(fila2, columna2)
    matriz_final = multiplicar(matriz_uno, matriz_dos, columna, fila2, columna2, fila)
    for i in range(len(matriz_final)):
        print(*matriz_final[i])
main()

    

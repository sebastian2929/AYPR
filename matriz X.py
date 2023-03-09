def main():
    n = int(input("Digite el tamaño de la matriz: "))
    tabla = []
    for i in range(n):
        fila = [0] * n
        tabla.append(fila)
    for i in range(n):              #recorre la diagonal principal
        tabla[i][i] = "X"
    j = n - 1
    for i in range(n):
        tabla[i][j] = "X"
        j -= 1            # es lo mismo de j = j - 1
    for i in range(n):
        print(*tabla[i])

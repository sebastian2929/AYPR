def main():
    n = int(input("Digite el tamaño de la matriz: "))
    tabla = []
    for i in range(n):
        fila = ["|"] * n
        tabla.append(fila)
    j = len(tabla) - 1
    for i in range(n):
        tabla[0][i] = "="
        tabla[i][0] = "="
        tabla[i][j] = "="
        tabla[j][i] = "="
    for i in range(n):
        print(*tabla[i])
main()
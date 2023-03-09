matriz = [[1,2,3],[4,5,6]]
len(matriz)  #muestra la cantidad de columnas
len(matriz[0]) #muestra la cantidad de elementos de la primera fila

matriz = []
n = 5
m = 6
for i in range(0, n):    #crea 5 columnas
    fila = [0 for i in range(m)] #rellena las columnas con "m" ceros 
    matriz.append(fila)

def main():
    n = int(input("Digite el tamaño de la matriz: "))
    tabla = []
    for i in range(n):
        fila = [0] * n
        tabla.append(fila)
    print(tabla)
    print("*****")
    conta = 1
    #recorre una matriz
    for i in range(n):
        for j in range(n):
            tabla[i][j] = conta
            conta = conta + 1
    print(tabla)
    print("*****")
    #imprimir fila x fila
    for i in range(n):
        print(tabla[i])
    print("*****")
        #para no imprimir corchete
    for i in range(n):
        print(*tabla[i])
    print("*****")
    #imprime las posiciones
    for i in range(n):
        for j in range(n):
            print(str(i) + "," +str(j), end = "  ")
        print() 
    #recorrer la diagonal principal
    for i in range(n):
        table[i][i] = "x"
    

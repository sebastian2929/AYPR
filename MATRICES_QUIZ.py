#Sebastian David Blanco Rodriguez
import random
def main():
    n = int(input("Digite el tamaño del tablero (filas): "))
    m = int(input("Digite el tamaño del tablero (columnas): "))
    ubi_n = int(input("digite posicion de la fila: "))
    ubi_m = int(input("digite posicion de la columna : "))
    matriz = []
    for i in range(n):
        for j in range(m):
            fila = random.randint(0,9)
            col = random.randint(0,9)
            matriz[i][j] = matriz[fila][col]
    for k in range(n):
        print(*matriz[k])
    suma = alrededor(n,m,matriz,ubi_n,ubi_m)
    print(suma)

def alrededor(n,m,matriz,ubi_n,ubi_m):
    suma = 0
    for i in range(n):
        for j in range(m):
            if matriz[i][j] == "*":
                for k in [-1,0,1]:
                    for l in [-1,0,1]:
                        if 0 <= i+k <= n-1 and 0 <= j+l <= m-1:
                            if matriz[i+k][j+l] == matriz[ubi_n][ubi_m]:
                                temp = matriz[i+k][j+l]
                                suma = suma + temp
    return(suma)

        
    

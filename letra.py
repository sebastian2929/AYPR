def main():
    """ funcion principal """
    n = input("tamaño caracter: ").split(" ")
    nn = int(n[0])
    c = n[1]
    matriz = [[0 for j in range(nn)] for i in range(nn)]
    for i in range(nn):
        matriz[i][0] = c
    for k in range(nn):
        matriz[k][k] = c
    for j in range(nn):
        matriz[j][nn-1] = c
    for i in range(nn):
        for j in range(nn):
            print()
            if matriz[i][j] != 0:
                print(matriz[i][j] , end = " ")
        print()
main()
    

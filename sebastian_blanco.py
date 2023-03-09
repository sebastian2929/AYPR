#Sebastian David Blanco Rodriguez
def traducir(matriz):
    """ Esta funcion traduce el Lenguaje Braille
    (list2D) -> None
    """
    valor = 0
    var = 0
    var_2 = 2
    cont = 0
    while cont != len(matriz):
        for i in range(len(matriz)):
            for j in range(var,var_2):
                for i in range(len(matriz)):
                    print(*matriz[i])
                if matriz == [[".","*"],["*","*"],["*","*"]]:
                    valor = 1
                if matriz == [[".","*"],[".","*"],["*","*"]]:
                    valor = 2
                if matriz == [[".","."],["*","*"],["*","*"]]:
                    valor = 3
                if matriz == [[".","."],["*","."],["*","*"]]:
                    valor = 4
                if matriz == [[".","*"],["*","."],["*","*"]]:
                    valor = 5
                if matriz == [[".","."],[".","*"],["*","*"]]:
                    valor = 6
                if matriz == [[".","."],[".","."],["*","*"]]:
                    valor = 8
                if matriz == [[".","*"],[".","."],["*","*"]]:
                    valor = 9
                if matriz == [["*","."],[".","."],["*","*"]]:
                    valor = 0
        var += 2
        var += 2
        cont += 1
    print(valor)
    



def main():
    """ Funcion principal """
    numero = int(input("cantidad de dígitos que contiene el mensaje Braille: "))
    cont = 0
    matriz = []
    while cont != numero:
        cont += 1
        temp = input("")
        matriz.append(temp)
    traducir(matriz)
main()
        
    

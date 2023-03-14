"""
Sebastian David Blanco Rodriguez
"""
import random

def tablero(tableroj, tabler, n, m, minas):
    """Esta funcion crea dos matrices una el tablero del jugador otra el tablero oculto donde aparecen las minas
    (list,list,int,int,int)->(list 2D, list 2D)
    """
    for i in range(n):
        fila = [0] * m
        tabler.append(fila)
    var = minas
    for i in range(var):
        filas = random.randint(0, n - 1)
        col = random.randint(0, m - 1)
        while tabler[filas][col] == "*":
            filas = random.randint(0, n - 1)
            col = random.randint(0, m - 1)
        if tabler[filas][col] != "*":
            tabler[filas][col] = "*"
    for i in range(n):
        fila2 = ["■"] * m
        tableroj.append(fila2)
    return tabler, tableroj


#
def alrededor(tabler, n, m):
    """  obtiene la cantidad de minas alrededor de una posición dada
    (List2D, int,int,int) -> int
    """
    for i in range(n):
        for j in range(m):
            if tabler[i][j] == "*":
                for k in [-1, 0, 1]:
                    for h in [-1, 0, 1]:
                        if 0 <= i + k <= n - 1 and 0 <= j + h <= m - 1:
                            if tabler[i + k][j + h] != "*":
                                tabler[i + k][j + h] += 1
    return tabler


#
def imprimir_tablero(tableroj, tab, n, m, minas, ganadas, perdidas, veces):
    """ Imprime el tablero del jugador
    (list2D, list2D, int) -> None
    """
    jugadas = (n * m) - minas
    per = 0
    cont = 0
    while per == 0:
        for i in range(n):
            print(*tableroj[i])
        revelar_n = int(input("digite la fila: ")) - 1
        revelar_m = int(input("digite la columna: ")) - 1
        while revelar_n > n - 1 or revelar_m > m - 1:
            print("La posicion no se encuentra en el tablero")
            revelar_n = int(input("digite la fila: ")) - 1
            revelar_m = int(input("digite la columna: ")) - 1
        while revelar_n <= -1 or revelar_m <= -1:
            print("La posicion no se encuentra en el tablero")
            revelar_n = int(input("digite la fila: ")) - 1
            revelar_m = int(input("digite la columna: ")) - 1
        if tab[revelar_n][revelar_m] == "*":
            tableroj[revelar_n][revelar_m] = tab[revelar_n][revelar_m]
            for k in range(n):
                print(*tableroj[k])
            print("""
             . . .                         
              \|/                          
            `--+--'                        
              /|\                          
             ' | '                         
               |                           
               |                           
           ,--'#`--.                       
           |#######|                       #
        _.-'#######`-._                    #
     ,-'###############`-.                 #
   ,'#####################`,               ###      ##     ##    ##   ## #
  /#########################\              #   #   #  #   #  #  #  #  # # #
 |###########################|             #   #   #  #   #  #  #  #  # # # 
|#############################|            ###      ##     ##    ##   #   #
|#############################|            
|#############################|            
|#############################|            
 |###########################|             
  \#########################/              
   `.#####################,'               
     `._###############_,'                 
        `--..#####..--'
             """)
            print("USTED PERDIO")
            perdidas += 1
            veces += 1
            per = 1
        if tableroj[revelar_n][revelar_m] == "■":
            if tab[revelar_n][revelar_m] != "*":
                tableroj[revelar_n][revelar_m] = tab[revelar_n][revelar_m]
                cont += 1
        if jugadas == cont:
            for h in range(n):
                print(*tableroj[h])
            print("USTED GANO!!!")
            ganadas += 1
            veces += 1
            per = 1
    jugar = input("Desea volver a jugar (si/no): ")
    return jugar, ganadas, perdidas, veces


#
def main():
    """ Funcion principal, toma de datos """
    jugar = "si"
    ganadas = 0
    perdidas = 0
    veces = 0
    print("BIENVENIDO AL JUEGO DE BUSCAMINAS")
    nombre = input("Nombre del jugador: ")
    while jugar == "si":
        print("=================================================================")
        print("partidas jugadas:  ", veces)
        print("partidas ganadas:  ", ganadas)
        print("partidas perdidas: ", perdidas)
        print("**** Buena suerte ****")
        tabler = []
        tableroj = []
        n = int(input("Digite el tamaño del tablero (filas): "))
        while n <= 1:
            print("La fila tiene que ser minimo de 2")
            n = int(input("Digite el tamaño del tablero (filas):"))
        m = int(input("Digite el tamaño del tablero (columnas): "))
        while m <= 1:
            print("La columna tiene que ser minimo de 2")
            m = int(input("Digite el tamaño del tablero (columnas):"))
        var = n * m // 2
        minas = random.randrange(1, var)
        if minas == 1:
            print("En esta partida hay", minas, "mina")
        else:
            print("En esta partida hay", minas, "minas")
        tabler, tableroj = tablero(tableroj, tabler, n, m, minas)
        tab = alrededor(tabler, n, m)
        jugar, ganadas, perdidas, veces = imprimir_tablero(tableroj, tab, n, m, minas, ganadas, perdidas, veces)
    if jugar == "no":
        print("=================================================================")
        if ganadas == 0 and perdidas == 1:
            print(nombre, " perdió ", perdidas, " vez y nunca ganó")
        if ganadas == 1 and perdidas == 0:
            print(nombre, " ganó ", ganadas, " vez y nunca perdió")
        if ganadas > 1 and perdidas == 0:
            print(nombre, " ganó", ganadas, " veces y nunca perdió")
        if ganadas == 0 and perdidas > 1:
            print(nombre, " perdió", perdidas, " veces y nunca ganó")
        if ganadas == 1 and perdidas == 1:
            print(nombre, " ganó ", ganadas, " vez y perdió ", perdidas, " vez")
        if ganadas > 1 and perdidas == 1:
            print(nombre, " ganó", ganadas, " veces y perdió ", perdidas, " vez")
        if ganadas == 1 and perdidas > 1:
            print(nombre, " ganó", ganadas, " vez y perdió ", perdidas, " veces")
        if ganadas > 1 and perdidas > 1:
            print(nombre, " ganó", ganadas, " veces y perdió ", perdidas, " veces")
        print("""
    ╔══════════════════════════════════════════════════╗
    ║                       __                                  ║
    ║                     .'  '.                                ║
    ║                 _.-'/  /  \                               ║
    ║    ,        _.-"  ,|  /  0 `-.                            ║
    ║   | \    .-"       `--""-.__.'======================'     ║
    ║    \ '-'`        .___.--._)=========================|     ║
    ║     \            .'      |                          |     ║
    ║      |      ,_.-'        |         GRACIAS          |     ║
    ║    _/   _. (             |           POR            |     ║
    ║   /  ,-' \  \            |          JUGAR           |     ║
    ║   \  \    `-'            |                          |     ║
    ║    `-'                   ----------------------------     ║
    ║                                                           ║
    ╚══════════════════════════════════════════════════╝
        """)


main()

def hola(matriz):
    edad = 0
    filas = len(matriz)-1
    columnas = len(matriz[0])-1
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == "Sexo":
                var = j
                if matriz[i][var] == "F":
                    if matriz[i][j] == "Recuperado":
                        var2 = j
                        if matriz[i][var2] == "Recuperado":
                            if matriz[i][j] == "Edad":
                                var3 = j
                                for z in range(1,filas):
                                    matriz[i][var] = int(matriz[i][var])
                                    if matriz[i][var3] > edad:
                                        edad = matriz[i][var2]
    print(edad)
#                            
def main():    
    """ Funcion Principal """
    fila = 0
    matriz = []
    cont = 0
    linea = 0
    edad_mujer = 0
    archivo = open("proyecto3.txt","r",encoding="utf8")
    while linea != "":
        linea = archivo.readline()
        fila = linea.split(",")
        matriz.append(fila)
        cont += 1
    hola(matriz)
main()

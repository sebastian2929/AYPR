#Cristian David Naranjo Orjuela
#Sebastian David Blanco Rodriguez
def compara(lista_cadena, lista_palabras, solucion):
    """ Esta funcion busca la palabra en las diferentes cadenas de caracteres
    (list, list) -> None
    """
    temp = ""
    respuesta = ""
    for i in range(len(lista_cadena)):
        for j in range(len(lista_palabras)):
            cadena = lista_cadena[i]
            palabra = lista_palabras[j]
            for l in range(len(palabra)):
                for k in range(len(cadena)):
                    caracter = palabra[l]
                    if caracter == cadena[k]:
                        print(caracter, cadena[k])
                        temp = temp + caracter
                        print(temp)
                        if temp == palabra:
                            respuesta = palabra
                            solucion.append(respuesta)
                            temp = ""
    return solucion
#
def main():
    """ Funcion Principal """
    stop = 1
    lista_cadena = []
    lista_palabras = []
    solucion = []
    while stop == 1:
        cadena = input("Digite la cadena de caracteres: ")
        if cadena != "0":
            lista_cadena.append(cadena)
        if cadena == "0":
            stop = 0
    while stop == 0:
        palabras = input("Digite la palabra: ")
        if palabras != "":
            lista_palabras.append(palabras)
        if palabras == "":
            stop = 2
    solucion = compara(lista_cadena, lista_palabras, solucion)
    var = len(solucion)
    if var == 0:
        print("No existe la palabra")
    if var != 0:
        for a in range(len(solucion)):
            print(solucion[a])
main()

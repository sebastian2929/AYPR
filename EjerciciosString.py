#Sebastian David Blanco Rodriguez

def promedio(lista):
    """ Calcula el promedio de los datos
    (list) -> float
    """
    sumar = 0
    media = 0
    for i in range(len(lista)):
        sumar += lista[i]
    media = sumar / len(lista)
    return media
#
 
    


def main_varianza():
    """ Funcion principal de la varianza """
    print("   FUNCION VARIANZA   ")
    lista = input("Digite una lista de numeros separados por comas: ").split(",")
    media = 0
    for i in range(len(lista)):
        lista[i] = float(lista[i])
    media = promedio(lista)
    #varianza(lista,media)
main_varianza()
#
def distancia_mayor(lista):
    """ Encuentra la mayor distancia entre los valores de una lista de enteros
    (list) -> int
    """
    mayor = lista[0]
    menor = lista[0]
    distancia = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
        if lista[i] > mayor:
            mayor = lista[i]
    distancia = mayor - menor
    return distancia
#
def main_distancia():
    """ Funcion principal de la mayor distancia """
    print(" ")
    print("   FUNCION MAYOR DISTANCIA   ")
    lista = input("Digite una lista de numeros separados por comas: ").split(",")
    distancia = 0
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    distancia = distancia_mayor(lista)
    print(str(distancia))

main_distancia()
#
def nombres(nombre):
    """ Encuentra el nombre de la persona correspondiente al correo\
        institucional
        (str) -> str
    """
    var = 0
    cont = 0
    oracion = ""
    for i in nombre:
        if "-" in nombre: 
            if i == "-":
                var = cont
        else:
            if i == "@":
                var = cont
        cont += 1
    nombre = nombre[0:var]
    nombre = nombre.split(".")
    for i in nombre:
        oracion += i
    oracion = " ".join(nombre)
    oracion = oracion.title()
    return oracion
#
def main_nombres():
    """ Funcion principal de encontrar el nombre """
    print("")
    print("   FUNCION NOMBRE ESTUDIANTE   ")
    nombre = input("Escriba el correo: ")
    nombre = nombres(nombre)
    print(nombre)

main_nombres()
#

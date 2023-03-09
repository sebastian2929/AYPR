def crear(lista):
    agregar = input("escribir: ")
    lista.append(agregar)
    return lista
def posicion(lista):
    esta = input("digite: ")
    for i in range(0,len(lista)):
        if esta == lista[i]:
            k = i
            lista = lista[k:] + lista[:k]
            print(lista, "CAMBIO")
            return k

def main():
    lista = list()
    parar = "no"
    while parar == "no":
        lista = crear(lista)
        print(lista, "lista sin cambio")
        posi = posicion(lista)
        print("la posicion es: ", posi)
        parar = input("DESEA PARAR (si/no): ")
main()

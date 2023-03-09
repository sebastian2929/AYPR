#Sebastian David Blanco Rodriguez

def invertir(lista):
    """esta funcion invierte los valores en un arreglo
    (list) -> (list)
    """
    if lista == []:
        inversa = lista
    else:
        inversa = [lista[-1] + invertir(lista[:-1])
    return inversa
#
def main():
    """funcion principal"""
    lista = input("digite los valores separados por comas: ").split(",")
    for i in range(0, len(lista)):
        lista[i] = int(lista[i])
    invertir = invertir(lista)
    print(invertir)
    

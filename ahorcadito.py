#Sebastian David Blanco Rodriguez
import random

def buscar(palabra, letra, incognitas):
    """ duncion que asigna la letra en la posicion correcta
    (str, str, list) -> list
    """
    for i in range(0, len(palabra)):
        if palabra[i] == letra:
            incognitas[i] = letra
        return incognitas
            

def main():
    
    bancopal = ["anota","aguja","ahora","nacer","vacio"]
    p = random.randint(0,len(bancopal)-1)
    palabra = bancopal[p]
    incognitas = ["_" for i in range(len(palabra))]
    print(*incognitas)
    intentos = len(palabra) + 2
    i = 0
    adivina = False
    while i < intentos and not adivina:
        letra = input("Diga letra: ").lower()
        if letra in palabra:
            incognitas = buscar(palabra, letra, incognitas)
            print(*incognitas)
        else:
            for i in range(0, i+1):
                print(pierde[i], end = "")
            print()
        i = i + 1
main()


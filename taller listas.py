#Sebastian David Blanco Rodriguez

#Punto 2
def lista_espacios(lista):
    """
     Imprime una lista en una sola línea separando con un espacio los elementos
    (list) -> none
    """
    for valor in lista:
        print(valor, end = " ")
#        
#Punto 3  
def lista_linea(lista):
    """
     Imprime la lista, un elemento por línea
     (list) -> none
     """
    for valor in lista:
        print(valor)
#
#Punto 4
def elementos_lista(lista):
    """
    Dice cuántos elementoshay en la lista
    (list) -> int
    """
    elementos = len(lista)
    return elementos
#
#Punto 5
def pares(lista):
    """
    Dice cuántos valores pares hay en la lista
    (list) -> int
    """
    contador = 0
    for i in range(0,len(lista)):
        if lista[i] % 2 == 0:
            contador = contador + 1
    return contador
#
#Punto 6
def mitad_final(lista):
    """
    Imprime los elementos ubicados en las posiciones de la mitad hasta el final
    (list) -> (list)
    """
    mitad = len(lista) // 2
    mitad_final = lista[mitad:]
    return mitad_final
#
#punto 8
def separar(lista):
    """
    Separa en dos listas los elementos de la primera posición hasta la mitad y los elementos de la 
    mitad más uno hasta el final
    (lista) -> (list, list)
    """
    mitad = len(lista) // 2
    mitad_final = lista[mitad:]
    inicio_mitad = lista[0:mitad]
    return inicio_mitad, mitad_final       
#
#punto 9
def unir(lista):
    mitad = len(lista) // 2
    mitad_final = lista[mitad:]
    inicio_mitad = lista[0:mitad]
    lista = mitad_final + inicio_mitad
    return lista
#
#10
def menor_val(lista):
    """
    Obtiene el menor valor de toda la lista
    (list) -> int
    """
    menor = 999
    for i in range(0,len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor
#
#11
def mayor_val(lista):
    """
    Obtiene el mayor valor de toda la lista
    (list) -> int
    """
    mayor = -999
    for i in range(0,len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor
#
#12
def esta(lista, valor):
    """
    Dice si un valordado se encuentra en la lista
    (list, int) -> (bool)
    """
    for i in range(0, len(lista)):
        if valor == lista[i]:
            return True
    return False
#
#13
def pos_lista(lista):
    """
    Entrega la posición de un valor dado en la lista.
    (list) -> int
    """
    valor = int(input("Digite un valor para saber su posicion en el arreglo: "))  
#    
#14
def segundo_cambio(lista):
    """
    Modifica el valor del segundo elemento en la lista con un valor cualquiera leído desde teclado
    (list) -> (list)
    """
    valor = input("Digite un valor para cambiar en el segundo elemento de la lista: ")
    for i in range(0, len(lista)):
        lista[1] = valor
    return lista
#
#15
def eliminar_ultimo(lista):
    """
    Elimina el último elemento de la lista
    (list) -> (list)
    """
    ultimo = len(lista) - 1
    lista = lista[:ultimo]
    return lista
#16
def eliminar_cualquier(lista):
    """
    Elimina un valor dado de la lista
    (list) -> (list)
    """
    valor = int(input("Digite el valor que desea eliminar"))
    for i in range(0, len(lista)):
        if lista[i] == valor:
            lista[i] = lista[:]
    return lista
#
#20
def corchete_comas(lista):
    """
    Imprime la lista con corchetes y comas
    (list) -> (list)
    """
    print(lista)
#
#21
def invertido(lista):
    """
    Entrega los elementos de la lista en orden invertido
    (list) -> (list)
    """
    longitud = len(lista)
    for i in range(longitud):
        lista = (lista[longitud-i-1])
        print(lista)

#
def main():
    """
    Funcion principal
    """
    
    lista = input("Digite una secuencia de numeros separados por comas: ").split(",")
    for i in range(0, len(lista)):
        lista[i] = int(lista[i])
        
    print(">>>punto 1<<<")
    print(lista)
    
    print(">>>punto 2<<<")
    lista_espacios(lista)
    
    print("")
    print(">>>punto 3<<<")
    lista_linea(lista)
    
    print(">>>punto 4<<<")
    elemen = elementos_lista(lista)
    print(elemen)

    print(">>>punto 5<<<")
    cont_par = pares(lista)
    print(cont_par)

    print(">>>punto 6<<<")
    mid_fin = mitad_final(lista)
    print(mid_fin)

    print(">>>punto 8<<<")
    div_lista = separar(lista)
    print(div_lista)

    print(">>>punto 9<<<")
    union = unir(lista)
    print(union)
    
    print(">>>punto 10>>>")
    menor = menor_val(lista)
    print(menor)

    print(">>>punto 11<<<")
    mayor = mayor_val(lista)
    print(mayor)
   

    print(">>>punto 12<<<")
    valor_arreglo = int(input("Digie un valor entero que quiere saber si se encuentra en el arreglo: "))
    if esta(lista, valor_arreglo):
        print("El valor si esta en el arreglo")
    else:
        print("El valor no esta en el arreglo")

    print(">>>punto 14<<<")
    pos_dos = segundo_cambio(lista)
    print(pos_dos)

    print(">>>punto 15<<<")
    eliminar_ult = eliminar_ultimo(lista)
    print(eliminar_ult)

    print(">>>punto 16<<<")
    #elimiar_algo = eliminar_cualquier(lista)
    #print(eliminar_algo)

    print(">>>punto 20<<<")
    corchete_comas(lista)

    print(">>>punto 21<<<")
    #invertido(lista)   
    
main()

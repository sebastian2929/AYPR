#Sebastian David Blanco Rodriguez

def triangulo(altura):
    """
    Segun una altura dada se imprime un triangulo
    (int) -> (none)
    """
    cont = 0
    resultado = "*"
    while cont < altura:
        print(resultado)
        cont = cont + 1
        resultado = "*" + resultado

   
def main():
    """ Funcion principal """
    altura = int(input("Digite la altura del triangulo: "))
    triangulo(altura)
    
main()

#trigonometria
def factorial(n):
    """ calcula factorial
    (int) -> int
    """
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact
#
def potencia(base, exp):
    """calcula una potencia
    (int, int) -> int
    """
    return base**exp
#
def termino(x,p):
    """ Funcion calcula valor de la serie
    (int, int) -> float
    """
    return potencia(x,p) / factorial(p)
#
def seno(x,t):
    """
    Se calcula la función trigonométrica seno(x) con ayuda de la serie de Taylor
    (int, int) -> (float)
    """
    acum = 0
    p = 1
    signo = 1
    for i in range(t):
        acum = acum + termino(x,p) * signo
        p = p + 2
        signo = signo * (-1)
    return acum
#           
def main():
    x = int(input("Digite el valor de x: "))
    t = int(input("Digite de cunatos terminos son: "))
    resp = seno(x, t)
    print(resp)
main()


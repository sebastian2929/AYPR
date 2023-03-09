def primo(valores):
    for i in valores:
        for j in range(2, i):
            if i % j == 0:
                return False
        return True

    
def main():
    valores = input("digite una secuencia de numeros separados por comas: ").split(",")
    for i in range(0, len(valores)):
        valores[i] = int(valores[i])
    primo(valores)


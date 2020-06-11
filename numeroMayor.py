"""
Programador Hernandez Rojas Mara Alexandra Práctica 10
Este programa encuentra el numero mayor de tres candidatos
con las estructuras de seleccion if, elif, else en python
"""
def numeroMayor(a, b, c):
    if a > b and a > c:
        print("El numero mayor es {} ".format(a))
    elif( b > c and b > a):
        print("El numero mayor es {} ".format(b))
    else:
        print("El numero mayor es {} ".format(c))


if __name__ == "__main__":
    a = int(input("Numero: "))
    b = int(input("Numero: "))
    c = int(input("Numero: "))
    numeroMayor(a, b, c)

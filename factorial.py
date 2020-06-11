"""
Programador Hernandez Rojas Mara Alexandra Practica 10
Factorial con ciclo while 
"""
def fact(a):
    i = 2
    t = 1
    while i<=a:
        t = t * i
        i = i + 1
    return t

if __name__ == "__main__":

    a = int(input("Ingrese un numero: "))
    print(fact(a))

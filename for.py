"""
Programador Hernandez Rojas Mara Alexandra Practica 10
Este programa ejemplifica como usar la estructura de control for en phyton

For para listas
"""
def forlist():
    for x in [1, 2, 3, 4, 5]:
        print(x)

"""
For para rangos
"""
def forrange():
    for x in range(5):
        print(x)

    for y in range(-3, 3):
        print(y)

    for z in range(-4, 2, 1):
        print(z)

    for i in range(5, 0, -1):
        print(i)

"""
For para diccionarios
"""
def fordic():
    diccionario = {'manzana': 1, 'pera':3, 'uva':10}
    for clave, valor in diccionario.items():
        print(clave," - ",valor)

    for clave in diccionario.keys():
        print(clave)

    for valor in diccionario.values():
        print(valor)

    for idx, x in enumerate(diccionario):
        print("El indice {} del elemento {}".format(idx, x))

"""
Else de for
"""

def elsefor():
    for x in range(5):
        print(x)
    else:
        print("La cuenta se termino")


def elsefor2():
    for x in range(5):
        print(x)
        if x== 2:
            break
    else:
        print("la cuenta se termino")
    print("\nNunca entro a else\n")

"""
En else for 2
Se rompio el ciclo y nunca entra al eslse
"""


if __name__ == "__main__":
    print("for de lista")
    forlist()
    print("for de rango")
    forrange()
    print("for de diccionario")
    fordic()
    print("elsefor")
    elsefor()
    print("elsefor2")
    elsefor2()

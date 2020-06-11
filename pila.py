"""
Programador Hernandez Rojas Mara Alexandra Práctica 10
Este programa muestra como usar una lista a manera de pila en Python
"""

def insertar(lista, dato):
    #por el principio
    lista.append(dato) #Agregar al final


def borrar(lista):
    dato = lista.pop()
    return dato


def imprimir_pila(lista):
    lista.reverse()
    for x in lista:
        print(x)
    print()
    lista.reverse()


def main():
    pila = [0]
    insertar(pila, 1)
    insertar(pila, "lista")
    insertar(pila, 2)
    print()
    print(borrar(pila))
    imprimir_pila(pila)


if __name__ == "__main__":
    main()

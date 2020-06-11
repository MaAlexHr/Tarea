"""
Programador Hernandez Rojas Mara Practica 10
Este programa muestra como importar bibliotecas en python

Primera Forma
Importa absolutamente todo en la biblioteca y cuando lo ocupas te refieres
a las funciones iniciando por el nombre de la biblioteca
"""
import math
x = math.cos(math.pi)
#print(x)

"""
Segunda forma de importar
Solo es necesario escribir el nombre de la funcion, sigue importando todo
"""

from math import *
x = cos(pi)
#print(x)

"""
Tercera 
Puedes cambiar el apodo de las bibliotecas al importarlas
"""
import math as ma
x = ma.cos(ma.pi)
#print(x)

"""
Cuatra 
Importa solo ciertas funciones y solo escribes sus nombres
"""
from math import cos, pi
x = cos(pi)
print(x)

"""
Programdor Hernandez Rojas Mara Alexanra Practica 10
Esta es la gráfica que viene en el manual de prácticas de la asignatura
"""
#%pylab inline esta linea genero un error

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import *

x = linspace(0, 5, 20)

fig, ax = plt.subplots(facecolor='w', edgecolor='k')
ax.plot(x, sin(x), marker="o", color="r", linestyle='None')

ax.grid(True)
ax.set_xlabel('X') 
ax.set_ylabel('Y') 
ax.grid(True)
ax.legend(["y = x**2"])

plt.title('Puntos')
plt.show()

fig.savefig("graf.png") #El resultado se va a guardar con este nombre


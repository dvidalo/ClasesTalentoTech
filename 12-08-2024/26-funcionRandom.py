# Nombre del módulo
# from random import *
# * = Todos los métodos
# También pueden importarse de manera
# independiente aquellos a utilizar.

# randint(min, max): devuelve un integer entre dos valores dados (ambos límites
# incluidos)

# uniform(min, max): devuelve un float entre un valor mínimo y uno máximo

# random(sin parámetros): devuelve un float entre 0 y 1

# choice(secuencia): devuelve un elemento al azar de una secuencia de valores
# (listas,tuples,rangos, etc.)

# shuffle(secuencia): toma una secuencia de valores mutable (como una lista), y la
# retorna cambiando el orden de sus elementos aleatoriamente.

# * La mecánica en cómo se generan dichos valores aletorios viene en realidad predefinida en "semillas". Si
# bien sirve para todos los usos habituales, no debe emplearse con fines de seguridad o criptográficos, ya
# que son vulnerables.

from random import *

# aleatorio = randint(1,50)
# print(f"randint entre 1 - 50 = {aleatorio}")

# aleatorio = uniform(1,5)
# print(f"uniform entre 1 - 5 da {aleatorio}")

# aleatorio=random()
# print(f"Random da {aleatorio}")

colores=['azul','rojo','verde','amarillo']
aleatorio = choice(colores)
print(f"choice da un elemento de la lista asi {aleatorio}")


aleatorio = shuffle(colores)
print(colores)



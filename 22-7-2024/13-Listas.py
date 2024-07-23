# secuencia ordenada de elementos string, int, float o todos
mi_lista=['a',10,25.6,'hola']
lista=['a','b','c','d']
lista_de_lista=[['a','b'],[1,2],[2,2.3]]

# se puede consultar el tipo de variable que es
print(type(mi_lista))

# acceder similar a los strnig print(lista[inicio:fin:salto])
print(mi_lista[0:3:2])
# se puede utilizar len para indentificar el tamaño de la lista
print(len(mi_lista))

# index para buscar y retornar la ubicacion del elemento a buscar
print(lista.index("c"))
# imprim el elemento que se encuentra en la ubicacion 2
print(lista[2])
# imprimir todos los elementos
print(mi_lista[:])

# los elementos de la lista si pueden modificarse lista[ubicacion]="dato nuevo"
mi_lista[0]='alfa'
print(mi_lista[:])

# agregar elementos
mi_lista.append('z')
print(mi_lista)

# eliminar elemento de una lista, por defecto elimina el ultimo
# en el () se puede escribir la ubicacion para eliminar lo que este en esa ubicacion
mi_lista.pop()
print(mi_lista)

mi_lista.pop(0)
print(mi_lista)

# si se tiene una lista desordenada yaq sea letras o ya sean numeros
# 
lista=['l','b','i','a']
print(lista)

# .sort() organiza la lista alfabeticamente o creciente
lista.sort()
print(lista)

# .reverse() orgniza de manera contraria a alfabeticamente o decreciente
lista.reverse()
print(lista)
lista.reverse()
print(lista)
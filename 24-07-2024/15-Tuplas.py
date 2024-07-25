# las tuplas no son mutables, no se pueden hacer cambios
mi_tupla=(1,2,3,4)
print(mi_tupla)
# Ordenados y aceptan duplicados
# se puede tener listas dento de la lista y acceder a ellos
mi_tupla = (1,2,(10,20),4)
print(mi_tupla[2][1])
# se puede castear una tupla a una lista
mi_tupla=list(mi_tupla)
print(mi_tupla)
# y puede cambiarse de lista a tupla
mi_tupla=tuple(mi_tupla)
print(mi_tupla)

# se pueden asignar los valores a variables si conocemos el total de elementos asi
mi_tupla=(1,2,3,4)
x,y,z,w = mi_tupla
print(x,y,z,w)

# se puedeutilizar la funcion len(tupla) para concer la cantidad de elementos
print(len(mi_tupla))

# se p uede utilizar la funcion tupla.count(valorbuscar) para contar canidad de veces que se repite
mi_tupla=(1,2,3,4,1,1)
print(mi_tupla.count(1))
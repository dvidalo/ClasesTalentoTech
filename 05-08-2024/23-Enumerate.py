# lleva la cuenta a traves de contadores ej. enumerate(inteable, inicio)
# inicia en 0
print(list(enumerate("Hola")))

for indice , numero in enumerate([5.55, 'G', 7.50]):
    print(indice, numero)

lista = ['a','b','c']

for item in enumerate(lista):
    print(item)

for x,item in enumerate(lista):
    print(x,item)
    
for x,item in enumerate(range(50,55)):
    print(x, item)
    
mi_tupla = list(enumerate(lista))
print(mi_tupla)
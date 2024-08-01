nombres=['juan','pedro','carlos','belen']

# Formato for, va a pasar por cada item en la lista, o arreglo o lo que se requiera
# Por Cada elemento en la variable, imprime un hola
for item in nombres:
    print("hola")

# iten hace referencia a cada elemento, podemos imprimir cada elemento asi
for item in nombres:
    print(item)
    
#  puede darse un nombre de variable e imprimir los elementos de un str
MInombre = "DIEGO"

for x in MInombre:
    print(x) 



# Ejemplos de utilizacion del for
for x in MInombre:
    num=MInombre.index(x)+1
    print(f"Letra {num}: {x} ")

for x in 'DIEGO':
    print(x)

for nomb in nombres:
    num=nombres.index(nomb)+1
    if nomb.startswith('c'):
        print(f"el nombre numero {num}: es {nomb}")
    else:
        print(f"el nombre numero {num} no inicia con \"c \"")

# Cuando se tienen arreglos se pueden relacionar varios elementos para imprimir la posicion de cada uno
for a in [[1,2],[3,4],[5,6]]:
    print(a)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)

# For en diccionarios

dic = {'clave1':'a','calve2':'b','clave3':'c'}

for item in dic:
    print(item)

for item in dic.items():
    print(item)

for item in dic.values():
    print(item)
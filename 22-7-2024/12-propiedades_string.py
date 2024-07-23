nombre = "karolina"
print(nombre)
''' no se puede cambiar la letra k por una c'''
n1="karo"
n2="lina"

print(n1+n2)
# si adicionamos * y el numero, nos imprime varias veces lo que este antes
print(n2*5)
# con triples comilas dobles se puede asignar o imprimir con salto de linea un string
poema="""
No todo es días de sol
y la lluvia cuando falta mucho, se pide.
Por eso tomo la infelicidad con la felicidad.
Naturalmente como quien no se extraña
con que existan montañas y planicies y que haya rocas y hierbas…
Lo que es necesario es ser natural y calmado en la felicidad o en la
infelicidad."""

print("""tambien se puede concatenar para ver en pantalla
      
      reconoce los saltos de linea
      
      y se puede agregar la variable"""+poema)
# in y not in para consultar si esta el contenido en una variable retorna false/ true or o/1
print("consultamos si esta la palabra agua")
print("agua"in poema)

print("consultamos si infelicidad esta en el texto")
print("infelicidad"in poema)

print("consultamos si no esta la palabra agua")
print("agua" not in poema)

print("consultamos si infelicidad no esta en el texto")
print("infelicidad"not in poema)
rta=int("infelicidad"not in poema)
print(rta)

# consultar el tamaño de una variable
print(len(poema))
# se busca concatenar variables con string o cadenas
# se da el valor a dos variables
x = 10
y = 5
suma= x+y
# se ingresan corchetes en las opciones donde quieres mostrar la variable 
# y posterior se visualizen, se define con .format, que variables irian en cada corchete

print("mis numeroes son {} y {}".format(x,y))
print("mis numeroes son {} y {}".format(y,x))
print("la suma de {} mas {} es igual a {}".format(x,y,suma))
print("la suma de {} mas {} es igual a {}".format(x,y,x+y))

# otra opcion es con la ocion de anteponer la f en una cadena

color="rojo"
matricula = 75451

print(f"el color es {color} y la matricula es {matricula}")
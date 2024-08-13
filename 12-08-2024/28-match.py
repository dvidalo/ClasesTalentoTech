# En Python 3.10, se incorpora la coincidencia de patrones
# estructurales mediante las declaraciones match y case. Esto
# permite asociar acciones específicas basadas en las formas o
# patrones de tipos de datos complejos.


# opc = int(input("ingresa un numero de 1 a 3"))

# match opc:
#     case 1:
#         print("entro en uno")
#     case 2:
#         print("entro en dos")
#     case 3:
#         print("entro en 3")


cliente= {'nombre':'luis','edad':45,'ocupacion':'docente'}
pelicula={'titulo':'matrix','ficha_tecnica':{'protagonista':'keanu reeves','director':'lana'}}
elemento=[cliente, pelicula,'libro']        

for el in elemento:
    match el:
        case {'nombre': nombre,'edad':edad,'ocupacion':ocupacion}:
            print('es un cliente')
            print(nombre, edad, ocupacion)
        case{'titulo':titulo,'ficha_tecnica':{'protagonista':protagonista,'director':director}}:
            print("es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print('es un libro')
# Practica 1

capitales=["Berlin","Tokio","Paris","Helsinki","Ottawa,Canberra"]
Paises=["Alemania","Japon","Francia","Finlandia","Canada","Australia"]

for pais,capital in zip(Paises,capitales):
    print(f"La capital de {capital}, es {pais}")
    
# Practica 3

marcas=["Suzuki", "Yamaha","Honda","Victory"]
Producto=["Motos","Motores","Automovil","MOtocicletas"]
mi_zip=zip(marcas,Producto)
for m,p in zip(marcas,Producto):
    print(f"la marca {m} produce {p}")

# Practica 3
español=["uno","dos","tres","cuatro","cinco"]
ingles = ["one","two","three","four","five"]
Portugues=["um","dois","tres","quatro","cinco"]
lista_numeros=list(zip(español,ingles,Portugues))
print(lista_numeros)
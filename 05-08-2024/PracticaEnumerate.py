# Practica 1

Lista_nombres=["Marcos", "Laura", "Monica", "Javier", "Celina","Martha","Dario","Emiliano","Melisa"] 
for indice,nombre in enumerate(Lista_nombres):
    print(f"{nombre} se encuentra en el indice {indice}")
    
# Practica 2
Lista_Indice = list(enumerate("Python"))
print(Lista_Indice)

# Practica 3
for i, nombre in enumerate(Lista_nombres):
    if nombre[0]=='M':
        print(f"En el Indicie {i} esta el nombre {nombre}")
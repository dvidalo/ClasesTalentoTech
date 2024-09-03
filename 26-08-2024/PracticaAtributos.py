
# practica 1
class Casa:
    def __init__(self,color,cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa('blanco','4')

print(f"PRACTICA NRO 1 \nla casa es de color {casa_blanca.color} y tiene {casa_blanca.cantidad_pisos} pisos")

# practica 2
class Cubo:
    caras = 6
    def __init__(self,color):
        self.color=color

cubo_rojo=Cubo('rojo')

print(f"\nPRACTICA 2 \nel color del cubo es {cubo_rojo.color} y tiene {Cubo.caras}")

class Personaje:
    real = False
    def __init__(self,especie,magico,edad):
        self.especie=especie
        self.magico=magico
        self.edad = edad
harry_potter= Personaje('humano',True,17)

print(f"\nPRACTICA 3 \nEl personaje es {harry_potter.especie}, es {harry_potter.magico} y tiene {harry_potter.edad}")
                
        

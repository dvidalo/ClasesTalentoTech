class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

print(Alumno.__bases__)

class Mascota:
    def __init__(self,edad, nombre, cantidad_patas):
        self.edad=edad
        self.nombre=nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass

print(Perro.__bases__)
        
class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass

print(Automovil.__bases__)


        
        
class Perro:
    pass
    def ladrar(self):
        print("Guau!")
        
pluto = Perro()
pluto.ladrar()

class Mago:
    pass
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin=Mago()
merlin.lanzar_hechizo()

class Alarma:
    pass
    def postergar(self,cantidad_minutos):
        print(f"la alarma ha sido pospuesta {cantidad_minutos}")
        
minutos=Alarma()
minutos.postergar(5)
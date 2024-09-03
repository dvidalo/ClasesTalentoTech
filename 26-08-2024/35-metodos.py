class pajaro:
    alas = True
    
    def __init__(self,color, especie) :
        self.color=color
        self.especie = especie
    
    def piar(self):
        print(f"ingresaste al pajaro de color {self.color} de la especie {self.especie}")
        
    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")

piolin = pajaro('amarillo','canario')
piolin.piar()
piolin.volar(40)
print(f"color {piolin.color}")

# METODO INSTANCIA, REQUIEREN INSTANCIA, PUEDE ACCEDER ATRIBUTOS, PUEDE CAMBIAR ATRIBUTOS

class pajaro:
    alas = True
    
    def __init__(self,color, especie) :
        self.color=color
        self.especie = especie
    
    def piar(self):
        print(f"ingresaste al pajaro de color {self.color} de la especie {self.especie}")
        
    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")
# metodos de instancia pueden cambiar los atributos del objeto
    def cambiar_negro(self):
        self.color='negro'
# metodo de clase, puede acceder a metodos y atributos de la clase pero no requiere instancia
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        alas=False
    
    @staticmethod
    def mirar():
        print(f"El pajaro mira")

piolin = pajaro('amarillo','canario')
piolin.piar()
piolin.cambiar_negro()
piolin.piar()
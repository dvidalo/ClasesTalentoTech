class Animal:
    def __init__(self,edad,color):
        self.color = color
    
    def nacer(self):
        print("Este animal ha nacido")
    
class Pajaro(Animal):
    pass


piolin =Pajaro(2,"amarillo")
piolin.nacer()

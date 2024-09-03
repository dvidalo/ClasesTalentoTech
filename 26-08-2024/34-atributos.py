class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

piolin = Pajaro('negro','Tucan')

print(piolin.color)

print(Pajaro.alas)
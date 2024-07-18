# Se relacionan el inicio y fin de la posicion"no se incluye" para mostrar una parte
# x:Y indica desde y hasta se debe fragmetar

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]
print(fragmento)
# x:   indica desde donde inicia y se fragmeta hasta el final

fragmento=texto[2:]
print(fragmento)
# :y  indica desde el inicio hasta la ubicacion

fragmento=texto[:5]
print(fragmento)
# x:y:z inicio, fin y saltos de cuantas bicaciones

fragmento=texto[2:10:2]
print(fragmento)
# ::z   se indica que muestre de dos en dos hasta el firnal 
fragmento=texto[::2]
print(fragmento)
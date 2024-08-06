# moneda = 5
# while moneda >0:
#     print(f"tengo {moneda} monedas")
#     moneda -=1
    # Es lo mismo que indicar moneda = moneda -1

# respuesta = 'n'

# while respuesta =='n':
#     respuesta = input("quieres salir? (s/n)")
    
# while respuesta =='s':
#     pass

nombre = input("ingrese nombre: ")

for letra in nombre:
    if letra =='r':
        break
    else:
        print(letra)

for letra in nombre:
    if letra =='r':
        continue
    else:
        print(letra)

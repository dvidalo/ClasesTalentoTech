from random import *
numeroSecreto = randint(1,100)
intentos = 0
estimado =0
nombre = input("ingresa tu nombre: ")

print(f"\n Hola {nombre}, \n he pensado un numero de 1 a 100\n solo tienes 8 intentos para que lo adivines")

while intentos < 8:
    intentos+=1
    estimado = int(input(f" {nombre} intento numero {intentos}\ningresa el numero que crees que he pensado"))
        
    if estimado < numeroSecreto:
        print("Mi numero es mayor")
    elif estimado > numeroSecreto:
        print("mi numero es menor")
    else:
        print(f"Felicidades {nombre}, Has ganado en {intentos} intentos")
        break
    
print(f"Lo sentimos {nombre} ya cmpletaste tus 8 intentos, mi numero era {numeroSecreto}")    
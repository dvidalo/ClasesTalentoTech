# practica 1
# num1= int(input("ingresa un numero: "))
# num2 = int(input("Ingresa otro numero: "))

# if num1>num2:
#     print(f"{num1} es mayor que {num2}")
# elif num2 >num1:
#     print(f"{num2} es mayor que {num1}")
# else:
#     print(f"{num1} y {num2} son iguales")
    

#  Practica 2

# licencia='si'in input("Tiene Licencia responda si o no: ").lower()
# edad=int(input("Ingrese su edad: "))

# if licencia and edad>=18:
#     print("puedes conducir")

# elif edad<18 and licencia == False:
#     print("no puedes conducir aun, debes tener 18 años y contar con una Licencia")

# elif edad>=18 and licencia==False:
#     print("no puedes conducir. Necesitas contar con una Licencia")
# else:
#     print("Verifica los datos porque no puedes tener licencia si tienes menos de 18 años")

# Practica 3

HablaIngles = 'si' in input("Hablas ingles (responde si o no): ").lower()
SabePython =  'si' in input("Programas en Python (responde si o no): ").lower()

if HablaIngles and SabePython:
    print("Cumples con los requisitos para postulare")
elif HablaIngles == False and SabePython:
    print("Para POstularte, necesitas tener conocimiento en Ingles")
elif SabePython== False and HablaIngles:
    print("Para POstularte, necesitas saber programar en Python")
else:
    print("Para POstularte, necesitas saber programar en Python y tener conocimiento en Ingles")
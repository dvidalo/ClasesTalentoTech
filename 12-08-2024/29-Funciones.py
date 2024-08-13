# Una función es un bloque de código que solamente se ejecuta
# cuando es llamada. Puede recibir información (en forma de
# parámetros), y devolver datos una vez procesados como
# resultado

# Se crea la funcion para saludar, recibe un string con un nombre
def saludo(nombre):
    print(f"Hola {nombre}")
    
# El codigo no se ejecuta desde la funcion
nombre=input("ingresa tu nombre")
saludo(nombre)

def sumar (a,b):
    suma=a+b
    return[suma]

numero1 = int(input("Ingresa numero 1: "))
numero2 = int(input("Ingresa numero 2"))
print(sumar(numero1,numero2))
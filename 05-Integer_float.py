numero1 = 1
print(numero1)

numero2 = 2.4
print(numero2)

#se verifica el tipo de variable que tenemos con la palabra type()

print("el numero 1 es de tipo ",type(numero1))
print("el numero 2 es de tipo ",type(numero2))

#si se suma un entero con un flotante, automaticamente la variable termina siendo flotante

suma= numero1+numero2

print("la suma es ",suma)
print("el tipo de la suma es ",type(suma))

#cualquier informacion que ingrese por teclado es tomado como string, asi el dato sea un numero

numero1=input("Ingrese un numero: ")
print(type(numero1))

#para pasar valor de variable a entero se utiliza int("variable"), la cual debe asignarse a una variable

numero1=int(numero1)
print(type(numero1))

suma=numero1+numero2
print("Suma de numeros flotante es: ",suma)
print(type(suma))
suma=int(suma)

print("Suma en Enteros: ",suma)
print(type(suma))
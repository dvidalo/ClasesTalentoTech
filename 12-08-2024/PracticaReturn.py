print("Practica 1:\n")
def potencia(base,exponente):
    resultado = base**exponente
    return resultado

numero1 = int(input("Ingresa la Base: "))
numero2 = int(input("Ingresa la Potencia: "))

print(f"la potencia de {numero1} elevado a {numero2} es {potencia(numero1,numero2)}")

print("\nPractica 2: \n")
def usd_a_eur(dolar):
    eur=dolar*0.90
    return eur
dolares=float(input("Ingrese el valor en dolares: "))
print(f"${dolares} dolares equivalen a {usd_a_eur(dolares)} Euros")

print("\nPractica 3\n")
def intvertir_palabra(palabra):
    invertida=(palabra[::-1]).upper()
    return invertida
PalabraOriginal=input("Ingrese una palabra: ")
print(intvertir_palabra(PalabraOriginal))
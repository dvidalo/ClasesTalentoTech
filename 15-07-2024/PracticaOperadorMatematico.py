
import math

# se utiliza la operacion division / para efectuar la operacion matematica
# se utiliza division al piso //
# Practica Operadores Matematicos 1
x=874
y=27
print(f"division al piso: {x//y}")

# Practica Operadores Matematicos 2
# se utiliza el simbolo % para retomar el resto de una division
x=456
y=33
print(f"el resto es {x%y}")

# Practica Operadores Matematicos 3
# raiz cuadrada, se importa la libreria math o se eleva a la potencia 0.5
x=783

print(f"potencia con math {math.sqrt(x)} o elevado a la potencia {x**0.5}")

# practica redondeo de cifras round(numero, decimales)
# Practica Redondeo 1
x=10
y=3
d=x/y
print(f"redondedo de la division a dos decimales  {round(d,2)}")

# Practica Redondeo 2
x=10.676767
print(f"redondedo de al entero mas cercano {round(x)}")

# PracticaRedondeo 3
x=5
print(f"raiz cuadrada a rendondeo con 4 cifras {round(math.sqrt(x),4)}")
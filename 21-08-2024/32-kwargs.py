# Nos ayuda a crear diccionarios 

def mostrarDicionario (**kwargs):
    print(type(kwargs))
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

# mostrarDicionario(x=3, y=5, z=2)

# cuando una definicion tine varios argumentos al final van los kwargs y enultimo *args

def prueba (num1, num2, *arg, **kwarg):
    print(f"El primer numero es {num1}")
    print(f"el segundo numero es {num2}")
    for arg in arg:
        print(f"arg = {arg}")
    
    for clave, valor in kwarg.items():
        print(f"{clave} = {valor}")

prueba(15,15,100,200,300,400,x=2,y=5,z=4)
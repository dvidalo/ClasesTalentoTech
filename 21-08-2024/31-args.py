# se puede definir una funcion sin argumentos predeterminados

def suma(*args):
    total = 0
    for args in args:
        total += args
    return total

print(suma(4,7,8,1))
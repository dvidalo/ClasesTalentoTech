def suma(*sumandos):
    total = 0
    for sumandos in sumandos:
        total += sumandos
    return total

print(suma(4,7,8,1))
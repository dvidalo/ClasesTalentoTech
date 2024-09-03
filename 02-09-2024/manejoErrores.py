# try:
#     print("Esa todo el codigo a ejecutar")
# except:
#     print("Manejo de Errores")    
# else:
#     print("Es cuando no existe error en el codigo")
# finally:
#     print("Siempre se va a ejecutar asi sea que si o no exista error")


def sumar():
    try:
        n1 = int(input("numero 1: "))
        n2 = int(input("Numero 2: "))
    except ValueError:
        print("Error por favor ingrese solo numeros")
    else:
        print(n1+n2)
    finally:
        print("Terminado")

def dividir():
    try:
        n1 = int(input("Ingrese numerador: "))
        n2 = int(input("Ingrese denominador: "))
        resultado = n1/n2
    except ValueError:
        print("Ingrese solo numeros")
    except ZeroDivisionError:
        print("No puede realizarse un numero entre Cero")
    else:
        print(f"la division de {n1} entre {n2} = {resultado}")
    finally:
        print("Terminado")
dividir()

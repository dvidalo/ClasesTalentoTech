from random import choice

def palabrarandom(lista):
    palabraelegida = choice(lista)
    letras_unicas=len(set(palabraelegida))
    return palabraelegida,letras_unicas

palabras=['panadero', 'dinosaurio', 'helipuerto', 'murcielago', 'tiburon']

letras_correctas =[]
letras_incorrectas =[]
intentos = 6
aciertos = 0
juegoTerminado= False

def pedir_letra():
    letra_elegida = ''
    esvalida= False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not esvalida:
        letra_elegida = input("Ingrese una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida)==1:
            esvalida=True
        else:
            print("No has ingresado una letra correcta\n")
    return letra_elegida

def mostrar_nuevoTablero(palabraelegida):
    listaoculta=[]
    for l in palabraelegida:
        if l in letras_correctas:
            listaoculta.append(l)
        else:
            listaoculta.append('_')
    print(' '.join(listaoculta))

def chequear_letra(letraelegida, palabraoculta, vidas, coincidencias):
    fin = False
    if letraelegida in palabraoculta:
        letras_correctas.append(letraelegida)
        coincidencias +=1
    else:
        letras_incorrectas.append(letraelegida)
        vidas -= 1
    
    if vidas== 0:
        fin = perder()
    elif coincidencias == letras_unicas:    
        fin = ganar(palabraoculta)
    return (vidas, fin, coincidencias)

def perder():
    print("Te has quedado sin vidas")
    print(f"la pallabra oculta era: {palabraelegida}")
    return True

def ganar(palabradescubierta):
    mostrar_nuevoTablero(palabradescubierta)
    print("felicidades has encontrado la palabra")
    return True

palabraelegida, letras_unicas = palabrarandom(palabras)

while not juegoTerminado:
    print("\n" + '*' *20 + "\n")
    mostrar_nuevoTablero(palabraelegida)
    print("\n")
    print('Letras incorrectas: '+'-'.join(letras_incorrectas))
    print(f"Vidas : {intentos}")
    print("\n" + '*' *20 + "\n")
    letra = pedir_letra()
    intentos, terminado, aciertos = chequear_letra(letra, palabraelegida,intentos, aciertos)
    juegoTerminado= terminado
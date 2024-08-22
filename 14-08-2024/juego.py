from random import *

palitos=['-','--','---','----']    

def cambiarorden(lista):
    shuffle(lista)
    return lista
       
     
def ProbarSuerte():
    intento=''
    while intento not in ['1','2','3','4']:
        intento = input("elige un numero entre 1 al 4: ")
    return(int(intento))
        
def chequear(lista,intento):
    if lista[intento-1] == '-':
        print("Lo siento perdiste el juego")
    else:
        print("Esta ves te has salvado")
    print(f"Te ha tocado{lista[intento-1]}")

palitosrandom = cambiarorden(palitos)
seleccion = ProbarSuerte()
chequear(palitosrandom,seleccion)
   
    
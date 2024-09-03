def chequear_3_cifras(numero):
     return numero in range(100,1000)



def revisarLista_3_cifras(lista):
    listade3cifras=[]
    for n in lista:
        if n in range(100,1000):
            listade3cifras.append(n)
        else:
            pass
    return listade3cifras

listafinal=revisarLista_3_cifras([555,45,700,40000])
print(listafinal)



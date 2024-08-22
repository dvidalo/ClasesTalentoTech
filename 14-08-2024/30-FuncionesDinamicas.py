def chequear_3_cifras(numero):
     return numero in range(100,1000)



def revisarLista_3_cifras(lista):
    listade3cifras=[]
    for n in lista:
        b=chequear_3_cifras(n)
        print(b)
        if b:
            listade3cifras.append(n)
        else:
            pass
    return listade3cifras

listafinal=revisarLista_3_cifras([555,45,700,40000])
print(listafinal)



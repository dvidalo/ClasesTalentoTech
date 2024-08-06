# agrupa los elementos del mismo indie provenientes de dos o mas iterables
# Uniria la cantdfad del menor numero de elementos de los arreglos
letras =['w','x','c']
numeros =[50, 65 , 90, 110, 135]
simbolo=['+', '-']

for letra,num,sim in zip(letras,numeros,simbolo):
    print(f"Letra {letra} y NUmero: {num}, Simbolo{sim}")
    
nombres=['ana', 'Luis', 'Antonio']
edades=(25,40,32)

combinados=zip(nombres,edades)
print(combinados)

combinados=list(combinados)
# combinados=list(zip(nombres,edades))
print(combinados)


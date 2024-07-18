# MAYUS  variable.upper()
texto=" este es un texto implementado en Python "
print(texto.upper())
print(len(texto))
# se puede utilizar el index para indicar cual pasar a a mayusculas
print(texto[1:5].upper())

# minus  variable.lower()
print(texto.lower())

# split()  separar 
prueba=texto.split()
print(prueba[5])

# join()  unir
palabra= "iniciamos"
palabra2= "para"
palabra3= "unir"
frase=" ".join([palabra,palabra2,palabra3])
print(frase)

frase=" ".join(prueba)
print(frase)

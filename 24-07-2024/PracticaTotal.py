# Se ingresa el texto y se pasa todo a minuscula en la variable texto
texto=input("ingrese el texto: ").lower()
# Se crea una lista para agregar una a una las letras a buscar
lista=[]
# Se ingresan las letras a la lista ubicaciones por defecto 0,1,2
lista.append(input("ingrese primera letra: "))
lista.append(input("ingrese segunda letra: "))
lista.append(input("ingrese tercera letra: "))

# imprimo la lista para confirmar los datos a buscar
print(lista)
# Se consulta cuantas veces esta repetida cada una de las letras ingresadas
# se ingresa el valor en repeticion_a,b y c
repeticion_a=texto.count(lista[0])
repeticion_b=texto.count(lista[1])
repeticion_c=texto.count(lista[2])
# Para mostrar en texto Ingreso los valores de la lista en variables
var_a=lista[0]
var_b=lista[1]
var_c=lista[2]
# Se presenta al usuario en pantalla el mensaje
print(f"""
      Repeticion de letras ingresadas
      1. letra "{var_a}" se repite {repeticion_a} veces
      2. letra "{var_b}" se repite {repeticion_b} veces
      3. letra "{var_c}" se repite {repeticion_c} veces""")
# Se agrega en lista el texto ingresado, separados por espacio
cadena_total_texto=texto.split()
# Se consulta el total de elementos y se guarda en una variable
total_cadena=len(cadena_total_texto)

# Se presenta al usuario cantidad de palabras
print(f"""
      Se encontraron un total de {total_cadena} palabras""")

# Se guarda la primera letra ubicada en [0]
# Para la ultima de toma el tamaño del texto y luego se agrega la cantidad de caracteres -1
# Se asigna a una variable la ultima letra
primera_letra=texto[0]
cantidad_texto=len(texto)-1
ultima_letra=texto[cantidad_texto]
# ultima_letra=texto[-1]
# Se muestra en pantalla la primera y ultima letra del texto
print(f"""
      La primera letra de su texto es "{primera_letra}" 
      La Ultima letra del Texto es "{ultima_letra}" """)
# Se asigna a una variable el texto pero inverso
texto_inverso=texto[::-1]
# Se muestra en pantalla el texto inverso
print(f"""
      El Texto Original invertido es 
      "{texto_inverso}" """)

# Se consulta si la palabra Python se encuentra en el texto
# el resultado se guarda como strin rta (true, false)
consultar="python" in texto
# Se consulta en un dicionario la clave true o false
ConsultaTex={True:"La Palabra Python si ",False:'La Palabra Python, no '}
# Se asigna a la variable rta y se muestra en pantalla
rta=ConsultaTex[consultar]

print(f"""
      Luego de Consultar su texto se pudo definir que {rta} se encuentra en el texto
      """)
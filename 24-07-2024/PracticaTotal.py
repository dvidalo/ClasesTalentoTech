texto=input("ingrese el texto: ").lower()
lista=[]
lista.append(input("ingrese primera letra: "))
lista.append(input("ingrese segunda letra: "))
lista.append(input("ingrese tercera letra: "))
print(lista)
repeticion_a=texto.count(lista[0])
repeticion_b=texto.count(lista[1])
repeticion_c=texto.count(lista[2])
var_a=lista[0]
var_b=lista[1]
var_c=lista[2]
print(f"""
      Repeticion de letras ingresadas
      1. letra "{var_a}" se repite {repeticion_a} veces
      2. letra "{var_b}" se repite {repeticion_b} veces
      3. letra "{var_c}" se repite {repeticion_c} veces""")
cadena_total_texto=texto.split()
total_cadena=len(cadena_total_texto)
print(f"""
      Se encontraron un total de {total_cadena} palabras""")

primera_letra=texto[0]
cantidad_texto=len(texto)-1
ultima_letra=texto[cantidad_texto]

print(f"""
      La primera letra de su texto es "{primera_letra}" 
      La Ultima letra del Texto es "{ultima_letra}" """)

texto_inverso=texto[::-1]
print(f"""
      El Texto Original invertido es 
      "{texto_inverso}" """)


consultar=str("python" in texto)
ConsultaTex={'True':"La Palabra Python si ",'False':'La Palabra Python, no '}
rta=ConsultaTex[consultar]

print(f"""
      Luego de Consultar su texto se pudo definir que {rta} se encuentra en el texto
      """)
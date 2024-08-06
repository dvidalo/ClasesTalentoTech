
# Practica 1
listanumero=[445422472/2, 21310/5,2134747*33,44556475,121676,6654067,353254,133134,55**12,611**5]
valor_maximo=float(max(listanumero))
print(f"el valor maximo es{valor_maximo}")

# Practica2
valor_minimo=float(min(listanumero))
rango=valor_maximo-valor_minimo
print(f"La diferencia entre {valor_maximo} menos {valor_minimo} es {rango}")

# Practica 3
diccionario_edades={"Carlos":55,"Maria":42,"Mabel":78,"Jose":44,"Lucas":24,"Rocio":35,"Sebastian":19,"Catalina":2,"Dario":49}

edad_minima=min(diccionario_edades.values())
ultimo_nombre=max(diccionario_edades.keys())
print(f"la edad minima es {edad_minima}")
print(f"el nombre mas largo es {ultimo_nombre}")

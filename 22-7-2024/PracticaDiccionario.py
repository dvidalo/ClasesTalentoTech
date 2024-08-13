# Practica Diccionario 1
mi_dic={'nombre':'Karen','apellido':'Jurgens','edad':35,'ocupacion':'Periodista'}

# Se asignan a Variables
nombre= mi_dic['nombre']
apellido =mi_dic['apellido']
edad= mi_dic['edad']
ocupacion = mi_dic['ocupacion']

# Se imprimen en pantalla
print(f"""
      practica Nro1
      nombre: {nombre}
      apellido: {apellido}
      edad: {edad}
      Ocupacion: {ocupacion}""")

# Practica Diccionario 2
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
resultado = mi_dict['puntos']['points2'][1]
print(f"""
      Practica Nro.2
      Segundo elemento es: {resultado}""")

# Practica Diccionario 3
# Se actualiza los datos en el Diccionario
mi_dic['edad']=36
mi_dic['ocupacion']='Editora'
mi_dic['pais']='Colombia'

# Se asignan en variables 
nombre= mi_dic['nombre']
apellido =mi_dic['apellido']
edad= mi_dic['edad']
ocupacion = mi_dic['ocupacion']
pais=mi_dic['pais']

# Se imprime en pantalla 

print(f"""
      practica Nro3
      nombre: {nombre}
      apellido: {apellido}
      edad: {edad}
      Ocupacion: {ocupacion}
      Pais: {pais}
      """)
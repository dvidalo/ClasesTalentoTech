# Practica Tupla 1
mi_tupla=(1,2,3,2,3,1,3,2,3,3,3,1,3,2,2,1,3,2)
repeticion=mi_tupla.count(2)
print(f"""
      Practica 1
      
      se repite el numero 2: {repeticion} veces""")

# Practica 2
mi_tupla= (1,2,3,2,3,1,3,2)
mi_lista= list(mi_tupla)
print(f"""
      practica 2
       se pasa la tupla= {mi_tupla}
       a mi lista = {mi_lista}""")
print(type(mi_lista))

# Practica 3
mi_tupla=(1,2,3,4)
a,b,c,d=mi_tupla
print(f"""
      Practica 3
      se pasan los valores a las variables
      a= {a}, b= {b}, c= {c}""")
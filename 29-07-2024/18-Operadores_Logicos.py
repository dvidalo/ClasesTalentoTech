# 4<5
# 5<6
mi_bool = 4<5<6
print(mi_bool)

mi_bool = 4<5 and 5<6 
print(mi_bool)

mi_bool = 4<5 and 5>6 
print(mi_bool)

mi_bool = 55==55 and 'juan'=='juan'
print(mi_bool)

mi_bool = 55!=55 and 'juan'=='juan'
print(mi_bool)

mi_bool = 4>5 or 4<5
print(mi_bool)

mi_bool = 4>5 or 5<6
print(mi_bool)

texto ="esta es una frase breve"
mi_bool=("esta" in texto) and ("python" in texto)
print(mi_bool)

mi_bool=("esta" in texto) or ("python" in texto)
print(mi_bool)

a= 5

if(a==4):
    print("es tres")
elif a<4:
    print ("segunda verificacion")
else:
    print("negacion")

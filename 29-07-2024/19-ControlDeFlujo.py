# if, elif, else
if 10>9:
    print("correcto")

if True:
    print("Correcto")

x=True

if x:
    print("correcto")
    
 
a= 5

if a==4:
    print("es tres")
elif a<4:
    print ("segunda verificacion")
else:
    print("negacion")
    
# for
letras=('a','b','c','d','e')    
for item in letras:
    print(item)

#  while
numeros=(2,4,6,8,10)
contador=0
while contador<4:
    print(f"numero {numeros[contador]}")
    contador += 1

# range
for i in range(1,11):
    print(i)
    
nombre_asociado = input("Ingresa el nombre del asociado: ")
numero_asociado = int(input("ingresa el numero del asociado: "))

print(f" Estimado/a {nombre_asociado}, su numero de asociado es {numero_asociado}")

puntos_actuales = int(input("ingresa los puntos actuales: "))
print(f"tu tienes {puntos_actuales} puntos en Total, acumulas ({puntos_actuales}) puntos")
puntos_nuevos = int(input("ingresa los puntos nuevos: "))
puntos_actuales=puntos_nuevos+puntos_actuales
print(f"has ganado {puntos_nuevos} puntos en Total, acumulas ({puntos_actuales})")


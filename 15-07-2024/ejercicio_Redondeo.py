nombre=input("Ingrese su nombre Completo: ")
VentaTotal=float(input(f"{nombre} Por Favor Ingresa el valor de la venta Total: "))
comision=round(VentaTotal*.13,2)
print(f"Nombre Completo: {nombre}\nVenta Total: ${VentaTotal}\nComision: ${comision}")
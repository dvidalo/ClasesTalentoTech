nombre=input("Ingrese su nombre Completo: ")
VentaTotal=float(input(f"\n{nombre} \nPor Favor Ingresa el valor de la venta Total: "))
comision=round(VentaTotal*.13,2)
print(f"\nNombre Completo: {nombre}\nVenta Total: ${VentaTotal}\nComision: ${comision}")
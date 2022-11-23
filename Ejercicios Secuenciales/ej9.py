""" 9. Una tienda ofrece un descuento del 15% sobre el total de la compra y 
un cliente desea saber cuanto deberá pagar finalmente por su compra."""

# Tienda ofrece un descuento del 15% sobre el total y se desea saber cuando pagará el cliente

compra = float(input("Introduce precio de compra "))
descuento = compra*0.15

print(f"El precio de compra con el descuento es {compra-descuento:.2f}")

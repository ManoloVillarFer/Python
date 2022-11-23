"""8. Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas,
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que 
realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones."""
commission = 0.1

# Sueldo base más 10% extra por comisión de ventas

# Se desea saber cuando dinero obtendrá por concepto de comisiones por la tres ventas que realiza al mes

# Y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones

base = float(input("Introduce el sueldo base "))
v1 = float(input("Introduce precio de venta "))
v2 = float(input("Introduce precio de venta "))
v3 = float(input("Introduce precio de venta "))

v1 = v1 * commission
v2 = v2 * commission
v3 = v3 * commission

print("Se llevará en comisiones", v1+v2+v3)
print("Su sueldo sera total sera de", base+v1+v2+v3)

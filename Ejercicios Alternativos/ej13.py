"""
13. Escribir un programa que calcule el desglose mínimo en billetes y monedas
de una cantidad exacta de euros. Hay billetes de 500, 200, 100, 50, 20, 10 y 5 euros
y monedas de 2 y 1 euro. Por ejemplo, si deseamos conocer el desglose de 534 euros,
el programa mostrará por pantalla el mensaje:

Para 534 euros, el desglose mínimo es:
5 billetes de 100 euros
1 billete de 20 euros
1 billete de 10 euros
1 billete de 2 euros
2 monedas de 1 euro
"""

# Pedimos los datos:
cantidad = int(input("Introduce la cantidad: "))

# Calculos y mostramos:
# Billetes de 500
if cantidad >= 500:
    print("Billetes de 500:", cantidad // 500)
    cantidad = cantidad % 500
# Billetes de 200
if cantidad >= 200:
    print("Billetes de 200:", cantidad // 200)
    cantidad = cantidad % 200
# Billetes de 100
if cantidad >= 100:
    print("Billetes de 100:", cantidad // 100)
    cantidad = cantidad % 100
# Billetes de 50
if cantidad >= 50:
    print("Billetes de 50:", cantidad // 50)
    cantidad = cantidad % 50
# Billetes de 20
if cantidad >= 20:
    print("Billetes de 20:", cantidad // 20)
    cantidad = cantidad % 20
# Billetes de 10
if cantidad >= 10:
    print("Billetes de 10:", cantidad // 10)
    cantidad = cantidad % 10
# Billetes de 5
if cantidad >= 5:
    print("Billetes de 5:", cantidad // 5)
    cantidad = cantidad % 5
# Monedas de 2
if cantidad >= 2:
    print("Monedas de 2:", cantidad // 2)
    cantidad = cantidad % 2
# Monedas de 1
if cantidad >= 1:
    print("Monedas de 1:", cantidad // 1)
    cantidad = cantidad % 1

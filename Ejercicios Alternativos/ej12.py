""" 12. Escribir un programa que lea un año indicar si es bisiesto.

Nota: un año es bisiesto si es un número divisible por 4,
pero no si es divisible por 100, excepto que también sea divisible por 400.
"""

print("Programa para indicar si un año es bisiesto.")

# Pedimos los datos:
anio = int(input("Introduzca el año: "))

# Calculos y mostramos:
if (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0):
    print("El año", anio, "es bisiesto")
else:
    print("El año", anio, "NO es bisiesto")

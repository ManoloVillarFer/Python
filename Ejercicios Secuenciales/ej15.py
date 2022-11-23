"""15. Dadas dos variables numéricas A y B, que el usuario debe teclear,
se pide realizar un algoritmo que intercambie
los valores de ambas variables y muestre cuanto valen al final las dos variables."""

a = int(input("Introduce un valor "))
b = int(input("Introduce un valor "))

""" Forma no python
aux = a 
a = b
b = aux
"""

a, b = b, a

print("El valor de a ahora es ", a)
print("El valor de b ahora es ", b)

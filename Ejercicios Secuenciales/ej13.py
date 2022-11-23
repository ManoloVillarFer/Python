""" # 13. Realiza un programa que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?"""

import math

n1 = int(input("Dame un número "))

raizcua = math.pow(n1,2)
raizcub = math.pow(n1,2)

print("La raíz cuadrada es", raizcua, "La raíz cúbica es", raizcub)

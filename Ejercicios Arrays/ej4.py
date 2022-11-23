import numpy as np

"""
Date: 14/11/2022
Author: Francisco Manuel Villar Fernández
Escribe un programa que pida 10 números por teclado y que luego muestre los números introducidos junto con las palabras 
“máximo” y “mínimo” al lado del máximo y del mínimo respectivamente.
"""

"""
Descomposición del problema:
Pedimos 10 números vacíos por teclado
Mostramos el máximo y el mínimo
"""

# Creamos un array de 10 elementos con valores vacíos
numbers = np.zeros(10)

# Recorremos el array y nos ponemos a pedir números
for n in range(10):
    numbers[n] = int(input("Introduce un número: "))

# Versión Corregida
min_number = np.min(numbers)
max_number = np.max(numbers)

for i in numbers:
    print(i, end="")
    if i == min_number:
        print(" es el mínimo")
    elif i == max_number:
        print(" es el máximo")
    else:
        print()
# Mostramos la salida por pantalla
# print(f"Máximo: {numbers.max()}")
# print(f"Mínimo: {numbers.min()}")

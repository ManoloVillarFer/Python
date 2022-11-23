import numpy as np

"""
Date: 14/11/2022
Author: Francisco Manuel Villar Fernández
Escribe un programa que pida 20 números enteros. Estos números se deben introducir en un array de 4 filas por 5 columnas. 
El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara. 
La suma total debe aparecer en la esquina inferior derecha.
"""

"""
Descomposición del problema: 
Pedir 20 números enteros
Introducirlos en un array de 4 filas por 5 columnas
Mostrar las sumas parciales de filas y columnas
Mostrar la suma total en la esquina inferior derecha
"""

# Pedimos los 20 números enteros
numbers = np.zeros((4, 5), dtype=int)
for row in range(4):
    for column in range(5):
        numbers[row, column] = int(input("Introduce un número entero: "))

# Sumas parciales de filas y columnas
for row in range(4):
    for column in range(5):
        print(f"{numbers[row, column]:>5}", end="")
    print(f"{np.sum(numbers[row, :]):>5}")

# Suma total en la esquina inferior derecha
for column in range(5):
    print(f"{np.sum(numbers[:, column]):>5}", end="")
print(f"{np.sum(numbers):>5}")

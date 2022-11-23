import numpy as np

"""
Date: 14/11/2022
Author: Francisco Manuel Villar Fernández
Modifica el programa anterior de tal forma 
que los números que se introducen en el array se generen de forma aleatoria (valores entre 100 y 999).
"""

"""
Descomposición del problema: 
Números aleatorios entre 100 y 999
Introducirlos en un array de 4 filas por 5 columnas
Mostrar las sumas parciales de filas y columnas
Mostrar la suma total en la esquina inferior derecha
"""

# Generamos los números aleatorios entre 100 y 999
numbers = np.random.randint(100, 1000, size=(4, 5), dtype=int)

# Sumas parciales de filas y columnas
for row in range(4):
    for column in range(5):
        print(f"{numbers[row, column]:>5}", end="")
    print(f"{np.sum(numbers[row, :]):>5}")

# Suma total en la esquina inferior derecha
for column in range(5):
    print(f"{np.sum(numbers[:, column]):>5}", end="")
print(f"{np.sum(numbers):>5}")


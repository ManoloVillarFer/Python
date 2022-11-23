import numpy as np

"""
Date: 14/11/2022
Author: Francisco Manuel Villar Fernández
Realiza un programa que rellene un array de 6 filas por 10 columnas 
con números enteros positivos comprendidos entre 0 y 1000 (ambos incluidos). 
A continuación, el programa deberá dar la posición tanto del máximo como del mínimo.
"""

"""
Descomposición del problema:
Creamos un array de 6 filas por 10 columnas con números aleatorios entre 0 y 1000
Mostramos la posición del máximo y del mínimo
"""

# Creamos el array
numbers = np.random.randint(0, 1001, (6, 10))

# Mostramos la posición del máximo y del mínimo
print(f"El máximo está en: ", np.argmax(numbers))
print(f"La posición del mínimo es: ", np.argmin(numbers))

# Mostramos el array
print(numbers)


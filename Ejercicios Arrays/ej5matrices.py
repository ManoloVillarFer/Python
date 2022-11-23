import numpy as np

"""
Date: 14/11/2022
Author: Francisco Manuel Villar Fernández
Modifica el programa anterior de tal forma que no se repita ningún número en el array.
"""

"""
Descomposición del problema:
No se debe repetir ningún número en el array
Creamos un array de 6 filas por 10 columnas con números aleatorios entre 0 y 1000
Mostramos la posición del máximo y del mínimo
"""

# Creamos el array
numbers = np.random.choice(range(0, 1001), (6, 10), replace=False)

# Mostramos la posición del máximo y del mínimo
print(f"El máximo está en: ", np.argmax(numbers))
print(f"La posición del mínimo es: ", np.argmin(numbers))

# Mostramos el array
print(numbers)

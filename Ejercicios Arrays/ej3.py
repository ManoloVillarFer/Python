import numpy as np
import pandas as pd

"""
Date: 14/11/2022
Author: Francisco Manuel Villar Fernández
Define tres arrays de 20 números enteros cada uno, con nombres numero, cuadrado y cubo. 
Carga el array numero con valores aleatorios entre 0 y 100. 
En el array cuadrado se deben almacenar los cuadrados de los valores que hay en el array numero. 
En el array cubo se deben almacenar los cubos de los valores que hay en numero. 
A continuación, muestra el contenido de los tres arrays dispuesto en tres columnas.
"""

"""
Descomposición del problema: 
Creamos tres arrays
En el array cuadrado se deben almacenar los cuadrados de los valores que hay en el array número.
En el array cubo se deben almacenar los cubos de los valores que hay en número.
Mostrar los tres arrays en tres columnas
"""

# Creamos los tres arrays
number = np.random.randint(0, 100, 20)
square = np.square(number)
cube = np.power(number, 3)

# Hacemos un bucle for de números para recorrer la longitud del array
# print("number square cube")
# for n in range(len(number)):
    # print(f"{number[n]:3}\t{square[n]:5}\t{cube[n]:7}")

# Representamos con Pandas
tabla = pd.DataFrame({"Numero": number, "Cuadrado": square, "Cubo": cube})
print(tabla)

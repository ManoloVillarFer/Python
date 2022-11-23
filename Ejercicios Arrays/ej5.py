import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
"""
Date: 14/11/2022
Author: Francisco Manuel Villar Fernández
Realiza un programa que pida la temperatura media que ha hecho en cada mes de un determinado año y 
que muestre a continuación un diagrama de barras horizontales con esos datos. 
Las barras del diagrama se pueden dibujar a base de asteriscos o cualquier otro carácter.
"""

"""
Descomposición del problema:
Creamos un array con los meses del año
Pedimos la temperatura media de cada mes
Mostramos el máximo y el mínimo
Dibujamos con cualquier carácter el diagrama de barras
"""

# Creamos un array con los meses del año
months = np.array(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
                   "Octubre", "Noviembre", "Diciembre"])

# Creamos un array vacío de 12 números
temperatures = np.zeros(12)

# Recorremos el array y pedimos números
for n in range(12):
    temperatures[n] = int(input(f"Temperatura media del mes {months[n]}: "))

# Modificar con pandas y mathplotlib

# Recorremos el array de temperaturas
for n in range(12):
    print(months[n])
    for i in range(int(temperatures[n])):
        print(".")
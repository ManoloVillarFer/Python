"""
Nombre del Programa: ej8
Author: Francisco Manuel Villar Fernández
Hacer un programa que muestre un cronómetro, indicando las horas, minutos y segundos.

Para hacer una espera en Python podemos usar el método sleep del módulo time.
"""

# Importamos el módulo time
import time

# Inicializamos las variables
horas = 0
minutos = 0
segundos = 0

# Bucle infinito
while True:
    print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
    time.sleep(1)
    segundos += 1
    if segundos == 60:
        segundos = 0
        minutos += 1
        if minutos == 60:
            minutos = 0
            horas += 1
            if horas == 24:
                horas = 0


""" 12. Pide al usuario dos pares de números x1,y1 y x2,y2,
que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos."""

# Dos pares de números x1,y1 y x2,y2 y mostramos la distancia entre ellos

# Importamos math para hacer la fórmula
import math

x1 = int(input("Dame el valor de x1 "))
y1 = int(input("Dame el valor de y1 "))
x2 = int(input("Dame el valor de x2 "))
y2 = int(input("Dame el valor de y2 "))

formula = math.sqrt(math.pow((x2-x1), 2)+math.pow((y2-y1), 2))

print("La distancia es", formula)

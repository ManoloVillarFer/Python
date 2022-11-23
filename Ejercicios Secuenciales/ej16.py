"""
Autor: Francisco Manuel Villar Fernández
16. Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d.
El que está detrás viaja a una velocidad mayor.
Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km)
y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo
(minutos) alcanzará el vehículo más rápido al otro.
"""
"""
La forma de poner una detección de errores es usando sys.exit y le damos un valor a sys.exit y
y por último sería interesante mandarlo a un archivo de error
"""
import sys

v1 = float(input("Introduce la velocidad del primer vehículo "))
v2 = float(input("Introduce la velocidad del segundo vehículo "))
if v1 <= v2:
    print("El primer vehículo no podrá alcanzar al segundo", file=sys.stderr)
    sys.exit(1)

distancia = float(input("Introduce la distancia entre ellos "))

# Hacemos los calculos
tiempo = 60 * distancia / (v1 - v2)

print("Lo alcanzará en", tiempo, "minutos")

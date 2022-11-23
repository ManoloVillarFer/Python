""" 10. Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos
circunferencias y las clasifique en uno de estos estados:

exteriores
tangentes exteriores
secantes
tangentes interiores
concéntricas
"""

# Importamos Math
import math

# Pedimos los datos
x1 = float(input("Dime coordenada x primera circunferencia: "))
y1 = float(input("Dime coordenada y primera circunferencia: "))
r1 = float(input("Dime radio primera circunferencia: "))
x2 = float(input("Dime coordenada x segunda circunferencia: "))
y2 = float(input("Dime coordenada y segunda circunferencia: "))
r2 = float(input("Dime radio segunda circunferencia: "))

# Calculos
distancia = math.sqrt(math.pow((x2-x1), 2)+math.pow((y2-y1), 2))

# Circunferencias exteriores
#  Si no tienen ningún punto en común y la distancia entre sus centros es mayor que la suma de sus radios.
if distancia > (r1+r2):
    print("Circunferencias exteriores")
# Circunferencias secantes
# La distancia es menor que la suma de los radios y mayor que su diferencia.
elif (r1 + r2) > distancia > abs(r1 - r2):
    print("Circunferencias secantes")
# Circunferencias interiores
# Tienen dos puntos en común.
# La distancia entre sus centros es menor que la suma de sus radios y mayor que su diferencia.
elif 0 < distancia < abs(r1 - r2):
    print("Circunferencias interiores")
# Circunferencias tangentes exteriores
# La distancia entre los centros es igual a la suma de los radios.
elif distancia == (r1+r2):
    print("Circunferencias tangentes exteriores")
# Circunferencias tangentes interiores
# La distancia entre los centros es igual a la diferencia entre los radios.
elif distancia == abs(r1-r2):
    print("Circunferencias tangentes interiores")
# Circunferencias concéntricas
# No tienen puntos en común y la distancia entre sus centros es cero (coinciden). La distancia = 0.
elif distancia == 0:
    print("Circunferencias concéntricas")
else:
    print("Esta situación no se puede dar")

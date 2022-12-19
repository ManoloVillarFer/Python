"""
Nombre del Programa: ej5
Author: Francisco Manuel Villar Fernández
Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior es mayor que el
superior lo tiene que volver a pedir.

A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las
siguientes informaciones:

    La suma de los números que están dentro del intervalo (intervalo abierto).
    Cuantos números están fuera del intervalo.
    Informa si hemos introducido algún número igual a los límites del intervalo.
"""

# Variables
fuera_de_intervalo = 0
igual_a_limites = False
suma = 0

# Pido intervalo
limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
limite_superior = int(input("Introduce el límite superior del intervalo: "))

# Si el límite inferior es mayor que el superior lo vuelvo a pedir
while limite_inferior > limite_superior:
    print("El límite inferior es mayor que el límite superior.")
    limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
    limite_superior = int(input("Introduce el límite superior del intervalo: "))

# Calculo
n = int(input("Introduce un número (0 para salir): "))
while n != 0:
    if limite_inferior < n < limite_superior:
        suma += n
    else:
        fuera_de_intervalo += 1
        if n == limite_inferior or n == limite_superior:
            igual_a_limites = True
    n = int(input("Introduce un número (0 para salir): "))

# Resultado
print(f"La suma de los números que están dentro del intervalo es {suma}.")
print(f"Han salido {fuera_de_intervalo} números fuera del intervalo.")
if igual_a_limites:
    print(f"Han salido números iguales a los límites del intervalo.")
else:
    print(f"No han salido números iguales a los límites del intervalo.")


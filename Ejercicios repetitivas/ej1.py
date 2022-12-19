"""
Nombre del Programa: ej1
Author: Francisco Manuel Villar Fernández
Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta
el número (además te dice en cuantos intentos lo has acertado), si se llega al límite de intentos te muestra el
número que había generado.
"""

# Importamos la librería random
import random

NUMERO_INICIAL = 1
NUMERO_FINAL = 100
INTENTOS = 10

# Número aleatorio del 1 al 100
aleatorio = random.randint(NUMERO_INICIAL, NUMERO_FINAL)
print("Adivina el número que estoy pensando entre el 1 y el 100, tienes 10 intentos")

# Bucle para pedir el número
while True:
    numero = int(input(f"Intento {INTENTOS}. Introduce un número del 1 al 100: "))

    if aleatorio > numero:
        print(f"El número {numero} es mayor que el número a adivinar.")
    elif aleatorio < numero:
        print(f"El número {numero} es menor que el número a adivinar.")

    INTENTOS -= 1

    if numero == aleatorio or INTENTOS == 0:
        break

# Intentos necesarios y resultado
if numero == aleatorio:
    print(f"Has adivinado el número en {10 - INTENTOS} intentos.")
else:
    print(f"No has adivinado el número. El número era el {aleatorio}.")


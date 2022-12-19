"""
Nombre del Programa: ej2
Author: Francisco Manuel Villar Fernández
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe
informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
"""

# Ajustamos las variables
positivos = 0
negativos = 0
ceros = 0

# Pedir los números
cantidad = int(input("¿Cuantos números vas a introducir?: "))

# Bucle para pedir los números
for i in range(cantidad):
    numero = int(input(f"Introduce el número {i + 1}: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

# Resultado
print(f"Has introducido {positivos} números positivos, {negativos} números negativos y {ceros} ceros.")

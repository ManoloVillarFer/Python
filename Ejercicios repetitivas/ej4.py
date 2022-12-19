"""
Nombre del Programa: ej4
Author: Francisco Manuel Villar Fernández
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
"""

# Pedimos los números
numero_inicial = int(input("Introduce el número de inicio: "))
numero_final = int(input("Introduce el número de final: "))

# Bucle para imprimir los números pares
print(f"Los números pares entre {numero_inicial} y {numero_final} son: ")

for i in range(numero_inicial, numero_final):
    if i % 2 == 0:
        print(i, end=" ")

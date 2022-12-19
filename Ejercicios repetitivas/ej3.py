"""
Nombre del Programa: ej3
Author: Francisco Manuel Villar Fernández
Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina
cuando se introduce un espacio.
"""

# Bucle para pedir los caracteres
while True:
    caracter = input("Introduce un caracter: ")
    if caracter in "aeiou" or caracter in "AEIOU":
        print("VOCAL")
    elif caracter == " ":
        break
    else:
        print("NO VOCAL")



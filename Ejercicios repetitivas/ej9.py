"""
Nombre del Programa: ej9
Author: Francisco Manuel Villar Fernández
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.
"""

# Pedimos la cantidad de números primos
cantidad = int(input("¿Cuantos números primos quieres mostrar? : "))

# Inicializamos las variables
contador_primos = 0
primo = 3

# Bucle
while contador_primos < cantidad:
    es_primo = True
    # Comprobamos si es primo
    for i in range(2, primo):
        if primo % i == 0:
            es_primo = False
            break
    if es_primo:
        contador_primos += 1
        print(f"El {contador_primos} número primo es el {primo}")
    primo += 1

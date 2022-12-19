"""
Nombre del Programa: ej10
Author: Francisco Manuel Villar Fernández
Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.
"""

# Pedimos la cadena y el carácter
cadena = input("Introduce una cadena: ")
caracter = input("Introduce un caracter: ")

# Inicializamos la variable
contador = 0

# Bucle
for i in cadena:
    if i == caracter:
        contador += 1

# Resultado
print(f"El caracter {caracter} aparece {contador} veces en la cadena {cadena}.")

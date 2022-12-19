"""
Nombre del Programa: ej12
Author: Francisco Manuel Villar Fernández
Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter
en la cadena por el segundo carácter.
"""

# Pedimos la cadena y los caracteres
cadena = input("Introduce una cadena: ")
caracter = input("Introduce un caracter: ")

# Validamos que sea un caracter
while len(caracter) != 1:
    print("Error, introduce más de un caracter.")
    caracter = input("Introduce un caracter: ")

caracter2 = input("Introduce un caracter: ")

# Validamos que sea un caracter de nuevo
while len(caracter2) != 1:
    print("Error, introduce más de un caracter.")
    caracter2 = input("Introduce un caracter: ")

nuevo_caracter = ""

# Bucle
for i in cadena:
    if i == caracter:
        nuevo_caracter += caracter2
    else:
        nuevo_caracter += i

# Resultado
print(f"La cadena {cadena} con el caracter {caracter} cambiado por {caracter2} es: {nuevo_caracter}")


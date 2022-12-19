"""
Nombre del Programa: ej14
Author: Francisco Manuel Villar Fernández
Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.
"""

# Pedimos las cadenas
cadena = input("Introduce una cadena: ")
subcadena = input("Introduce una subcadena: ")

# Inicializamos la variable
contador = 0

# Bucle
for i in cadena:
    if i == subcadena[contador]:
        contador += 1
    else:
        contador = 0

    if contador == len(subcadena):
        break

# Resultado
if contador == len(subcadena):
    print(f"La cadena {cadena} contiene la subcadena {subcadena}.")

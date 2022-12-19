"""
Date: 16/11/22
Nombre del Programa: ej5
Author: Francisco Manuel Villar Fernández
Crea una función que reciba un número, lo convierta al sistema de palotes y lo devuelva en una cadena de caracteres.

Por ejemplo, el 470213 en decimal es el | | | | - | | | | | | | - - | | - | - | | | en el sistema de palotes.

Utiliza esta función en un programa para comprobar que funciona bien. Desde la función no se debe mostrar nada por
pantalla, solo se debe usar print desde el programa principal.
"""

from ej5 import number_to_sticks


number = int(input("Dame un número para convertirlo al sistema de palotes: "))
print(f"{number} convertido al sistema de palotes es: {number_to_sticks(number)}")

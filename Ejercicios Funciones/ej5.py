"""
Date: 16/11/22
Nombre del Programa: ej5
Author: Francisco Manuel Villar Fernández
Crea una función que reciba un número, lo convierta al sistema de palotes y lo devuelva en una cadena de caracteres.

Por ejemplo, el 470213 en decimal es el | | | | - | | | | | | | - - | | - | - | | | en el sistema de palotes.

Utiliza esta función en un programa para comprobar que funciona bien. Desde la función no se debe mostrar nada por
pantalla, solo se debe usar print desde el programa principal.
"""


def number_to_sticks(number):

    number = str(number)

    # Creamos una lista para la cadena
    sticks_list = []

    # Recorremos toda la cadena
    for n in number:
        n = int(n)
        # Añadimos al final de la lista la cantidad de palotes
        sticks_list.append("|" * n)

    # Le añadimos un - entre cada palote
    palotes_list = " - ".join(sticks_list)

    return palotes_list

"""
Date: 23/11/22
Nombre del Programa: ej7
Author: Francisco Manuel Villar Fernández
Define la función mezcla de forma que tome dos listas como parámetros y devuelve otra que es el resultado de mezclar 
los números de ambos de forma alterna, se coge un número de a, luego de b, luego de a, etc. Los arrays a y b pueden 
tener longitudes diferentes; por tanto, si se terminan los números de un array se terminan de coger 
todos los que quedan del otro.

Ejemplos:

Si a = [8, 9, 0] y b = [1, 2, 3], mezcla(a, b) devuelve [8, 1, 9, 2, 0, 3 ]

Si a = [4, 3] y b = [7, 8, 9, 10], mezcla(a, b) devuelve [4, 7, 3, 8, 9, 10]

Si a = [8, 9, 0, 3] y b = [1], mezcla(a, b) devuelve [8, 1, 9, 0, 3]

Si a = [ ] y b = [1, 2, 3], mezcla(a, b) devuelve [1, 2, 3]
"""


def mixture(lista1, lista2):
    # Creamos una lista vacía
    empty_list = []
    i = 0

    # Comparamos las dos listas
    while i < len(lista1) and i < len(lista2):
        empty_list.append(lista1[i])
        empty_list.append(lista2[i])

        i += 1
    if len(lista1) > len(lista2):
        # Añadimos los valores de la lista1
        empty_list += lista1[i:]
    elif len(lista2) > len(lista1):
        # Añadimos los valores de la lista2
        empty_list += lista2[i:]
    return empty_list


# Creamos las listas
lista1 = [8, 9, 0, 10]
lista2 = [1, 2, 3, 5, 3, 2, 1]

# Llamamos a la función
if __name__ == "__main__":
    assert mixture([8, 9, 0], [1, 2, 3]) == [8, 1, 9, 2, 0, 3]
    assert mixture([4, 3], [7, 8, 9, 10]) == [4, 7, 3, 8, 9, 10]
    assert mixture([8, 9, 0, 3], [1]) == [8, 1, 9, 0, 3]
    assert mixture([], [1, 2, 3]) == [1, 2, 3]

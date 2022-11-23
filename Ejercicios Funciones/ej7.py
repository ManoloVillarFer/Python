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

# Creamos las listas
lista1 = [8, 9, 0, 10]
lista2 = [1, 2, 3, 5, 3, 2, 1]


def mezcla(a, b):
    # Creamos una lista vacía
    empty_list = []
    # Ponemos un contador a 0 para recorrer las listas
    i = 0
    # Recorremos la lista mientras el contador sea menor que la longitud de la lista
    while i < len(a) and i < len(b):
        # Ponemos los valores al final de las listas en la lista vacía
        empty_list.append(a[i])
        empty_list.append(b[i])
        # Aumentamos el contador
        i += 1
    if len(a) > len(b):
        # Añadimos los valores de la lista1 creando una copia de la lista
        empty_list += a[i:]
    elif len(b) > len(a):
        # Añadimos los valores de la lista2 creada una copia de la lista
        empty_list += b[i:]
    return empty_list


# Llamamos a la función
print(mezcla(lista1, lista2))

"""
Date: 16/11/22
Nombre del Programa: ej1
Author: Francisco Manuel Villar Fernández
Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cuatro opciones:
sumar, restar, multiplicar, dividir y terminar.
Cada opción llama a una función a la que se le pasan las dos variables y muestra el resultado de la operación.
Si se introduce una opción incorrecta se muestra un mensaje de error.
Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera).
Las variables se inicializan a cero.
Modifica el programa anterior para que si no se introducen las dos variables desde la opción
correspondiente no se puedan ejecutar el resto de las opciones.
Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas,
pide una opción (por su número) y devuelve la opción escogida. Modifica el último programa para que use esta función.
"""
"""
Modifica el programa anterior para que si no se introducen las dos variables desde la opción
correspondiente no se puedan ejecutar el resto de las opciones.
"""


def main():
    n1, n2 = 0, 0
    dato_ha_sido_introducido = False
    while True:
        option = menu()
        if option == 1:
            n1, n2 = introduce_datos()
            dato_ha_sido_introducido = True
        elif option == 6:
            break
        elif not dato_ha_sido_introducido:
            print("ERROR: No se han introducido los datos")
        elif option == 2:
            sumar(n1, n2)
        elif option == 3:
            restar(n1, n2)
        elif option == 4:
            multiplicar(n1, n2)
        elif option == 5:
            dividir(n1, n2)
        else:
            print("Opción incorrecta.")


# Creamos la función menu
def menu():
    print("Menú")
    print("1. Introducir datos")
    print("2. Sumar")
    print("3. Restar")
    print("4. Multiplicar")
    print("5. Dividir")
    print("6. Terminar")
    option = int(input("Introduce una opción: "))
    return option


def introduce_datos():
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    return n1, n2


# Calculos
def sumar(number_1, number_2):
    print(f"La suma de {number_1} y {number_2} es {number_1 + number_2}")


def restar(number_1, number_2):
    print(f"La resta de {number_1} y {number_2} es {number_1 - number_2}")


def multiplicar(number_1, number_2):
    print(f"La multiplicación de {number_1} y {number_2} es {number_1 * number_2}")


def dividir(number_1, number_2):
    if number_2 != 0:
        print(f"La división de {number_1} y {number_2} es {number_1 / number_2}")
    else:
        print("No se puede dividir entre 0")


if __name__ == "__main__":
    main()

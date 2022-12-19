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
Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera).
Las variables se inicializan a cero.
"""


def main():
    number_1, number_2 = 0, 0
    while True:
        opcion = menu()
        if opcion == 1:
            sumar(number_1, number_2)
        elif opcion == 2:
            restar(number_1, number_2)
        elif opcion == 3:
            multiplicar(number_1, number_2)
        elif opcion == 4:
            dividir(number_1, number_2)
        elif opcion == 5:
            number_1, number_2 = introduce_datos()
        elif opcion == 6:
            break
        else:
            print("Opción incorrecta")


# Creamos la función menu
def menu():
    print("Menú")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Introducir datos")
    print("6. Terminar")
    option = int(input("Introduce una opción: "))
    return option


def introduce_datos():
    number_1 = int(input("Introduce el primer número: "))
    number_2 = int(input("Introduce el segundo número: "))
    return number_1, number_2


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

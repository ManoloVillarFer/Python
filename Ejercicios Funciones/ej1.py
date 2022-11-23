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


# Creamos la función menu
def menu():
    print("Menú")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Introducir variables")
    print("6. Terminar")
    return int(input("Elige una opción: "))


# Creamos la función principal
def main():
    while True:
        option = menu()
        if option == 1:
            print(f"La suma es {(a + b)}")
        elif option == 2:
            print(f"La resta es {(a - b)}")
        elif option == 3:
            print(f"La multiplicación es {(a * b)}")
        elif option == 4:
            print(f"La división es {(a / b)}")
        elif option == 5:
            a = int(input("Introduce el valor de a: "))
            b = int(input("Introduce el valor de b: "))
        elif option == 6:
            break
        else:
            print("Opción incorrecta")


# Llamamos a la función
main()

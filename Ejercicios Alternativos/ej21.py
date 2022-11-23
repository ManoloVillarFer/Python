# 21. Realiza un programa que pida tres números enteros y diga cuál es el mayor.

# Pedimos datos
n1 = int(input("Dime el número 1: "))
n2 = int(input("Dime el número 2: "))
n3 = int(input("Dime el número 3: "))

# Proceso
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print("El primer número es mayor")
    else:
        print("El primer número es menor")
if n2 > n1 and n2 > n3:
    if n1 > n3:
        print("El segundo número es mayor")
    else:
        print("El segundo número es menor")
if n3 >= n1 and n3 >= n2:
    if n1 > n2:
        print("El tercer número es mayor")
    else:
        print("El tercer número es menor")

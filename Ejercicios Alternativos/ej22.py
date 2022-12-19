"""
22. Realiza un programa que pida cinco números enteros y diga cuál es el mayor.
"""

# Pedimos datos
n1 = int(input("Dime el número 1: "))
n2 = int(input("Dime el número 2: "))
n3 = int(input("Dime el número 3: "))
n4 = int(input("Dime el número 4: "))
n5 = int(input("Dime el número 5: "))

# Calculos
if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print("El primer número es mayor")
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print("El segundo número es mayor")
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    print("El tercer número es mayor")
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    print("El cuarto número es mayor")
elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
    print("El quinto número es mayor")

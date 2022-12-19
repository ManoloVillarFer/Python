"""
23. Diseña un programa que, dados cinco números enteros,
determine cuál de los cuatro últimos números es más cercano al primero.
Por ejemplo, si el usuario introduce los números 2, 6, 4, 1 y 10,
el programa responderá que el número más cercano al 2 es el 1.
"""

# Pedimos datos
n1 = int(input("Dime el número 1: "))
n2 = int(input("Dime el número 2: "))
n3 = int(input("Dime el número 3: "))
n4 = int(input("Dime el número 4: "))
n5 = int(input("Dime el número 5: "))

# Distancia de n1 a n2, poniendo a n2 como referencia
candidato = n2
distancia = abs(n1 - n2)

# Tercer número
if abs(n1-n3) < distancia:
    candidato = n3
    distancia = abs(n1 - n3)

# Cuarto número
if abs(n1-n4) < distancia:
    candidato = n4
    distancia = abs(n1 - n4)

# Quinto número
if abs(n1-n5) < distancia:
    candidato = n5

print(candidato, "es el número con menor distancia a", n1)

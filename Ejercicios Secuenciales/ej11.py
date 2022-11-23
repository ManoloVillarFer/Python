""" 11. Pide al usuario dos números y muestra la "distancia" entre ellos
(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo)."""


# Pedimos dos números y tenemos que sacar el valor absoluto

n1 = int(input("Dame un número "))
n2 = int(input("Dame un número "))

total = n1-n2

print("La distancia entre los números es ", abs(total))

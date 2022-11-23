# 14. Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.

number = int(input("Dame un número de dos cifras: "))

tens = number // 10
units = number % 10

inverted = units * 10 + tens

print("El número invertido es", inverted)

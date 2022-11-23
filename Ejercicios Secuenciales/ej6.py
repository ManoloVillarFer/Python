# 6. Calcular la media de tres números pedidos por teclado.

from statistics import mean

n1 = float(input("Dame el primer número "))
n2 = float(input("Dame el segundo número "))
n3 = float(input("Dame el tercer número "))

print(f"La media es {mean([n1, n2, n3])}")

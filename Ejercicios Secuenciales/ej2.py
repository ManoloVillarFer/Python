# 2. Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = float(input("Dame la base del rectángulo: "))
altura = float(input("Dame la altura del rectángulo: "))

perimetro = altura*2 + base*2
area = base * altura

print(f"El perímetro del rectángulo es {perimetro:.2f} y el área es {area:.2f}")

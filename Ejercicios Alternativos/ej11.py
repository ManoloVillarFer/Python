"""
11. Programa que lea 3 datos de entrada A, B y C.
Estos corresponden a las dimensiones de los lados de un triángulo.
El programa debe determinar que tipo de triángulo es, teniendo en cuenta lo siguiente:

Si se cumple Pitágoras entonces es triángulo rectángulo
Si solo dos lados del triángulo son iguales entonces es isósceles.
Si los 3 lados son iguales entonces es equilátero.
Si no se cumple ninguna de las condiciones anteriores, es escaleno.
"""

# Pedimos los datos de los lados del triángulo
ladoA = float(input("Introduce longitud lado A: "))
ladoB = float(input("Introduce longitud lado B: "))
ladoC = float(input("Introduce longitud lado C: "))

# Cálculos
# Comprobamos si es equilátero, este caso es excluyente
if ladoA == ladoB and ladoB == ladoC:
    print("El triángulo es Equilátero")
else:
    # Comprobamos si es rectángulo (puede ser rectángulo e isósceles o escaleno)
    if ladoA**2 == (ladoB**2+ladoC**2) or ladoB**2 == (ladoA**2+ladoC**2) or ladoC**2 == (ladoB**2+ladoA**2):
        print("El triángulo es Rectángulo")
    # Comprobamos si es isósceles o escaleno (equilátero no es)
    if ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("El triángulo es Isósceles")
    else:
        print("El triángulo es Escaleno")

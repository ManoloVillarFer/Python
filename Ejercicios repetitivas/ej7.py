"""
Nombre del Programa: ej7
Author: Francisco Manuel Villar Fernández
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y
así sucesivamente. Realizar un programa para determinar cuánto debe pagar mensualmente y el total de lo que pagará
después de los 20 meses.
"""

# Constantes
PAGO_INICIAL = 10
MESES = 20

# Inicializamos las variables
pago = PAGO_INICIAL
total = 0

# Bucle
for i in range(MESES):
    print(f"El pago del mes {i + 1} es de {pago}€.")
    total += pago
    pago *= 2

# Resultado
print(f"El total a pagar es de {total}€.")

""" 4. Crea un programa que pida al usuario dos números
y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario."""

# Pedimos los números
dividendo = int(input("Dime el número 1: "))
divisor = int(input("Dime el número 2: "))

# Calculos y mostramos
if divisor == 0:
    print("No puedes dividir por 0")
else:
    print("La división es", dividendo/divisor)

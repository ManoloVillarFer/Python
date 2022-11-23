# 6. Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

# Pedimos los datos
cadena = input("Introduce una letra: ")

# Calculos y mostramos
if len(cadena) == 1 and "A" <= cadena <= "Z":
    print("Es una letra mayúscula")
else:
    print("No es una letra mayúscula")

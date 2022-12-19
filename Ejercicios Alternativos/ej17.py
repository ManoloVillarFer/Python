"""
17. Realiza un programa que pida por teclado el resultado (dato entero)
obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras
(dato cadena) de la cara opuesta al resultado obtenido.

Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje:
“ERROR: número incorrecto.”.
Ejemplo:

Introduzca número del dado: 5
En la cara opuesta está el "dos".
"""

# Pedimos los datos
resultado = int(input("Resultado del dado: "))

# Calculos
if resultado < 1 or resultado > 6:
    raise ValueError("ERROR: número incorrecto.")
elif resultado == 1:
    resultado = "Seis"
elif resultado == 2:
    resultado = "Cinco"
elif resultado == 3:
    resultado = "Cuatro"
elif resultado == 4:
    resultado = "Tres"
elif resultado == 5:
    resultado = "Dos"
elif resultado == 6:
    resultado = "Uno"

# Salida
print(f"La cara opuesta es {resultado}")

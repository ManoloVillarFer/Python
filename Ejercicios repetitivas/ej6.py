"""
Nombre del Programa: ej6
Author: Francisco Manuel Villar Fernández
Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el
resultado de la potencia. No se puede utilizar el operador de potencia ni la función.
"""

# Inicializamos las variables
potencia = 1

# Pedimos los números
base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

# Calculamos la potencia
for i in range(abs(exponente)):
    potencia *= base

# Si es negativo lo hacemos a la inversa
if exponente < 0:
    potencia = 1 / potencia

# Resultado
print(f"El resultado de la {base} elevado a {exponente} es {potencia}.")

"""
Nombre del Programa: ej13
Author: Francisco Manuel Villar Fernández
Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.
"""

# Pedimos la frase
frase = input("Introduce una frase: ")

# Inicializamos la variable
nueva_frase = ""

# Bucle
for i in frase:
    if i.isupper():
        nueva_frase += i.lower()
    elif i.islower():
        nueva_frase += i.upper()
    else:
        nueva_frase += i

# Resultado
print(f"La frase {frase} con las mayúsculas y minúsculas cambiadas es: {nueva_frase}")

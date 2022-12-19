"""
Nombre del Programa: ej11
Author: Francisco Manuel Villar Fernández
Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios),
realiza un programa que cuente cuantas palabras tiene.
"""

# Pedimos la frase
frase = input("Introduce una frase: ")

# Inicializamos la variable
contador = 0

# Bucle
for i in frase:
    if i == " ":
        contador += 1

# Resultado
print(f"La frase {frase} tiene {contador + 1} palabras.")

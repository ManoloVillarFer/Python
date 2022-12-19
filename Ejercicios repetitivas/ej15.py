"""
Nombre del Programa: ej15
Author: Francisco Manuel Villar Fernández
Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual
adelante que atrás.
"""

# Pedimos la frase
frase = input("Introduce una frase: ")

# Inicializamos la variable
nueva_frase = ""

# Bucle
for i in frase.upper():
    if i == "Á":
        nueva_frase += "A"
    elif i == "É":
        nueva_frase += "E"
    elif i == "Í":
        nueva_frase += "I"
    elif i == "Ó":
        nueva_frase += "O"
    elif i == "Ú":
        nueva_frase += "U"
    elif "A" <= i <= "Z":
        nueva_frase += i

# Variable invertida
invertida = ""

# Bucle
for i in nueva_frase:
    invertida = i + invertida

# Comprobamos si es palíndromo
if nueva_frase == invertida:
    print(f"La frase {frase} es un palíndromo.")
else:
    print(f"La frase {frase} no es un palíndromo.")

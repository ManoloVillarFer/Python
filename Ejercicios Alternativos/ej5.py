"""
5. Crea un programa que lea la edad de dos personas y diga quién es más joven,
la primera o la segunda.
Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.
"""

# Pedimos datos
edad1 = int(input("Edad de la primera persona: "))
edad2 = int(input("Edad de la segunda persona: "))

# Proceso
if edad1 < edad2:
    print("La primera persona es más joven.")
elif edad1 > edad2:
    print("La segunda persona es más joven.")
else:
    print("Las dos personas tienen la misma edad.")

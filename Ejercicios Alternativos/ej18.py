"""
18. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente.
Si introducimos otro número nos da un error.
"""

dia = int(input("Introduce el día de la semana: "))

# Calculos
if dia == 1:
    dia = "Lunes"
elif dia == 2:
    dia = "Martes"
elif dia == 3:
    dia = "Miércoles"
elif dia == 4:
    dia = "Jueves"
elif dia == 5:
    dia = "Viernes"
elif dia == 6:
    dia = "Sábado"
elif dia == 7:
    dia = "Domingo"
else:
    raise ValueError("ERROR: número incorrecto.")

# Salida
print("El día de la semana es", dia)

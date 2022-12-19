"""
19. Escribe un programa que pida un número entero entre uno y
doce e imprima el número de días que tiene el mes correspondiente.
"""

# Pedimos los datos
mes = int(input("Introduce el número de mes: "))

# Calculos
if mes == 1:
    mes = "Enero"
    dias = 31
elif mes == 2:
    mes = "Febrero"
    dias = 28
elif mes == 3:
    mes = "Marzo"
    dias = 31
elif mes == 4:
    mes = "Abril"
    dias = 30
elif mes == 5:
    mes = "Mayo"
    dias = 31
elif mes == 6:
    mes = "Junio"
    dias = 30
elif mes == 7:
    mes = "Julio"
    dias = 31
elif mes == 8:
    mes = "Agosto"
    dias = 31
elif mes == 9:
    mes = "Septiembre"
    dias = 30
elif mes == 10:
    mes = "Octubre"
    dias = 31
elif mes == 11:
    mes = "Noviembre"
    dias = 30
elif mes == 12:
    mes = "Diciembre"
    dias = 31
else:
    raise ValueError("ERROR: número incorrecto.")

# Salida
print(f"El mes {mes} tiene {dias} días.")

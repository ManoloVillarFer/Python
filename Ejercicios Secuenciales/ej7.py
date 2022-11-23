""" 7. Realiza un programa que reciba una cantidad de minutos
  y muestre por pantalla a cuantas horas y minutos corresponde"""

minutos = int(input("Dame una cantidad de minutos "))

horas = minutos // 60
mins = minutos % 60

print("Tenemos ", horas, "hora y", mins, "minutos")

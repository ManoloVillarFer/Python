""" 17. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
Escribir un algoritmo que determine la hora de llegada a la ciudad B."""

horasalida = int(input("Hora salida "))
minssalida = int(input("Minutos salida "))
segsalida = int(input("Segundos salida "))
hastardado = int(input("Has tardado en segundos "))

seginicio = horasalida*3600 + minssalida*60 + segsalida
segfin = seginicio + hastardado
horallegada = segfin // 3600
minllegada = (segfin % 3600) // 60
segllegada = (segfin % 3600) % 60

print("La hora de llegada sera", horallegada, ":", minllegada, ":", segllegada)

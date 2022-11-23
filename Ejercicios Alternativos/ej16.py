"""
16. La política de cobro de una compañía telefónica es: cuando se realiza una llamada,
el cobro es por el tiempo que está dura, de tal forma que los primeros cinco minutos cuestan 1 euro por minuto,
los siguientes tres, 80 céntimos por minuto, los siguientes dos minutos,
70 céntimos por minuto, y a partir del décimo minuto, 50 céntimos por minuto.

Además, se carga un impuesto de 3% cuando es domingo, y si es otro día, en turno de mañana,
15%, y en turno de tarde, 10%.
Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.
"""

# Datos
tiempo = int(input("¿Cuánto tiempo es la llamada?: "))
es_domingo = input("¿Es Domingo? (S/N): ")
if es_domingo == "N":
    turno = input("¿Qué turno: Mañana o Tarde? (M/T)?: ")

# Operaciones
if tiempo <= 5:
    coste = tiempo * 100

elif tiempo <= 8:
    coste = (tiempo-5) * 80 + 500

elif tiempo <= 10:
    coste = (tiempo-8) * 70 + 240 + 500

else:
    coste = (tiempo-10) * 50 + 140 + 240 + 500

# Impuestos
if es_domingo == "S":
    coste += coste * 0.03

elif turno == "M":
    coste += coste * 0.15

else:
    coste += coste * 0.10

# Mostramos en pantalla
print("El coste de la llamada:", coste / 100, "euros.")

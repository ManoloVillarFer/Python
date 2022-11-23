""" 10. Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.
Dicha calificación se compone de los siguientes porcentajes:

* 55% del promedio de sus tres calificaciones parciales.

* 30% de la calificación del examen final.

* 15% de la calificación de un trabajo final. """

# Se desea obtener la nota final
# 55% tres calificaciones parciales
# 30% examen final
# 15% trabajo final

ex1 = float(input("Introduce la nota del primer examen "))
ex2 = float(input("Introduce la nota del segundo examen "))
ex3 = float(input("Introduce la nota del tercer examen "))

exfinal = float(input("Introduce la nota del examen final "))

trabajo = float(input("Introduce la nota del trabajo final "))

parciales = (ex1+ex2+ex3)/3
parciales55 = parciales*0.55

exfinal = exfinal*0.30

trabajo = trabajo*0.15

print("La nota total del alumno sera", parciales55+exfinal+trabajo)


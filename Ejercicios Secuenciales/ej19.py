""" 19. Escribir un programa para calcular la nota final de un estudiante, considerando que:

Cada respuesta correcta suma 5 puntos
cada respuesta incorrecta suma -1 puntos
cada respuesta en blanco suma 0 puntos.
Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.
¿Qué tendrías que hacer para facilitar que los puntos que
suman los diferentes tipos de respuestas puedan cambiar en el futuro?
"""
import sys

CORRECTA = 5
INCORRECTA = 1

correcta = int(input("Preguntas correctas "))
incorrecta = int(input("Preguntas incorrectas "))

notafinal = (correcta * 5) - incorrecta
notafinal = notafinal/10

if notafinal > 10:
    print("Tu no puede ser mayor que 10 así que vuelve a introducir unos valores correctos", file=sys.stderr)
    sys.exit(1)

print("Tu resultado final es ", notafinal)

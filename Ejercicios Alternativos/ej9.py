""" 9. Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje
«Es signo de puntuación» solo si el carácter leído es un signo de puntuación,
«Es una letra» si es una letra (da igual que sea mayúscula, minúscula o acentuada),
«Es un dígito» si es un dígito, «Es otro carácter» si no es ninguno de los anteriores y
«No es un carácter» si el usuario ha introducido más de un carácter.

Pista: quizás te pueda venir bien usar el método find de la clase str.
"""
PUNTUACION = ".:!¡?¿\",;-^(){}[]"

caracter = input("Inserta un carácter: ")

if len(caracter) != 1:
    print("No es un caracter")
elif caracter in PUNTUACION:
    print("Es un signo de puntuación")
elif caracter.isalpha():
    print("Es una letra")
elif caracter.isdigit():
    print("Es un dígito")
else:
    print("No es ningún carácter de los anteriores")
    
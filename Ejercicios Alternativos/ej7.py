""" 7. Realiza un programa que calcule la potencia, para ello pide por teclado la base y el exponente.
Pueden ocurrir tres cosas:

El exponente sea positivo, solo tienes que imprimir la potencia.
El exponente sea 0, el resultado es 1.
El exponente sea negativo, el resultado es 1/potencia con el exponente positivo."""

base = int(input("Dame la base: "))
exponente = int(input("Dame el exponente: "))

potencia = base**exponente
negativo = 1 / potencia

if potencia:
    print(potencia)
elif exponente == 0:
    print("El resultado es 1")
else:
    print(negativo)

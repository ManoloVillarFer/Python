""" 20. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
después de pedirnos cuantas monedas
tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos). """

dos = float(input("Cuantas monedas de dos euros tienes: "))
un = float(input("Cuantas monedas de un euro tienes: "))
cincuenta = float(input("Cuantas monedas de cincuenta céntimos tienes: "))
veinte = float(input("Cuantas monedas de veinte céntimos tienes: "))
diez = float(input("Cuantas monedas de diez céntimos tienes: "))
```
dos = 2 * dos
un = 1 * un
cincuenta = (50 * cincuenta) / 100
veinte = (20 * veinte) / 100
diez = (10 * diez) / 100
euros = dos+un+cincuenta+veinte+diez
doseurosacentimos = 100 * dos
uneuroacentimos = 100 * un
cincuentacentimos = 100 * cincuenta
veintecentimos = 100 * veinte
diez = 100 * diez
cent = doseurosacentimos+uneuroacentimos+cincuentacentimos+veintecentimos+diez
```
# Salida por pantalla
print("Tienes", euros, "euros y", cent, "céntimos")

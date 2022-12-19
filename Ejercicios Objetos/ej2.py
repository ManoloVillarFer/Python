"""
Nombre del Programa: ej2
Author: Francisco Manuel Villar Fernández
Crea una clase, y pruébala, que modele fracciones. Debe permitir:

Crear fracciones indicando numerador y denominador.
 Ejemplo: f = Fraction(2, 3)
Ojo!!! No se puede tener un denominador cero.
Las fracciones pueden operar entre sí.
Sumar, multiplicar, dividir, restar.
Ojo!!! esto se puede hacer: f + 1, 5 * f
Las fracciones se pueden comparar.
==, <, <=, >, >=, !=
Ojo!!! estas dos fracciones son iguales: 1/2 y 2/4
Ojo!!! esto se puede hacer 1 < 1/2
"""


# Creamos la clase Fraction
class Fraction:


# Inicializamos la clase
    def __init__(self, numerator=0, denominator=1):
        if not isinstance(numerator, int):
            raise ValueError(f"Error en numerador: '{numerator}' no es un entero")
        elif not isinstance(denominator, int) or denominator == 0:
            raise ValueError(f"Error en el denominador: '{denominator}' no es un entero diferente de 0")

        self.numerator, self.denominator = numerator, denominator

# Lo pasamos a cadena
    def __str__(self):
        return str(f"{self.__numerator}/{self.__denominator}")

# Obtenemos los valores
    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

# Nuevos valores
    @numerator.setter
    def numerator(self, value_numerator):
        if not isinstance(value_numerator, int):
            raise ValueError(f"Error en numerador: '{value_numerator}' no es un entero")
        self.__numerator = value_numerator

    @denominator.setter
    def denominator(self, value_denominator):
        if not isinstance(value_denominator, int) or value_denominator == 0:
            raise ValueError(f"Error en el denominador: '{value_denominator}' no es un entero diferente de 0")
        self.__denominator = value_denominator

# No vamos a modificar el estado de la instancia
    @staticmethod
    def __fraction_to_number(fraction):
        return fraction.numerator / fraction.denominator

    @staticmethod
    def __first_numerator(fraction1, fraction2):
        return fraction1.__numerator * \
               (fraction1.__denominator, fraction2.__denominator // fraction1.__denominator)

    @staticmethod
    def __second_numerator(fraction1, fraction2):
        return fraction2.__numerator * \
               (fraction1.__denominator, fraction2.__denominator) // fraction2.__denominator

# Suma de fracciones
    def __add__(self, new_fraction):
        if isinstance(new_fraction, str):
            raise ValueError(f"Error al sumar: '{new_fraction}' es una cadena de caracteres")
        else:
            if isinstance(new_fraction, int):
                return Fraction(self.__numerator + (new_fraction * self.__denominator), self.__denominator)
            else:
                first_numerator = Fraction.__first_numerator(self, new_fraction)
                second_numerator = Fraction.__second_numerator(self, new_fraction)
                return Fraction((first_numerator + second_numerator),
                                (self.__denominator, new_fraction.__denominator)
# Multiplicación de fracciones (a la derecha)

    def __radd__(self, new_fraction):
        if isinstance(new_fraction, str):
            raise ValueError(f"Error al sumar: '{new_fraction}' es una cadena de caracteres")
        else:
            if isinstance(new_fraction, int):
                return Fraction(self.__numerator + (new_fraction * self.__denominator), self.__denominator)

# Resta de fracciones
    def __sub__(self, new_fraction):
        if isinstance(new_fraction, str):
            raise ValueError(f"Error al restar: '{new_fraction}' es una cadena de caracteres")
        else:
            if isinstance(new_fraction, int):
                return Fraction(self.__numerator - (new_fraction * self.__denominator), self.__denominator)
            else:
                first_numerator = Fraction.__first_numerator(self, new_fraction)
                second_numerator = Fraction.__second_numerator(self, new_fraction)
                return Fraction((first_numerator - second_numerator),
                                (self.__denominator, new_fraction.__denominator)

# Resta de fracciones (a la derecha)
    def __rsub__(self, new_fraction):
        if isinstance(new_fraction, str):
            raise ValueError(f"Error al sumar: '{new_fraction}' es una cadena de caracteres")
        else:
            if isinstance(new_fraction, int):
                return Fraction(self.__numerator - (new_fraction * self.__denominator), self.__denominator)

# Multiplicación de fracciones
    def __mul__(self, new_fraction):
        if isinstance(new_fraction, str):
            raise ValueError(f"Error al multiplicar: '{new_fraction}' es una cadena de caracteres")
        else:
            if isinstance(new_fraction, int):
                return Fraction(self.__numerator * new_fraction, self.__denominator)
            else:
                return Fraction(self.__numerator * new_fraction.__numerator,
                                self.__denominator * new_fraction.__denominator)

# Multiplicación de fracciones (a la derecha)
    def __rmul__(self, new_fraction):
        if isinstance(new_fraction, str):
            raise ValueError(f"Error al multiplicar: '{new_fraction}' es una cadena de caracteres")
        else:
            if isinstance(new_fraction, int):
                return Fraction(self.__numerator * new_fraction, self.__denominator)

# División de fracciones
    def __truediv__(self, new_fraction):
        if isinstance(new_fraction, str):
            raise ValueError(f"Error al dividir: '{new_fraction}' es una cadena de caracteres")
        else:
            if isinstance(new_fraction, int):
                return Fraction(self.__numerator, self.__denominator * new_fraction)
            else:
                return Fraction(self.__numerator * new_fraction.__denominator,
                                self.__denominator * new_fraction.__numerator)

# División de fracciones (a la derecha)
    def __rtruediv__(self, new_fraction):
        if isinstance(new_fraction, str):
            raise ValueError(f"Error al dividir: '{new_fraction}' es una cadena de caracteres")
        else:
            if isinstance(new_fraction, int):
                return Fraction(self.__numerator, self.__denominator * new_fraction)

# Comparadores
    def __eq__(self, new_fraction):
        if isinstance(new_fraction, int) or isinstance(new_fraction, float):
            return Fraction.__fraction_to_number(self) == new_fraction
        else:
            return self.__numerator == new_fraction.__numerator and self.__denominator == new_fraction.__denominator

    def __ne__(self, new_fraction):
        if isinstance(new_fraction, int) or isinstance(new_fraction, float):
            return Fraction.__fraction_to_number(self) != new_fraction
        else:
            return self.__numerator != new_fraction.__numerator or self.__denominator != new_fraction.__denominator

    def __lt__(self, new_fraction):
        if isinstance(new_fraction, int) or isinstance(new_fraction, float):
            return Fraction.__fraction_to_number(self) < new_fraction
        else:
            return Fraction.__fraction_to_number(self) < Fraction.__fraction_to_number(new_fraction)

    def __le__(self, new_fraction):
        if isinstance(new_fraction, int) or isinstance(new_fraction, float):
            return Fraction.__fraction_to_number(self) <= new_fraction
        else:
            return Fraction.__fraction_to_number(self) <= Fraction.__fraction_to_number(new_fraction)

    def __gt__(self, new_fraction):
        if isinstance(new_fraction, int) or isinstance(new_fraction, float):
            return Fraction.__fraction_to_number(self) > new_fraction
        else:
            return Fraction.__fraction_to_number(self) > Fraction.__fraction_to_number(new_fraction)

    def __ge__(self, new_fraction):
        if isinstance(new_fraction, int) or isinstance(new_fraction, float):
            return Fraction.__fraction_to_number(self) >= new_fraction
        else:
            return Fraction.__fraction_to_number(self) >= Fraction.__fraction_to_number(new_fraction)


def main():
    fraction1 = Fraction(8, 15)
    print(f"Primera fracción: {fraction1}")

    fraction2 = Fraction(6, 22)
    print(f"Segunda fracción: {fraction2}")

    print(f"La suma de {fraction1} + {fraction2} es: {fraction1 + fraction2}")
    print(f"La suma de {fraction2} + 10 es: {fraction2 + 10}")

    print(f"La resta de {fraction1} - {fraction2} es: {fraction1 - fraction2}")
    print(f"La resta de 5 - {fraction1} es: {5 - fraction1}")

    print(f"La multiplicación de {fraction1} * {fraction2} es: {fraction1 * fraction2}")
    print(f"La multiplicación de 9 * {fraction1} es: {9 - fraction1}")

    print(f"La división de {fraction1} / {fraction2} es: {fraction1 / fraction2}")
    print(f"La división de {fraction1} / 6 es: {fraction1 / 6}")

    print(f"¿Es {fraction1} igual que {fraction2}? {fraction1 == fraction2}")
    print(f"¿Es {fraction1} distinto a {fraction2}? {fraction1 != fraction2}")
    print(f"¿Es {fraction1} menor que {fraction2}? {fraction1 < fraction2}")
    print(f"¿Es {fraction1} menor o igual que {fraction2}? {fraction1 <= fraction2}")
    print(f"¿Es {fraction1} mayor que {fraction2}? {fraction1 > fraction2}")
    print(f"¿Es {fraction1} mayor o igual que {fraction2}? {fraction1 >= fraction2}")


if __name__ == '__main__':
    main()

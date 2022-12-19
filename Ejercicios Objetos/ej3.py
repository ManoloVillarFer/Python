"""
Nombre del Programa: ej3
Author: Francisco Manuel Villar Fernández
En Python podemos manejar fechas pero no nos gusta, vamos a crear una clase Date. Debe permitir:

Crear fechas.
Ejemplo: f = Date(17, 11, 2022)
Ojo!!! Estas fechas son erróneas:
Date(78, -45, 0)
Date(31, 6, 2022)
Date(29, 2, 2022)
Las fechas se pueden comparar.
A las fechas se le pueden sumar y restar días.
Las fechas se pueden restar.
Se debe poder averiguar el día de la semana de una fecha.
"""

# Creamos la clase Date
class Date:

    # Inicializamos la clase ponemos los valores de día, mes y año a 1
    def __init__(self, day=1, month=1, year=1):
        if not Date.__correct(day, month, year):
            raise ValueError("La fecha introducida es incorrecta")
        self.__year, self.__month, self.__day = year, month, day

    # Pasamos a cadena
    def __str__(self):
        return str(f"{self.__day} de {self.name_month()} de {self.__year}")

    # Obtenemos los valores
    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    # Nuevos valores
    @day.setter
    def day(self, new_day):
        if not Date.__correct(new_day, self.__month, self.__year):
            raise ValueError(f"El día asignado {new_day} es incorrecto")
        self.__day = new_day

    @month.setter
    def month(self, new_month):
        if not Date.__correct(self.__day, new_month, self.__year):
            raise ValueError(f"El mes asignado {new_month} es incorrecto")
        self.__month = new_month

    @year.setter
    def year(self, new_year):
        if not Date.__correct(self.__day, self.__month, new_year):
            raise ValueError(f"El año asignado {new_year} es incorrecto")
        self.__year = new_year

    # No modificamos la instancia
    @staticmethod
    def __leap_year(year):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    @staticmethod
    def __correct(day, month, year):
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            return False
        elif year < 0:
            return False
        elif month < 1 or month > 12:
            return False
        else:
            return 0 < day <= Date.__day_month(month, year)

    @staticmethod
    def __day_month(month, year):
        day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Date.__leap_year(year):
            day_month[1] = 29
        return day_month[month - 1]

    # Sumamos un día
    def __sum_1day(self):
        year, month, day = self.__year, self.__month, self.__day + 1

        if day > Date.__day_month(month, year):
            day = 1
            month += 1

        if month > 12:
            month = 1
            year += 1

        return Date(day, month, year)

    # Restamos un día
    def __rest_1day(self):
        year, month, day = self.__year, self.__month, self.__day - 1

        if day == 0:
            month -= 1

            if month == 0:
                month = 12
                year -= 1

            day = Date.__day_month(month, year)

        return Date(day, month, year)

    # Cambiamos el número del mes por su nombre
    def name_month(self):
        month = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        return month[self.month - 1]

    # Buscamos el día de la semana que es una fecha
    def name_day(self):
        up_year = self.__year // 100
        sub_year = self.__year % 100

        century, month, a = 0, 0, 0

        # Bucle para asignar la costante "a" dependiendo del siglo de la fecha
        while up_year >= century:
            if up_year == century:
                a = 6
            century += 1

            if up_year == century:
                a = 4
            century += 1

            if up_year == century:
                a = 2
            century += 1

            if up_year == century:
                a = 0
            century += 1

        # Dependiendo del mes del año le asignaremos a dicho mes un valor para el cálculo del día de la semana
        if self.__month == 1:
            if self.__leap_year(self.__year):
                month = 6
            else:
                month = 0
        elif self.__month == 2:
            if self.__leap_year(self.__year):
                month = 2
            else:
                month = 3
        elif self.__month == 3:
            month = 3
        elif self.__month == 4:
            month = 6
        elif self.__month == 5:
            month = 1
        elif self.__month == 6:
            month = 4
        elif self.__month == 7:
            month = 6
        elif self.__month == 8:
            month = 2
        elif self.__month == 9:
            month = 5
        elif self.__month == 10:
            month = 0
        elif self.__month == 11:
            month = 3
        elif self.__month == 12:
            month = 5

        # Formula que calcula el dia de la semana
        day = (self.__day + month + sub_year + (sub_year // 4) + a) % 7

        # Dependiendo del resto de la operación se asigna un día de la semana
        if day == 0:
            return str("Domingo")
        elif day == 1:
            return str("Lunes")
        elif day == 2:
            return str("Martes")
        elif day == 3:
            return str("Miércoles")
        elif day == 4:
            return str("Jueves")
        elif day == 5:
            return str("Viernes")
        elif day == 6:
            return str("Sábado")

    # Suma de días y fechas
    def __add__(self, new_date):
        sum_date = Date(self.__day, self.__month, self.__year)
        if new_date > 0:
            for i in range(new_date):
                sum_date = sum_date.__sum_1day()
        else:
            for i in range(new_date):
                sum_date = sum_date.__rest_1day()

        return sum_date

    def __radd__(self, new_date):
        sum_date = Date(self.__day, self.__month, self.__year)
        if new_date > 0:
            for i in range(new_date):
                sum_date = sum_date.__sum_1day()
        else:
            for i in range(new_date):
                sum_date = sum_date.__rest_1day()

        return sum_date

    # Resta de días y fechas
    def __sub__(self, new_date):
        if isinstance(new_date, int):
            return self + -1 * new_date
        else:
            rest_date, days = Date(self.__day, self.__month, self.__year), 0

            if rest_date < new_date:
                raise ValueError(f"Error al restar fechas: '{new_date}' es mayor que '{rest_date}'")

            while rest_date > new_date:
                rest_date = rest_date.__rest_1day()
                days += 1

            return days

    def __rsub__(self, new_date):
        return self + -1 * new_date

    # Comparadores
    def __eq__(self, compare_date):
        return self.__year == compare_date.year and self.__month == compare_date.month and self.__day == compare_date.day

    def __ne__(self, compare_date):
        return self.__year != compare_date.year or self.__month != compare_date.month or self.__day != compare_date.day

    def __lt__(self, compare_date):
        if self.__year != compare_date.year:
            return self.__year < compare_date.year
        elif self.__month != compare_date.month:
            return self.__month < compare_date.month
        else:
            return self.__day < compare_date.day

    def __le__(self, compare_date):
        if self.__year != compare_date.year:
            return self.__year <= compare_date.year
        elif self.__month != compare_date.month:
            return self.__month <= compare_date.month
        else:
            return self.__day <= compare_date.day

    def __gt__(self, compare_date):
        if self.__year != compare_date.year:
            return self.__year > compare_date.year
        elif self.__month != compare_date.month:
            return self.__month > compare_date.month
        else:
            return self.__day > compare_date.day

    def __ge__(self, compare_date):
        if self.__year != compare_date.year:
            return self.__year >= compare_date.year
        elif self.__month != compare_date.month:
            return self.__month >= compare_date.month
        else:
            return self.__day >= compare_date.day


# Función para probar fechas
def main():
    date1 = Date(16, 11, 1999)
    print(f"Primera fecha: {date1}")

    # Introducción de la segunda fecha
    date2 = Date()
    date2.day = 16
    date2.month = 12
    date2.year = 2022
    print(f"Segunda fecha: {date2}")

    print(f"La suma de {date1} + 365 días es: {date1 + 365}")
    print(f"La suma de 31 días + {date2} es: {31 + date2}")

    print(f"La resta de {date2} - 720 días es: {date2 + 720}")
    print(f"La resta de 80 días - {date1} es: {80 + date1}")
    print(f"La resta de {date2} - {date1} es: {date2 - date1} días ({(date2 - date1) // 365} años)")

    print(f"¿Es {date1} igual que {date2}? {date1 == date2}")
    print(f"¿Es {date1} diferente a {date2}? {date1 != date2}")
    print(f"¿Es {date1} menor que {date2}? {date1 < date2}")
    print(f"¿Es {date1} menor o igual que {date2}? {date1 <= date2}")
    print(f"¿Es {date1} mayor que {date2}? {date1 > date2}")
    print(f"¿Es {date1} mayor o igual que {date2}? {date1 >= date2}")

    print(f"¿Qué día de la semana fue el {date1}? {Date.name_day(date1)}")
    print(f"¿Qué día de la semana fue el {date2}? {Date.name_day(date2)}")


if __name__ == '__main__':
    main()

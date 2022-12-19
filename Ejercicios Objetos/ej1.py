"""
Nombre del Programa: ej1
Author: Francisco Manuel Villar Fernández
En Python existen clases para manipular duraciones de tiempo (horas:minutos:segundos), pero no nos gustan,
vamos a hacer una nueva que se llamará Duration. Debe permitir:

Crear duraciones de tiempos.
Ejemplo: t = Duration(10,20,56)
Ojo!!! (10, 62, 15) se debe guardar como (11, 2, 15)
Las duraciones de tiempo se pueden comparar.
A las duraciones de tiempo les puedo sumar y restar segundos.
Las duraciones de tiempo se pueden sumar y restar.
"""


# Creamos la clase Duration
class Duration:

# Inicializamos la clase ponemos los valores de horas, minutos y segundos a 0
    def __init__(self, h=0, m=0, s=0):
        self.__h = h
        self.__m = m
        self.__s = s
        self.normalizar()

# Creamos el método normalizar
    def normalizar(self):
        total_segundos = self.__h * 3600 + self.__m * 60 + self.__s
        if total_segundos < 0:
            raise ValueError('La duración no puede ser negativa')
        self.__h, total_segundos = divmod(total_segundos, 3600)
        self.__m, self.__s = divmod(total_segundos, 60)

# Obtenemos los valores
    @property
    def h(self):
        return self.__h

    @property
    def m(self):
        return self.__m

    @property
    def s(self):
        return self.__s

# Modificamos para nuevos valores
    @h.setter
    def h(self, nuevo_valor_h):
        if nuevo_valor_h < 0:
            raise ValueError('La hora no puede ser negativa')
        self.__h = nuevo_valor_h

    @m.setter
    def m(self, nuevo_valor_m):
        self.__m = nuevo_valor_m
        self.__normalizar()

    @s.setter
    def s(self, nuevo_valor_s):
        self.__s = nuevo_valor_s
        self.__normalizar()

    def __str__(self):  # usaremos esta función cuando quiera pasar el objeto a cadena
        return f"({self.__h}:{self.__m}:{self.__s})"

# Suma de segundos
    def suma_s(self, p):
        self.__s += p
        if self.__s > 60:
            while True:
                self.__m += 1
                self.__s -= 60
                if self.__s <= 60:
                    break
# Suma de minutos
        if self.__m > 60:
            while True:
                self.__h += 1
                self.__m -= 60
                if self.__m <= 60:
                    break
        return self

# Resta de segundos
    def resta_s(self, p):
        total_self = self.__h * 3600 + self.__m * 60 + self.__s
        total_s = total_self - p
        horas = int(total_s / 60 / 60)
        total_s -= horas * 60 * 60
        minutos = int(total_s / 60)
        total_s -= minutos * 60
        return f"{abs(horas)}:{abs(minutos)}:{abs(total_s)}"

# Restamos la instancia
    def __sub__(self, p):
        if isinstance(p, int):
            return self + -p
        elif isinstance(p, Duration):
            return Duration(self.__h - p.__h, self.__m - p.__m, self.__s - p.__s)
        raise ValueError('El valor sumado debe ser entero')

# Sumamos la instancia
    def __add__(self, p):
        if isinstance(p, int):
            return Duration(self.__h, self.__m, self.__s + p)
        elif isinstance(p, Duration):
            return Duration(self.__h + p.__h, self.__m + p.__m, self.__s + p.__s)
        raise ValueError('El valor sumado debe ser entero')

        # Comparadores

    def __eq__(self, p):
        return self.__h == p.__h and self.__m == p.__m and self.__s == p.__s

    def __ne__(self, p):
        return not self == p

    def __lt__(self, p):
        total_self = self.__h * 3600 + self.__m * 60 + self.__s
        total_p = p.__h * 3600 + p.__m * 60 + p.__s
        return total_self < total_p

    def __le__(self, p):
        return self < p or self == p

    def __gt__(self, p):
        return not self < p and self != p

    def __ge__(self, p):
        return not self < p

    def __ne__(self, p):
        return not self == p


t1 = Duration(10, 80, 0)
t2 = Duration(20, 0, 10)

print(t1 - 63)
print(t2 - 105)
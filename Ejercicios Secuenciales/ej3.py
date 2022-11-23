# 3. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math
try:
    c1 = float(input("Dame el valor del primer cateto"))
    c2 = float(input("Dame el valor del segundo cateto"))

except ValueError:
    print("Debes poner punto en lugar de coma")

hipotenusa = math.sqrt(c1**2 + c2**2)

print("La hipotenusa de este triángulo rectángulo es", hipotenusa)


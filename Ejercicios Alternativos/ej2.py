""" 2. Indica qué líneas del último programa (y en qué orden) se ejecutarán para cada uno
de los siguientes casos:
1) a = 2 y b = 6.
Se ejecutará cuando a sea igual a 2 y b a 6
2) a = 0 y b = 3.
Se ejecutará cuando a sea igual a 0 y b a 3
3) a = 0 y b = −3.
Se ejecutará cuando a sea igual a 0 y b a -3
4) a = 0 y b = 0.
Se ejecutará cuando a sea igual a 0 y b a 0
"""

a = int(input("Dame un valor de a: "))
b = int(input("Dame un valor de b: "))

if a == 2 and b == 6:
    print("Se ejecutará 1")

elif a == 0 and b == 3:
    print("Se ejecutará 2")

elif a == 0 and b == -3:
    print("Se ejecutará 3")

elif a == 0 and b == 0:
    print("Se ejecutará 4")

else:
    print("Los valores de A deben ser 2 o 0, los valores de B deben ser -3, 0, 3, 6")

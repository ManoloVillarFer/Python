# 18. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Dime tu nombre ")
ap1 = input("Dime tu nombre ")
ap2 = input("Dime tu nombre ")

iniciales = (nombre[0], ap1[0], ap2[0].upper())

print("Las iniciales de ", nombre, "", ap1, "", ap2, "son", iniciales)

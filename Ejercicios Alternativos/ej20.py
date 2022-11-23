""" 20. Una compañía de transporte internacional tiene servicio en algunos países de América del Norte,
 América Central, América del Sur, Europa y Asia.
 El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido.
 Lo anterior se muestra en la tabla:

ZONA	UBICACIÓN	COSTO/GRAMO
1	América del Norte	24.00 euros
2	América Central	20.00 euros
3	América del Sur	21.00 euros
4	Europa	10.00 euros
5	Asia	18.00 euros
Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados,
esto por cuestiones de logística y de seguridad.
Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso,
el rechazo de la entrega.
"""

# Pedimos los datos
peso = float(input("Introduce el peso de paquete en gramos: "))

# Calculos y de nuevo datos
if 0 < peso <= 5000:
    print("Elige zona de destino")
    print("Zona     Ubicación                                       Precio")
    print("---------------------------------------------------------------")
    print("1        América del Norte el envío es de 24.00 euros por gramo")
    print("2        América Central el envío es de 20.00 euros por gramo")
    print("3        América del Sur el envío es de 21.00 euros por gramo")
    print("4        Europa el envío es de 10.00 euros por gramo")
    print("5        Asia el envío es de 18.00 euros por gramo")

    zona = int(input("Introduce la zona a la que va dirigida el paquete: "))

    if zona == 1:
        peso = peso * 24
        print("Tendrás que pagar", peso, "euros")

    elif zona == 2:
        peso = peso * 20
        print("Tendrás que pagar", peso, "euros")

    elif zona == 3:
        peso = peso * 21
        print("Tendrás que pagar", peso, "euros")

    elif zona == 4:
        peso = peso * 10
        print("Tendrás que pagar", peso, "euros")

    elif zona == 5:
        peso = peso * 18
        print("Tendrás que pagar", peso, "euros")
    else:
        print("Esta zona esta mal")

else:
    print("No se puede enviar")


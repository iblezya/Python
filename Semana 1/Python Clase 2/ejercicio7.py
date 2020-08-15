cantidad = float(input("Ingrese la cantidad de kilos: "))
precio_inicial = float(input("Ingrese el precio inicial al kilo de uva: S/. "))
tipo = str(input("Ingrese el tipo de uva (A o B): "))
tamaño = int(input("Ingrese el tamaño de uva (1 o 2): "))
a1 = 0.2
a2 = 0.3
b1 = -0.3
b2 = -0.5
if tipo==str("A") and tamaño==int("1"):
    precio_final = cantidad*(precio_inicial + a1 )
    ganancia = cantidad*a1
    print("El precio final por ",cantidad," kilos es S/. ",precio_final)
    print("La ganacia es S/. ",ganancia)
elif tipo==str("A") and tamaño==int("2"):
    precio_final = cantidad*(precio_inicial + a2)
    ganancia = cantidad*a2
    print("El precio final por ",cantidad," kilos es S/. ",precio_final)
    print("La ganacia es S/. ",ganancia)
elif tipo==str("B") and tamaño==int("1"):
    precio_final = cantidad*(precio_inicial + b1)
    perdida = cantidad*(-b1)
    print("El precio final por ",cantidad," kilos es S/. ",precio_final)
    print("La perdida es S/. ",perdida)
else:
    precio_final = cantidad*(precio_inicial + b2)
    perdida = cantidad*(-b2)
    print("El precio final por ",cantidad," kilos es S/. ",precio_final)
    print("La perdida es S/. ",perdida)

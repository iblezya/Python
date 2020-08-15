print("="*50)
precio_traje = float(input("Ingrese el precio del traje: S/. "))
print("="*50)
if precio_traje>250:
    print("="*50)
    d1 = precio_traje*0.15
    print("Usted tiene un descuento del 15% que es S/. ",d1)
    precio_final = precio_traje*0.85
    print("El precio final del traje es S/. ",precio_final)
else:
    print("="*50)
    d2 = precio_traje*0.08
    print("Usted tiene un descuento del 8% que es S/. ",d2)
    precio_final = precio_traje*0.92
    print("El precio final del traje es S/. ",precio_final)
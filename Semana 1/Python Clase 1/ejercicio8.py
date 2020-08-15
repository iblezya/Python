print("Este programa cálcula el pago por m3 de agua usado en una piscina.")
print("="*50)
a = float(input("Ingrese la primera dimensión de la piscina: "))
b = float(input("Ingrese la segunda dimensión de la piscina: "))
c = float(input("Ingrese la tercera dimensión de la piscina: "))
precio = float(input("Ingrese el precio de Sedapal por m3: S/. "))
vol = a*b*c
pago = precio*vol
print("="*50)
print("El volúmen de la piscina es: ",vol," m3")
print("El pago por el volumen en m3 de la piscina es: S/. ",pago)
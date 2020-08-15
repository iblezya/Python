print("="*50)
alumnos = int(input("Ingrese el número de alumnos: "))
c1 = 65
c2 = 70
c3 = 95
print("="*50)
if alumnos>=100:
    pago = alumnos*c1
    print("Se cobra S/. ",c1," por cada alumno y se paga a la compañia de viajes S/. ",pago)
elif 100>alumnos and alumnos>=50:
    pago = alumnos*c2
    print("Se cobra S/. ",c2," por cada alumno y se paga a la compañia de viajes S/. ",pago)
elif 50>alumnos and alumnos>=30:
    pago = alumnos*c3
    print("Se cobra S/. ",c3," por cada alumno y se paga a la compañia de viajes S/. ",pago)
else:
    pago = 4000
    c4 = pago/alumnos
    print("Se cobra S/. ",c4," por cada alumno y se paga a la compañia de viajes S/. ",pago)
    print("="*50)
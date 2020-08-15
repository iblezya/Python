print("="*50)
llamada = float(input("Ingrese el número de minutos: "))
if llamada <= 5:
    pago_llamada = 1*llamada
elif llamada <= 8:
    pago_llamada = 5 + (llamada-5)*0.8
elif llamada <= 10:
    pago_llamada = 5 + 2.4 + (llamada-8)*0.7
else:
    pago_llamada = 5 + 2.4 + 1.4 + (llamada-10)*0.5
dia_ingreso = int(input("Ingrese \"1\" para domingo y \"2\" para día habil: "))
if dia_ingreso == 1:
    precio_final = pago_llamada*1.05
    print("="*50)
    print("Usted debe pagar S/. ",precio_final," por la llamada.")
    print("="*50)
elif dia_ingreso == 2:
    turno = int(input("Ingrese \"1\" para matutino y \"2\" para vespertino: "))
    print("="*50)
    if turno == 1:
        precio_final = pago_llamada*1.15
        print("Usted debe pagar S/. ",precio_final," por la llamada.")
        print("="*50)
    elif turno == 2:
        precio_final = pago_llamada*1.10
        print("Usted debe pagar S/. ",precio_final," por la llamada.")
        print("="*50)
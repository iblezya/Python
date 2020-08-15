while (True):
    try:
        Consumo = float(input('Ingrese la cantidad de su consumo(S/.): '))
        if Consumo > 100:
            MontoFinal = 0.7*Consumo
        elif 100 >= Consumo > 60:
            MontoFinal = 0.8*Consumo
        elif 60 >= Consumo > 30:
            MontoFinal = 0.85*Consumo
        elif 30 >= Consumo > 0:
            MontoFinal = 0.9*Consumo
        else:
            print('Ingrse su consumo mayor a 0.')
            continue
        break
    except ValueError:
        print('Error. Intente de nuevo.')
print('Promocion de descuento.')
print(f'El monto final a pagar por su consumo es S/.{(MontoFinal):.2f}')
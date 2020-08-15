Nombre = str(input('Ingrese el nombre del producto: '))
while (True):
    try:
        Precio = float(input('Ingrese el precio del producto(S/.): '))        
        Cantidad = int(input('Ingrese la cantidad de productos: '))
        Monto = Precio*Cantidad
        if Cantidad >= 100:
            MontoFinal = 0.6*Monto
        elif 100 > Cantidad >= 25:
            MontoFinal = 0.8*Monto
        elif 25 > Cantidad >= 10:
            MontoFinal = 0.9*Monto
        elif 10 > Cantidad >= 1:
            MontoFinal = Monto
        else:
            print('Mínima cantidad permitida: 1. Intente de nuevo.')
            continue
        break
    except ValueError:
        print('Error. Intente de nuevo.')
print('\nUsted acaba de comprar: ',Nombre)
print('Cantidad: ',Cantidad,'productos.')
print('Monto final a pagar: S/.',MontoFinal)
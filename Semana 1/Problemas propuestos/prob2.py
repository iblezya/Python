i = 1
def Prob2():    
    print('*'*35)
    PrecioProducto = 0
    while (True):
        try:        
            PrecioProducto = float(input('Ingrese el precio del producto (S/.): '))
            while PrecioProducto<=0:
                print('Tiene que ingresar un valor positivo.')
                PrecioProducto = float(input('Ingrese el precio del producto (S/.): '))
            break
        except ValueError:
            print("¡Error! Ingrese correctamente los datos.")
    CantidadUnidades = 0
    while (True):
        try:        
            CantidadUnidades = int(input('Ingrese la cantidad de unidades: '))
            while CantidadUnidades<=0:
                print('Tiene que ingresar un valor positivo.')
                CantidadUnidades = int(input('Ingrese la cantidad de unidades: '))
            break
        except ValueError:
            print("¡Error! Ingrese correctamente los datos.")
    print('*'*35)
    ImporteCompra = PrecioProducto*CantidadUnidades
    if CantidadUnidades>10:
        Descuento = 0.15*ImporteCompra
        ImportePagar = ImporteCompra - Descuento
    else:
        Descuento = 0.05*ImporteCompra
        ImportePagar = ImporteCompra - Descuento
    if ImportePagar>200:
        gift = 'una agenda'
    else:
        gift = 'un cuaderno'
    print(f'El importe de compra es S/. {(ImporteCompra):.2f} .'+
        f"\nEl importe de descuento es S/. {(Descuento):.2f} ."+
        f"\nEl importe a pagar es S/. {(ImportePagar):.2f} ."+
        f"\nLa tienda le obsequia {(gift)}.\nGracias por su compra.")
while i<=1:
    Prob2()
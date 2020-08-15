print('Este programa ayuda al vendedor a organizar el monto en 3 tipos de venta.')
print('1. Tipo C: Menor o igual a S/. 10 000\n2. Tipo B: Mayor a S/. 10 000 y menor a S/. 20 000')
print('3 Tipo A: Mayor o igual a S/. 20 000\nY por último cálcula el monto local y global')
print('*'*30)
while (True):
    try:
        n_ventas = int(input('Ingrese la cantidad de ventas: '))
        while n_ventas<0:
            print('Ingrese como mínimo 1 venta.')
            n_ventas = int(input('Ingrese la cantidad de ventas: '))
        break
    except ValueError:
        print('Error intente de nuevo.')
tipoA = []
tipoB = []
tipoC = []
for i in range(1,(n_ventas+1)):    
    while (True):
        try:  
            venta = float(input(f'Ingrese su venta {i}: '))
            if venta > 0 and venta <= 10000:                
                tipoC.append(venta)
                break
            elif 10000 <venta < 20000:
                tipoB.append(venta)
                break
            elif venta >= 20000:
                tipoA.append(venta)
                break
            else:
                print('Error intente de nuevo.')                     
        except ValueError:
            print('Error intente de nuevo.')    
sumatoriaTipoA = sum(tipoA)
sumatoriaTipoB = sum(tipoB)
sumatoriaTipoC = sum(tipoC)
total = sumatoriaTipoA + sumatoriaTipoB + sumatoriaTipoC
print('')
print('El monto en el Tipo A es S/. ',sumatoriaTipoA)
print('El monto en el Tipo B es S/. ',sumatoriaTipoB)
print('El monto en el Tipo C es S/. ',sumatoriaTipoC)
print('El monto total es S/. ',total)
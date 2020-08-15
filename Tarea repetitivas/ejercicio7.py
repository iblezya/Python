print('Este programa determina el impuesto por cada vehículo de la siguiente manera.')
print('1. Categoría 1: 10% de su valor\n2. Categoría 2: 7% de su valor')
print('3 Categoría 1: 5% de su valor\nAdicionalmente cálcula el impuesto por categoría y total.')
print('*'*30)
while (True):
    try:
        n_vehiculos = int(input('Ingrese la cantidad de vehículos: '))
        while n_vehiculos<0:
            print('Ingrese como mínimo 1 vehículo.')
            n_vehiculos = int(input('Ingrese la cantidad de vehículos: '))
        break
    except ValueError:
        print('Error intente de nuevo.')
#dictCategoriasValor = {}
listaImpuesto1 = []
listaImpuesto2 = []
listaImpuesto3 = []
print('Ingrese 1 , 2 o 3 para indicar la categoria del vehiculo.')
for i in range(1,(n_vehiculos+1)):    
    while (True):
        try:  
            categoriaVehiculo = int(input(f'Ingrese la categoría del vehículo {i}: '))
            if categoriaVehiculo>0 and categoriaVehiculo<4:
                break
            else:
                print('Ingrese una opción correcta')
        except ValueError:
            print('Error intente de nuevo')
    while (True):
        try:
            valorVehiculo = float(input('Ingrese el valor del vehículo S/. : '))
            if valorVehiculo>0:
                break
            else:
                print('Ingrese un valor positivo')                     
        except ValueError:
            print('Error intente de nuevo.')
    if categoriaVehiculo==1:
        impuesto = valorVehiculo*0.1
        listaImpuesto1.append(impuesto)   
    elif categoriaVehiculo==2:
        impuesto = valorVehiculo*0.07
        listaImpuesto2.append(impuesto)
    elif categoriaVehiculo==3:
        impuesto = valorVehiculo*0.05
        listaImpuesto3.append(impuesto)
sumaImpuesto1 = sum(listaImpuesto1)
sumaImpuesto2 = sum(listaImpuesto2)
sumaImpuesto3 = sum(listaImpuesto3)
total = sumaImpuesto1 + sumaImpuesto2 + sumaImpuesto3
print('')
print('Categoria 1:')
for i in listaImpuesto1:
    print(f'El impuesto del vehículo {listaImpuesto1.index(i)+1} es S/. ',i,'\n')
print('Categoria 2:')
for a in listaImpuesto2:
    print(f'El impuesto del vehículo {listaImpuesto2.index(a)+1} es S/. ',a,'\n')
print('Categoria 3:')
for e in listaImpuesto3:
    print(f'El impuesto del vehículo {listaImpuesto3.index(e)+1} es S/. ',e,'\n')
print('Los impuestos de la categoria 1 son S/.',)
print('El impuesto en la categoria 1 es S/. ',sumaImpuesto1)
print('El impuesto en la categoria 2 es S/. ',sumaImpuesto2)
print('El impuesto en la categoria 3 es S/. ',sumaImpuesto3)
print('El impuesto total es S/. ',total)
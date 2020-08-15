while (True):
    try:
        Numero_1 = int(input('Ingrese el primer número: '))
        Numero_2 = int(input('Ingrese el segundo número: '))
        if Numero_1 > Numero_2:
            print('Los números ascendentemente son',Numero_2,'y',Numero_1)
        elif Numero_1 == Numero_2:
            print('Los números son iguales') 
        else:
            print('Los números ascendentemente son',Numero_1,'y',Numero_2)
        break
    except ValueError:
        print('Error. Ingrese solo números enteros.')
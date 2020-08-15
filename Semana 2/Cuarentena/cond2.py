while (True):
    try:        
        Numero_1 = int(input('Ingrese el primer número: '))
        Numero_2 = int(input('Ingrese el segundo número: '))
        Numero_3 = int(input('Ingrese el tercer número: '))
        if Numero_1 >= Numero_2 and Numero_1 >= Numero_3:
            print('El mayor número es',Numero_1)
        elif Numero_2 >= Numero_1 and Numero_2 >= Numero_3:
            print('El mayor número es',Numero_2)
        else:
            print('El mayor número es',Numero_3)
        break
    except ValueError:
        print('Error. Ingrese solo números enteros.')
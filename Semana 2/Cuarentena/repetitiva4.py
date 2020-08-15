while (True):
    try:
        Numero = int(input('Ingrese el numero: '))        
        if Numero>0:
            if Numero < 10:
                print('No es capicua')
                break 
            Numero = str(Numero)            
            if Numero==Numero[::-1]:
                print('Es capicua.')
            else:
                print('No es capicua.')
        else:
            print('Ingrese un número entero positivo.')
            continue
        break
    except ValueError:
        print('Ingrese un número entero positivo.')
        
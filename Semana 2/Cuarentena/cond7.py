while (True):
    try:        
        promedio = int(input('Ingrese su promedio: '))
        if 20 >= promedio >= 16:
            print('Usted tiene un promedio Bueno.')
        elif 16 > promedio >= 10:
            print('Usted tiene un promedio Regular.')
        elif 10 > promedio >=6:
            print('Usted tiene un promedio Deficiente.')
        elif 6 > promedio >= 0:
            print('Usted tiene un promedio Pésimo.')
        else:
            print('Ingrese su promedio desde 0 hasta 20.')
            continue
        break
    except ValueError:
        print('Error. Intente de nuevo.')
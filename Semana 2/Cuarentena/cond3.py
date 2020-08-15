while (True):
    try:
        Numero = int(input('Ingrese el número: '))
        if Numero <0:
            print('Este número es negativo.')
        elif Numero == 0:
            print('Este número es nulo.')
        else:
            print('Este número es positivo.')
        break
    except ValueError:
        print('Error. Ingrese solo números enteros.')
        
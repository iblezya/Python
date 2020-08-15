
while (True):
    try:
        Numero = int(input('Ingrese el número: '))
        if Numero == 0:
            print('Ingrese un número distinto de cero.')
            continue
        elif Numero%2 == 0:
            print('El número es par.')
        else:
            print('El número es impar.')
        break
    except ValueError:
        print('Error. Intente de nuevo')
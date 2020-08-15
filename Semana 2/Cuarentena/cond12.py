while (True):
    try:        
        N1 = int(input('Ingrese el primer número: '))
        N2 = int(input('Ingrese el segundo número: '))
        N3 = int(input('Ingrese el tercer número: '))
        N4 = int(input('Ingrese el cuarto número: '))
        N5 = int(input('Ingrese el quinto número: '))
        if N1 >= N2 and N1 >= N3 and N1 >= N4 and N1 >= N5:
            mayor = N1        
        elif N2 >= N1 and N2 >= N3 and N2 >= N4 and N2 >= N5:
            mayor = N2
        elif N3 >= N1 and N3 >= N2 and N3 >= N4 and N3 >= N5:
            mayor = N3
        elif N4 >= N1 and N4 >= N2 and N4 >= N3 and N4 >= N5:
            mayor= N4
        else:
            mayor = N5
        break
    except ValueError:
        print('Error. Intente de nuevo.')
print('El mayor numero es ',mayor)
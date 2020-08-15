while (True):
    try:        
        numero = int(input('Ingrese el numero: '))
        if numero==int(2):
                print('Este número es primo')
                break                          
        for i in range(2,numero):             
            if (numero%i)==0:
                print('Este numero no es primo')
                break
            else:
                print('Este número es primo')
                break                
        break
    except ValueError:
        print('Ingrese un número entero positivo.')

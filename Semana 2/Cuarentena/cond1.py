while (True):
    try:        
        Edad = int(input('Ingrese su edad: '))
        if Edad >= 18:
            print('Usted es mayor de edad desde hace',Edad-18,'años.')
        elif 18> Edad >=0:
            print('Usted es menor de edad le falta',18-Edad,'\naños para ser mayor de edad.')
        else:
            print('Usted ha ingresado un valor negativo.\nIngrese correctamente su edad')
            continue
        break
    except ValueError:
        print('Ingrese correctamente su edad.')


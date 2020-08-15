while (True):
    try:        
        Numero_1 = int(input('Ingrese el primer número: '))
        Numero_2 = int(input('Ingrese el segundo número: '))
        Numero_3 = int(input('Ingrese el tercer número: '))
        ListaNumeros = [Numero_1,Numero_2,Numero_3] 
        if Numero_1 >= Numero_2 and Numero_1 >=Numero_3:
            Tercero = Numero_1
            if Numero_2 >= Numero_3:
                Segundo = Numero_2
                Primero = Numero_3
            else:
                Segundo = Numero_3
                Primero = Numero_2
        else:
            if Numero_2 >= Numero_1 and Numero_2 >= Numero_3:
                Tercero = Numero_2
                if Numero_1 >= Numero_3:
                    Segundo = Numero_1
                    Primero = Numero_3
                else:
                    Segundo = Numero_3
                    Primero = Numero_1
            else:
                Tercero = Numero_3
                if Numero_2 >= Numero_1:
                    Segundo = Numero_2
                    Primero = Numero_1
                else:
                    Segundo = Numero_1
                    Primero = Numero_2
        print('Los números ordenados ascendentemen son:')
        print(Primero,Segundo,Tercero)
        print('El orden ingresado es:')
        print(ListaNumeros)
        break
    except ValueError:
        print('Error. Ingrese solo números enteros.')
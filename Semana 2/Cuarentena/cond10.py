print('Pograma social familiar. Indique cuantos hijos tiene.')
print("1.De 1 hasta 2 hijos.")
print("2.De 3 hasta 5 hijos.")
print("3.De 6 o más hijos.")
print("**"*18)     
while (True):
    try:
        Opcion = int(input("Ingrese la opcion(Del 1 al 3): "))            
        if Opcion ==1:
            NumeroHijos = int(input('Ingrese el número de hijos: '))
            NumeroHijosEscolares = int(input('Ingrese el número de hijos entre la edad de 6 y 18 años: '))
            Subsidio = 70 + 10*NumeroHijosEscolares
        elif Opcion ==2:
            NumeroHijos = int(input('Ingrese el número de hijos: '))
            NumeroHijosEscolares = int(input('Ingrese el número de hijos entre la edad de 6 y 18 años: '))
            Subsidio = 90 + 10*NumeroHijosEscolares
        elif Opcion==3:
            NumeroHijos = int(input('Ingrese el número de hijos: '))
            NumeroHijosEscolares = int(input('Ingrese el número de hijos entre la edad de 6 y 18 años: '))
            Subsidio = 120 + 10*NumeroHijosEscolares         
        else:
            print("Ingrese una opcion valida.")
            continue
        print('**'*18)
        break
    except ValueError:
        print("Error. Intente de nuevo.")
print('Si en la familia la madre es viuda. Confirme.')
print("1.Si")
print("2.No")
print("**"*18)
while (True):
    try:
        Opcion = int(input("Ingrese la opcion: "))            
        if Opcion ==1:
            Subsidio = Subsidio + 80
        elif Opcion ==2:
            Subsidio = Subsidio + 0          
        else:
            print("Ingrese una opcion valida.")
            continue
        print('**'*18)
        break
    except ValueError:
        print("Error. Intente de nuevo.")
print('La familia recibe un subsidio por el programa social de  S/. ',Subsidio)
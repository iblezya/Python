SueldoBase = 850   
print('Determine su grado de instrucción.')
print("1.Hasta 5to de secundaria")
print("2.Técnico")
print("3.Profesional")
print("**"*18)     
while (True):
    try:
        Opcion = int(input("Ingrese la opcion(Del 1 al 3): "))            
        if Opcion ==1:
            IncrementoEstudios = 0.05
        elif Opcion ==2:
            IncrementoEstudios = 0.1
        elif Opcion==3:
            IncrementoEstudios = 0.2            
        else:
            print("Ingrese una opcion valida.")
            continue
        print('**'*18)
        break
    except ValueError:
        print("Error. Intente de nuevo.")
print('Determine su condición social.')
print("1.Casado")
print("2.Casado")
print("3.Cuantos hijos tiene")
print("4.Sin vivienda")
print("**"*18)
while (True):
    try:
        Opcion = int(input("Ingrese la opcion(Del 1 al 3): "))            
        if Opcion ==1:
            IncrementoCSocial = 0.03
        elif Opcion ==2:
            IncrementoCSocial = 0
        elif Opcion==3:
            while (True):
                try:
                    NumHijos = int(input('Ingrese cuantos hijos tiene:'))
                    if NumHijos>=0:
                        IncrementoCSocial = 0.02*NumHijos
                        break
                    else:
                        print('Error. Intente de nuevo')
                        continue
                except ValueError:
                    print('Error.Ingrese la cantidad de hijos.')
        elif Opcion==4:
            IncrementoCSocial = 0.05                 
        else:
            print("Ingrese una opcion valida.")
            continue
        print('**'*18)
        break
    except ValueError:
        print("Error. Intente de nuevo.")
SueldoNeto = SueldoBase*(1+(IncrementoEstudios+IncrementoCSocial))
print(f'El sueldo neto del trabajador es S/. {(SueldoNeto):.2f}')
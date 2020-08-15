from math import pi
from math import factorial
print('Este programa calcula el seno de un ángulo.')
print('1. Ángulo en grados.\n2. Ángulo en radianes.\nSeleccione una opción:\n'+'*'*35)
while (True):
    try:
        opcion = int(input('Ingrese la opción : '))
        if opcion==1:
            while (True):
                try:
                    gradossexagesi = float(input('Ingrese el ángulo (°): '))
                    n=0
                    seno=0
                    x = (gradossexagesi*pi)/180
                    while n<20:
                        n=n+1
                        sumatoria = float((x**(2*n-1))*((-1)**(n+1))/factorial(2*n-1))
                        seno = seno + sumatoria
                    senofinal = round(seno,3)                    
                    break                     
                except ValueError:
                    print('Error. Intente de nuevo.')
            break                    
        elif opcion==2:
            while (True):
                try:
                    radianes = float(input('Ingrese el ángulo (rad): '))
                    n=0
                    seno=0
                    x = radianes
                    while n<20:
                        n=n+1
                        sumatoria = float((x**(2*n-1))*((-1)**(n+1))/factorial(2*n-1))
                        seno = seno + sumatoria
                    senofinal = round(seno,3)                    
                    break
                except ValueError:
                    print('Error. Intente de nuevo.')
            break
        else:
            print('Ingrese una opción valida.')
    except ValueError:
        print('Error. Intente de nuevo.')
print('El seno del ángulo es:', senofinal)
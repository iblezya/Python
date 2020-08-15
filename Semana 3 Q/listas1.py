import math
while (True):
    try:
        cantidadNumeros = int(input('Ingrese cuantos números desear imprimir: '))
        while cantidadNumeros<0:
            print("Ingrese una cantidad mayor o igual a 1.")
            cantidadNumeros = int(input('Ingrese cuantos números desear imprimir: '))
            break
        numerosLista = []
        for i in range(1,(cantidadNumeros +1)):    
            while (True):        
                try:
                    numeros = int(input(f"Ingrese su número {i}: "))  
                    if numeros>=0:
                        numerosLista.append(numeros)  
                        break
                    else:
                        print('Error intente de nuevo.')                          
                except ValueError:
                    print('Error intente de nuevo.')
        break                        
    except ValueError:
        print('Error intente de nuevo.')
print(numerosLista)   



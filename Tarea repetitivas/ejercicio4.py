print('Este programa cálcula el cubo de n números.')
print('*'*30)
while (True):
    try:
        n_numeros = int(input('Ingrese la cantidad de números a ingresar: '))
        break
    except ValueError:
        print('Error intente de nuevo.')
n_lista = []
for i in range(1,(n_numeros+1)):    
    while (True):        
        try:
            numeros = int(input(f"Ingrese su número {i}: "))  
            if numeros>0:
                n_lista.append(numeros)  
                break
            else:
                print('Error intente de nuevo.')       
        except ValueError:
            print('Error intente de nuevo.')  
print('')
for i in n_lista:
    print("El cubo de",i,'es',i**3)

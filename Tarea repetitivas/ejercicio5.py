print('Este programa imprime la tabla de multiplicar de un entero K comenzando desde el 1.')
print('*'*35)
while (True):
    try:
        k = int(input('Ingrese el número: '))
        n=0
        while n<13:
            n+=1
            print(n,' x ',k," = ",(n*k))
        break        
    except ValueError:
        print('Error intente de nuevo.')

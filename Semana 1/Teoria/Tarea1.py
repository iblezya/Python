print('*'*30)
print('Este programa cálcula el promedio de 6 notas como máximo.')
print('*'*30)
i = 1
def Promedios():
    NumeroNotas = 0
    while (True):
        try:
            NumeroNotas = int(input('Ingrese el número de notas: '))
            while NumeroNotas>6 or NumeroNotas<2:
                print('Para calcular su promedio debe ingresar\nun mínimo de 2 notas y un máximo de 6.')
                NumeroNotas = int(input('Ingrese el número de notas: '))    
            break
        except ValueError:
            print('Error intente de nuevo.')
    NotasLista = []
    for i in range(1,(NumeroNotas+1)):    
        while (True):        
            try:
                Notas = float(input(f"Ingrese su nota {i}: "))  
                if Notas>=0 and Notas<=20:
                    NotasLista.append(Notas)  
                    break
                else:
                    print('Error intente de nuevo.')       
            except ValueError:
                print('Error intente de nuevo.')  
    print('')
    Prom = sum(NotasLista)/(NumeroNotas)
    print(f"Su promedio es {(Prom):.2f}")
while i<=1:
    Promedios()
    print('*'*30)

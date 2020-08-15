print('*'*38+'\nEste programa determina cuantos dígitos son pares, impares')
print('y cuantos hay en total para un número entre 0 a 32500')
print('*'*38)
while (True):
    try:
        Numero = int(input('Ingrese el número: '))
        if 0<Numero<32500:
            break
        else:
            print('Ingrese un numero mayor que 0 y menor que 32500')
            continue
    except ValueError:
        print('Error. Ingrese un número.')
Numero = str(Numero)
NumeroDigitos = len(Numero)
par=0

for d in Numero:
    if int(d)%2 ==0:
        par+=1
print('\nNúmero de dígitos totales: ',NumeroDigitos)
print('Número de dígitos pares: ',par)
print('Número de dígitos impares: ',int(NumeroDigitos)-par)
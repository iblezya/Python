print('Este programa cálcula la inversión final de un capital de $1500 al 15 % anual.')
print('El año inicial es 1961.')
while (True):
    try:
        anho = int(input('Ingrese el año final :'))
        n=1961
        inversion = 1500
        if anho>1961:
            while n<anho:    
                inversion= inversion*(1+0.15)
                n = n +1
            break
        else:
            print('Ingrese un año mayor a 1961.')
    except ValueError:
        print('Error intente de nuevo.')
inversion = round(inversion,2)
print('La inversión final asciende a S/. ',inversion)

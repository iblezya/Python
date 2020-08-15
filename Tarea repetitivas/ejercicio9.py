print('Este programa determina  qué  cantidad  de  dinero  hay  en  un  monedero,')
print('considerando  que  se  tienen  monedas  de cinco, dosy  un sol,  y  billetes  ')
print('de  diez,  veinte  y cincuenta soles.')
print('*'*35)
#while (True):
    #try:
dinero = []
# M O N E D A S
while (True):
    try:
        monedas1sol = int(input('Ingrese cuantas monedas de 1 sol tiene: '))
        while monedas1sol < 0:
            print('Ingrese un valor mayor o igual a 0.')
            monedas1sol = int(input('Ingrese cuantas monedas de 1 sol tiene: '))
        break
    except ValueError:
        print('Error. Intente de nuevo.')
dinero.append(monedas1sol)
while (True):
    try:
        monedas2sol = int(input('Ingrese cuantas monedas de 2 soles tiene: '))
        while monedas2sol < 0:
            print('Ingrese un valor mayor o igual a 0.')
            monedas2sol = int(input('Ingrese cuantas monedas de 2 soles tiene: '))
        break
    except ValueError:
        print('Error. Intente de nuevo.')
dinero.append(monedas2sol*2)
while (True):
    try:
        monedas5sol = int(input('Ingrese cuantas monedas de 5 soles tiene: '))
        while monedas5sol < 0:
            print('Ingrese un valor mayor o igual a 0.')
            monedas5sol = int(input('Ingrese cuantas monedas de 5 soles tiene: '))
        break
    except ValueError:
        print('Error. Intente de nuevo.')
dinero.append(monedas5sol*5)
# B I L L E T E S
while (True):
    try:
        billete10sol = int(input('Ingrese cuantos billetes de 10 sol tiene: '))
        while billete10sol < 0:
            print('Ingrese un valor mayor o igual a 0.')
            billete10sol = int(input('Ingrese cuantos billetes de 10 sol tiene: '))
        break
    except ValueError:
        print('Error. Intente de nuevo.')
dinero.append(billete10sol*10)
while (True):
    try:
        billete20sol = int(input('Ingrese cuantos billetes de 20 sol tiene: '))
        while billete20sol < 0:
            print('Ingrese un valor mayor o igual a 0.')
            billete20sol = int(input('Ingrese cuantos billetes de 20 sol tiene: '))
        break
    except ValueError:
        print('Error. Intente de nuevo.')
dinero.append(billete20sol*20)
while (True):
    try:
        billete50sol = int(input('Ingrese cuantos billetes de 50 sol tiene: '))
        while billete50sol < 0:
            print('Ingrese un valor mayor o igual a 0.')
            billete50sol = int(input('Ingrese cuantos billetes de 50 sol tiene: '))
        break
    except ValueError:
        print('Error. Intente de nuevo.')
dinero.append(billete50sol*50)
#print(dinero)
d = sum(dinero)
print('Usted tiene S/. ',d)

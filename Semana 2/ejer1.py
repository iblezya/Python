while (True):
    user = input('Ingrese su codigo: ')
    password = input('Ingrese su contraseña: ')
    if user == '1' and password == '1234':
        print('Welcome.')
        break
    else:
        print('Ingrese de nuevo.')

print('Este programa lee las calificaciones de N alumnos y determina el número de aprobados y desaprobados.')
print('*'*30)
while (True):
    try:
        n_alumnos = int(input('Ingrese la cantidad de alumnos: '))
        while n_alumnos<0:
            print('Ingrese como mínimo 1 alumno.')
            n_alumnos = int(input('Ingrese la cantidad de alumnos: '))
        break
    except ValueError:
        print('Error intente de nuevo.')
alumnos = {}
for i in range(1,(n_alumnos+1)):    
    while (True):        
        try:
            nombre = str(input(f"Ingrese el nombre del alumno {i}: "))
            break
        except ValueError:
            print('Error intente de nuevo.')
    while (True):
        try:  
            nota = int(input('Ingrese su nota: '))
            if nota>=0 and nota<=20:                
                break
            else:
                print('Error intente de nuevo.')                     
        except ValueError:
            print('Error intente de nuevo.')
    alumnos[nombre] = nota  
print('')
aprobados = 0
desaprobados = 0
for nta in alumnos:
    if alumnos[nta]>10:
        aprobados += 1
    else:
        desaprobados += 1
print('El número de aprobados es ',aprobados)
print('El número de desaprobados es ',desaprobados)

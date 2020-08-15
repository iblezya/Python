print('Este programa determina el sueldo semanal con descuentos de N trabajadores considerando sus ganancias.')
print('*'*30)
while (True):
    try:
        n_trabajadores = int(input('Ingrese la cantidad de trabajadores: '))
        while n_trabajadores<0:
            print('Ingrese como mínimo 1 alumno.')
            n_trabajadores = int(input('Ingrese la cantidad de trabajadores: '))
        break
    except ValueError:
        print('Error intente de nuevo.')
dicTrabajador = {}
for i in range(1,(n_trabajadores+1)):    
    while (True):        
        try:
            nombre = str(input(f"Ingrese el nombre del trabajador {i}: "))
            break
        except ValueError:
            print('Error intente de nuevo.')
    while (True):
        try:  
            sueldo = int(input('Ingrese su sueldo S/. : '))
            if sueldo>0 and sueldo<=150:
                sueldo = sueldo*0.95                
                break
            elif sueldo>150 and sueldo<=300:
                sueldo = sueldo*0.93  
                break
            elif sueldo>300 and sueldo<=450:
                sueldo = sueldo*0.91  
                break
            else:
                print('Debe ingresar un valor de 0 hasta 450')                     
        except ValueError:
            print('Error intente de nuevo.')
    dicTrabajador[nombre] = sueldo  
print('')
for trabj, sueld in dicTrabajador.items():
    print(f"El trabajador {trabj} gana semanalmente S/. {sueld}")

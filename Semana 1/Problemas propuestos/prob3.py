i = 1
def Prob3():    
    print('*'*35)
    TarifaHoraria = 0
    while (True):
        try:        
            TarifaHoraria = float(input('Ingrese su tarifa horaria (S/.): '))
            while TarifaHoraria<=0:
                print('Tiene que ingresar un valor positivo.')
                TarifaHoraria = float(input('Ingrese su tarifa horaria (S/.): '))
            break
        except ValueError:
            print("¡Error! Ingrese correctamente los datos.")
    HorasTrabajo = 0
    while (True):
        try:        
            HorasTrabajo = int(input('Ingrese las horas trabajadas: '))
            while HorasTrabajo<=0:
                print('Tiene que ingresar un valor positivo.')
                HorasTrabajo = int(input('Ingrese las horas trabajadas: '))
            break
        except ValueError:
            print("¡Error! Ingrese correctamente los datos.")
    print('*'*35)
    SueldoBruto = HorasTrabajo*TarifaHoraria
    if SueldoBruto>3500:
        Descuento = 0.15*SueldoBruto
        SueldoNeto = SueldoBruto - Descuento
    else:
        Descuento = 0.11*SueldoBruto
        SueldoNeto = SueldoBruto - Descuento    
    print(f'El sueldo bruto es S/. {(SueldoBruto):.2f} .'+
        f"\nEl descuento es S/. {(Descuento):.2f} ."+
        f"\nEl sueldo neto es S/. {(SueldoNeto):.2f} .")
while i<=1:
    Prob3()
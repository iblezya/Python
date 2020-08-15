while (True):
    try:
        n_clientes = int(input('Ingrese la cantidad de clientes: '))
        while n_clientes<0:
            print('Ingrese como mínimo 1 cliente.')
            n_clientes = int(input('Ingrese la cantidad de clientes: '))
        break
    except ValueError:
        print('Error intente de nuevo.')
listaInteres=[]
dictCliente = {}
for i in range(1,(n_clientes+1)):
    while (True):        
        try:
            nombre = str(input(f"Ingrese el nombre del cliente {i}: "))
            break
        except ValueError:
            print('Error intente de nuevo.')
    while (True):
        try:
            saldoAnterior = float(input('Ingrese su saldo anterior de deuda S/. : '))
            if saldoAnterior==0:
                while (True):
                    try:
                        montoCompras = float(input('Ingrese el monto de compras S/. : '))
                        while montoCompras<0:
                            print('Ingrese un monto mayor a 0.')
                            montoCompras = float(input('Ingrese el monto de compras S/. : '))                        
                        break                                            
                    except ValueError:
                        print('Error intente de nuevo.')
                saldoActual = montoCompras
                pagoMinimo = 0.15*saldoActual
                pagoNoInteres = 0.85*saldoActual
                interes = 0
                break            
            elif saldoAnterior>0:
                while (True):
                    try:
                        montoCompras = float(input('Ingrese el monto de compras S/. : '))                    
                        while montoCompras<0:
                            print('Ingrese un monto mayor a 0.')
                            montoCompras = float(input('Ingrese el monto de compras S/. : '))                        
                        break                                            
                    except ValueError:
                        print('Error intente de nuevo.')
                pagoMinimoAnterior = 0.15*saldoAnterior
                pagoNoInteresAnterior = 0.85*saldoAnterior
                interes = 0.12*saldoAnterior
                multa = 200
                while (True):
                    try:
                        pagoDepositoAnterior = float(input('Ingrese el pago que depositó en el corte anterior S/. : '))
                        if pagoDepositoAnterior>=pagoMinimoAnterior and pagoDepositoAnterior<pagoNoInteresAnterior:
                            saldoActual = saldoAnterior - pagoDepositoAnterior + interes + montoCompras
                            pagoMinimo = 0.15*saldoActual
                            pagoNoInteres = 0.85*saldoActual
                            break
                        elif pagoDepositoAnterior>=0 and pagoDepositoAnterior<pagoMinimoAnterior:    
                            saldoActual = saldoAnterior - pagoDepositoAnterior + interes + 200 + montoCompras
                            pagoMinimo = 0.15*saldoActual
                            pagoNoInteres = 0.85*saldoActual
                            break
                        elif pagoDepositoAnterior>=0.85*saldoAnterior and pagoDepositoAnterior<=saldoAnterior:
                            saldoActual = saldoAnterior - pagoDepositoAnterior + montoCompras
                            pagoMinimo = 0.15*saldoActual
                            pagoNoInteres = 0.85*saldoActual
                            break
                        else:
                            print('Ingrese un su pago entre 0 y el saldo anterior.')
                    except ValueError:
                        print('Error intente de nuevo.')
                break
            else:
                print('Ingrese un valor mayor o igual a 0.')
        except ValueError:
            print('Error intente de nuevo.')
    listaInteres.append(interes)
    listaCliente = [saldoActual,pagoMinimo,pagoNoInteres]
    dictCliente[nombre] = listaCliente
sumatoriaInteres= sum(listaInteres)
for nom, lsta in dictCliente.items():
    print('El cliente '+nom+' registra:')
    print('Un saldo actual de S/. ',lsta[0])
    print('Un pago mínimo de S/. ',lsta[1])
    print('Un pago para no generar intereses de S/. ',lsta[2])
print('El monto ganado por interes de los clientes morosos es S/. ',sumatoriaInteres) 
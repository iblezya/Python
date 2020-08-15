while (True):
    try:
        NumeroVotasA = int(input('Ingrese el número de votos del candidato A: '))
        NumeroVotasB = int(input('Ingrese el número de votos del candidato B: '))
        NumeroVotosNulos = int(input('Ingrese el número de votos nulos: '))
        TotalVotos = NumeroVotasA + NumeroVotasB
        if (NumeroVotasA +NumeroVotasB + NumeroVotosNulos)==500:            
            if (NumeroVotasA/TotalVotos)>0.5:
                print('El candidato A es el ganador.')
                break
            elif (NumeroVotasB/TotalVotos)>0.5:
                print('El candidato B es el ganador.')
                break
            else:
                print('<<HABRA SEGUNDA VUELTA>>.')
                continue
        else:
            print('Debe ingresar los 500 votos porfavor.')
            continue
    except ValueError:
        print('Error.Ingrese de nuevo.')

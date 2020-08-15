#Crear una calculadora
def suma():
    a = float(input("Ingrese el primer numero: \n"))
    b = float(input("Ingrese el primer numero: \n"))   
    x=a+b
    print("Resultado: ",x)
def resta():
    a = float(input("Ingrese el primer numero: \n"))
    b = float(input("Ingrese el primer numero: \n"))
    x=a-b
    print("Resultado: ",x)
def multiplicador():
    a = float(input("Ingrese el primer numero: \n"))
    b = float(input("Ingrese el primer numero: \n"))

    x=a*b
    print("Resultado: ",x)
def dividir():
    a = float(input("Ingrese el primer numero: \n"))
    b = float(input("Ingrese el primer numero: \n"))
    x=a/b
    print("Resultado: ",x)
def menu():
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("**"*18)    
    while (True):
        try:
            Opcion = int(input("Ingrese la opcion: "))
            
            if Opcion ==1:
                suma()
            elif Opcion ==2:
                resta()
            elif Opcion==3:
                multiplicador()
            elif Opcion==4:
                dividir()
            else:
                print("Ingrese una opcion valida.")
        except ValueError:
            print("Ingrese de nuevo.")
menu()


def dia(argument):
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miercoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sabado",
        7: "Domingo",
    }
    print(dias.get(argument, "Entrada invalida."))
i=1
while i<=1:
    Num = int(input("Ingrese el número: "))
    dia(Num)
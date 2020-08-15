def mes(argument):
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    print(meses.get(argument, "Entrada invalida."))
i=1
while i<=1:
    Num = int(input("Ingrese el número: "))
    mes(Num)
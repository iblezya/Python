apellidos = str(input("Ingrese sus apellidos: "))
nombres = str(input("Ingrese sus apellidos: "))
cantHorasTrabj = int(input("Ingresar las horas trabajadas: "))
while cantHorasTrabj<=0:
    cantHorasTrabj = int(input("Ingrese un valor mayor a 0.\nIngresar las horas trabajadas: "))
valorHora = float(input("Ingresar el valor de hora trabajada: "))
while valorHora<=0:
    valorHora = float(input("Ingrese un valor mayor a 0.\nIngresar el valor de hora trabajada: "))
sueldoBruto=cantHorasTrabj*valorHora
descuentoSNP=0.13*sueldoBruto
bonificacion=0.07*sueldoBruto
sueldoNeto=sueldoBruto-descuentoSNP+bonificacion
print("Trabajador "+apellidos.upper()+" "+nombres.upper())
print("Sueldo bruto: S/. ",round(sueldoBruto,2))
print("Descuentos por ley de aporte al SNP: S/. ",round(descuentoSNP,2))
print("Bonificación familiar: S/. ",round(bonificacion,2))
print("Sueldo neto: S/. ",round(sueldoNeto,2))
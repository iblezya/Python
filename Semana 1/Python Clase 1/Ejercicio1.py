print("Buenos días este programa calculara su promedio de calificaciones")
nombre = str(input("Ingrese su nombre: "))
nota_1 = float(input("Ingrese su primera nota: "))
nota_2 = float(input("Ingrese su segunda nota: "))
nota_3 = float(input("Ingrese su tercera nota: "))
nota_4 = float(input("Ingrese su cuarta nota: "))
promedio = (nota_1 + nota_2 + nota_3 + nota_4)/4
print (nombre)
print ("Su calificación es: ",promedio)
if promedio>=10.5:
    print("Usted esta aprobado.")
else:
    print("Usted esta desaprobado.")

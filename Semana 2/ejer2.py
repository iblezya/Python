Entrada = str(input("Ingrese su palabra: "))
Contador = 0
for car in Entrada:
    if car == "a":
        Contador = Contador + 1
print("Las vocales a contadas son ",Contador)
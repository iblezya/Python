print("="*50)
personas = int(input("Ingrese el número de personas: "))
tipo_autobus = str(input("Ingrese el tipo de autobus (A, B o C): "))
print("="*50)
if tipo_autobus==str("A"):
    c = 2
elif tipo_autobus==str("B"):
    c = 2.5
elif tipo_autobus==str("C"):
    c = 3    
if personas < 20:
    costo_total = c*20
    print("El precio por kilómetro es $ ",c)
    print(" $ ",costo_total)
    print("="*50)
else:
    costo_total = c*personas
    print("El precio por kilómetro es $ ",c)
    print("El costo total es $ ",costo_total)
    print("="*50)
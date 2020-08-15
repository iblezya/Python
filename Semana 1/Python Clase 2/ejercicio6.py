print("="*50)
num_personas = int(input("Ingrese el número de personas: "))
if num_personas>300:
    print("="*50)
    p = 75
    print("El precio por platillo es S/. ",p)
    presu = num_personas*p
    print("El presupuesto del banquete es S/. ",presu)
elif 300>=num_personas and num_personas>200:
    print("="*50)
    p = 85
    print("El precio por platillo es S/. ",p)
    presu = num_personas*p
    print("El presupuesto del banquete es S/. ",presu)
else:
    print("="*50)
    p = 95
    print("El precio por platillo es S/. ",p)
    presu = num_personas*p
    print("El presupuesto del banquete es S/. ",presu)
print("="*50)
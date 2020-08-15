print("="*50)
a = float(input("Ingrese el primer valor: "))
b = float(input("Ingrese el segundo valor: "))
c = float(input("Ingrese el tercer valor: "))
print("="*50)
if a>b and a>c:
    print("El mayor valor es: ",a)
elif b>a and b>c:
    print("El mayor valor es: ",b)
else:
    print("El mayor valor es: ",c)
print("="*50)
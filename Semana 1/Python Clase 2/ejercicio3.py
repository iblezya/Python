print("="*50)
cant_lapiceros = int(input("Ingrese la cantidad de lapiceros: "))
if cant_lapiceros>=1000:
    print("="*50)
    p1 = 0.85*cant_lapiceros
    print("Por la compra de ",cant_lapiceros,
          " lapiceros se debe pagar S/. ",p1)
else:
    print("="*50)
    p2 = 0.9*cant_lapiceros
    print("Por la compra de ",cant_lapiceros,
          " lapiceros se debe pagar S/. ",p2)
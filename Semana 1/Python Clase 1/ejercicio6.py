print("="*50)
prod = float(input("Ingrese los la producción de leche en litros: "))
val = float(input("Ingrese el valor de cada galón de leche(S/.): "))
transf = prod/3.785
precio = val*transf
print("="*50)
print("El productor producio ",transf," galones de leche.")
print("El productor recibira por la entrega: S/. ",precio)
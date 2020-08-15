print("="*50)
import math
radio = float(input("Ingrese el radio de la figura(m): "))
hipo = float(input("Ingrese la hipotenusa de la figura(m): "))
area = (radio*radio*math.pi/2)+2*(radio*(math.sqrt(hipo*hipo-radio*radio))/2)
print("="*50)
print("El área de la figura es: ",area," m2")
#Arrays
#Son grupos de variables almacenados en una sola linea de codigo.
#Tambien se consume espacios de memoria que se puede acceder por un indice.

v = [1,2,3,4,5,6,7,8,9,0]
#for i in v:
    #print(i,"",end="")
v.append(99)
for i in range(len(v)):
    print(v[i]," ",end="")
v.insert(0,985)
print("\n")
print(v)
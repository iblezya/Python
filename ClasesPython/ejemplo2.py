class persona:
    def __init__(self,n,e,i):
        self.nombre=n
        self.edad=e
        self.instituto=i

    def mostrar_nombre(self):
        print(self.nombre)
    
    def mostrar_edad(self):
        print(self.edad)
    
    def mostrar_instituto(self):
        print(self.instituto)

rufian = persona('Lucho Toribui','18 años','Senati Independencia')
rufian.mostrar_nombre()
rufian.mostrar_edad()
rufian.mostrar_instituto()
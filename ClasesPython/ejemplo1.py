#POO

class persona:
    nombre = ''
    instituto = ''
    def mostrar_informacion(self,nombre,instituto):
        print(self.nombre)
        print(self.instituto)

anita=persona()
anita.nombre="Ana"
anita.instituto='Senati'
anita.mostrar_informacion(anita.nombre,anita.instituto)
class Figura:
    def __init__(self,nombre:str) -> None:
        self.nombre=nombre
        
    def mostrar_nombre(self):
        print(f'El nombre de la figura es :{self.nombre}')
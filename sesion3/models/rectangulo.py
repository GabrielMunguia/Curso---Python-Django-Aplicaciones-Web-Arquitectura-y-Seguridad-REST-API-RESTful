from models.figura import Figura
class Rectangulo(Figura):
    def __init__(self, nombre: str,base:float,altura:float) -> None:
        super().__init__(nombre)
        self.base=base
        self.altura=altura
    
    def calcular_area(self)->float:
        return self.base*self.altura
    
    def calcular_perimetro(self)->float:
        return 2*(self.base+self.altura)
        
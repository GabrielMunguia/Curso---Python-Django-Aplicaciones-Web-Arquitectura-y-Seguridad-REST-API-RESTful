import math
from models.figura import Figura
class Circulo(Figura):
    def __init__(self, nombre: str,radio:float) -> None:
        super().__init__(nombre)
        self.radio=radio
    
    def calcular_area(self)->float:
        return math.pi*self.radio**2
    
    def calcular_perimetro(self)->float:
        return 2*math.pi*self.radio
   
    
    
        
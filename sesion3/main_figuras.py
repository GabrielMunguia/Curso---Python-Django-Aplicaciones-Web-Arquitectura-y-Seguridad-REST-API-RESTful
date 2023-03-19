from models.rectangulo import Rectangulo
from models.circulo import Circulo


rect=Rectangulo('Rectangulo1',2,2)
circulo= Circulo('Circulo 1',30)
print(f'El area es : {rect.calcular_area()}') 
print(f'El perimetro es : {rect.calcular_perimetro()}')
print(f'El area es : {circulo.calcular_area()}')

class Persona:
    def __init__(self, nombre, apellido, dui, edad):
        self.nombre = nombre # atributo publico
        self._apellido = apellido # protegido
        self.__dui = dui # privado
        self.__edad = edad # privado

    def __es_adulto(self):
        return self.__edad>=18
    
    def mostrar_datos(self):
        print(
            f'Nombre: {self.nombre}\n'
            f'Apellido: {self._apellido}\n'
            f'Edad: {self.__edad}, {self.__es_adulto()}\n'
            f'DUI: {self.__dui}\n'
            )
    
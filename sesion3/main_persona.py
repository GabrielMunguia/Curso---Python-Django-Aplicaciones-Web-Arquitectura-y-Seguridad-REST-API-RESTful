from models.persona import Persona

gabriel = Persona('Gabriel', 'Munguia', '12345678-9', 20)

#Atributos publicos
print(f'Nombre: {gabriel.nombre}')
#Atributos protegidos
print(f'Apellido: {gabriel._apellido}')
#Atributos privados
print(f'Edad: {gabriel._Persona__edad}')

#Metodos privados
print(f'Es adulto: {gabriel._Persona__es_adulto()}')

#Metodos publicos
gabriel.mostrar_datos()
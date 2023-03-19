# programa para uso de sets

clientes = {'alicia','beto','carlos','diana'}
print(len(clientes))
# son DESordenados
print(clientes)
# No tienen acceso indexado
# print(clientes[1])
# NO soporta asignacion
# clientes[1] = 'eva'
# son dinamicos
clientes.add('eva')
clientes.add('eva')
print(clientes)
clientes.discard('beto')
print(clientes)

for cliente in clientes:
    print('cliente: ', cliente)

lista = {9,1,5,1,7,1,3}
conjunto = set(lista)
print(conjunto)
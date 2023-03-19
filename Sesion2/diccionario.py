# nombre: alicia
usuario = {
    'usuario': None,
    'correo': 'alicia@gmail.com',
    'token': 'sshfgjsdfgyweurtwvnzcvnzxbcahgwy',
}
print(usuario['usuario'])
print(usuario['correo'])
print(usuario['token'])
# elementos modificables
usuario['usuario'] = 'alicia123'
print('usuario modificado:',usuario['usuario'])
# agregar elementos
usuario['telefono'] = '123456789'
print(usuario)
# eliminar elementos
usuario.pop('token')
print(usuario)
# recorrido
for valor in usuario.values():
    print(f'valor: {valor}')
for llave in usuario.keys():
    print(f'llave: {llave}')
for k,v in usuario.items():
    print(f'k: {k}, v: {v}')
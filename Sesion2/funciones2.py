# paso por valor
x = 5
def modificar_variable(x):
    x+=2
    return x

z = modificar_variable(x)
print(z)
print(x)

# paso por referencia
v = [2,8,1,5]
def modificar_vector(w):
    w.append(9)
    return w

t = modificar_vector(v)
print(t)
print(v)


def coordenadas():
    return (1, 2)

# Si quiero definir tupla con un solo valor debería ir (1,)
my_tuple = (1,)
my_other_tuple = (2, 3, 4)

# Aqui sumarémos o reasignaremos a my_tuple para que queden dos tuplas unificadas
my_tuple += my_other_tuple

# También podemos asignar los valores a letras
w, x, y, z = my_tuple
print(z)

# imprimiendo la function con 2 valores
print(coordenadas())
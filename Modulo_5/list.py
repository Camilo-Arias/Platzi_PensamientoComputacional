# Definiendo mi lista
my_list = [0, 1, 2, 3]
# imprimiendo mi lista desde un indice hasta el final
# print(my_list[1:])

# Apuntando al mismo segmento de almacenamiento
b = my_list
# Clonando la lista b y apuntando a otro segmento, otra manera de clonar sería a[::]
c = list(b)

# Añadiendo valor al final de nuestra lista con el metodo append
b.append(1)

# print(b)
# print(c)

# 
# LIST COMPREHENSION
# 
my_list_1 = list(range(100))

# doblando los valores de mi list_1
double = [i * 2 for i in my_list_1]
# print(double)

impares = [i for i in my_list_1 if i % 2 != 0]
# print(impares)

#######################################################################################################
# Definiendo 1 lista y 1 tupla, y la lista extenderá los valores de la tupla
list_extend = [1, 2, 3]
tupla_1 = ('a', 'b', 'c')

# Extendiendo tupla a list.
list_extend.extend(tupla_1)
# print(list_extend)
# ### index recibirá 3 parametros, el valor a buscar, posición inicial y posición final. 
# print(list_extend.index('c', 0, len(list_extend)))
# print(list_extend.index('c'))

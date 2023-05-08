# Crear un bucle que cuente todos los números pares hasta el 100

# METODO 1
# Definiendo sum como entero 
sum1 = 0

# Recorriendo numeros desde el 0 hasta el 100 con pasos de 2 (0,2,4,6,8, n)
for i in range(0, 101, 2):
    # sumando todos los i que serán números pares
    sum1 += i
# imprimiendo sum
print(f'Resultado metodo 1: {sum1}')
# METODO 2
sum2 = 0
# recorriendo numeros de 0 a 100, el paso de 1 se infiere dentro del range
for i in range(0, 101):
    # se divide i en 2 y si el modulo es 0 será un número par
    if i % 2 == 0:
        sum2 += i

# imprimiendo sum
print(f'Resultado metodo 2: {sum2}')
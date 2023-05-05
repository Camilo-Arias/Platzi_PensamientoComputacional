table = int(input('Inserte el número para imprimir su tabla de multiplicar: '))

# Irá de 1 hasta 10 con pasos de 1
for i in range(1, 11, 1):
    multi = i * table
    print(f'{i} * {table} = {multi}')
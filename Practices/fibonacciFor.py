# Mostrar series de Fibonacci hasta 10 términos

# Se puede usar recursividad, si se quiere ver el codigo revisarlo en el Modulo 4 en fibonacci.py

a = 0
b = 1
for i in range (0, 11, 1):
    if i < 2:
        print(i)
    else:
        # Ejemplo: 0 , 1 = c 1
        # c = 0+1   a = 1    b = 1
        # c = 1+1   a = 1    b = 2
        c = b + a
        a = b
        b = c
        print(c)
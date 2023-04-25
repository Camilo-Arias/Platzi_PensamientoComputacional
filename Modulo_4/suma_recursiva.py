def suma_recursiva(n):
    """Suma todos los números en secuencia hasta n 
    n int > 0 límite de suma

    returns sum
    """
    
    if n == 0:
        return 0
    return n + suma_recursiva(n - 1)

n = int(input('Introduce un entero: '))

print(suma_recursiva(n))
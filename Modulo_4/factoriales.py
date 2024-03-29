def factorial(n):
    """Calcula el factorial de n

    n int > 0
    returns n!
    
    """
    # Condicional de n = 1 para evitar infinity loop
    if n == 1:
        return 1
    # Creando recursividad en cada llamado.
    return n * factorial(n - 1)

n = int(input('Escribe un entero: '))

print(factorial(n))
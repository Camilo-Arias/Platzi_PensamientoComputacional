def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    
    print(f'aqui: {fibonacci(n - 1) + fibonacci(n - 2)}')
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
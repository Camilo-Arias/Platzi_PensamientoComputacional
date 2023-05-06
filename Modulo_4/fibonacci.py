def fibonacci(n):
    if n < 2:
        return 1
    # Verificar funcionamiento del return
    # print(f'aqui: {fibonacci(n - 1) + fibonacci(n - 2)}')
    return fibonacci(n - 1) + fibonacci(n - 2)

rango = int(input('Ingresa el rango que quieres para ver el flujo fibonacci: '))

for n in range(0, rango):
    print(n, ':', fibonacci(n))
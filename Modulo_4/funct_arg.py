def multiplicar_por_dos(n):
    """Multiplica un número por 2

    n int > 0
    return n*2
    """
    return n * 2

def sumar_dos(n):
    """Suma 2 a un número

    n int > 0
    return n+2
    """
    return n + 2

def aplicar_operacion(f, numeros):
    """Aplicará 2 funciones definidas arriba

    f -> función multiplicar o sumar
    numeros -> array de 3 posiciones con listado de números a operar

    return array con 3 resultados.
    """
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    return resultados

nums = [1, 2, 3]
print(f'Multiplicación de números: {aplicar_operacion(multiplicar_por_dos, nums)}')
# [2, 4, 6]

print(f'Suma de números: {aplicar_operacion(sumar_dos, nums)}')
# [3, 4, 5]
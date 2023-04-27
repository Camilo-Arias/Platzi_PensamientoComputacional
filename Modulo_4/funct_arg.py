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

# Fuction lambda es una fuction mas sencilla y puede ser anonima
# Recibe un nombre restar, 2 parametos, y después de los : un return.
restar = lambda x, y: x - y

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

# Array vacio
nums = []

# For de 1 hasta 3 
for n in range(1, 4):
    # Captura de datos de usuario para rellenar array
    numingestado = int(input(f'Ingresa número entero #{n}: '))
    # Rellenando array nums con append.
    nums.append(numingestado)

# Imprimiendo array logrado
print(nums)

print(f'Multiplicación de números: {aplicar_operacion(multiplicar_por_dos, nums)}')
# [2, 4, 6]

print(f'Suma de números: {aplicar_operacion(sumar_dos, nums)}')
# [3, 4, 5]

print(f'resta de números: {restar(nums[0], nums[1])}')
# 4
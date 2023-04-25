def aplicar_operaciones(num):
    """Ejecutara las funciones que esten dentro del array

    num int != null

    return [abs(num), float(num)]
    """
    operaciones = [abs, float]

    resultado = []

    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

num = int(input('Ingresa un número a calcular absoluto y volverlo flotante: '))
# imprimirá el array de resultados obtenidos de las functions
print(aplicar_operaciones(num))
def suma_recursiva(n):
    """Calcula la longitud de un numero

    n = numero a calcular

    returns longitud
    """
    # print(n)
    div = n / 10
    # si div < 1 quiere decir que es un numero del 1 al 9 y se retornará 1 que es 1 digito
    if div < 1:
        return 1
    # si div == 1 quiere decir que es un 10 y tendrá 2 digitos
    elif div == 1:
        return 2   
    # la recursividad irá sumando 1 cada ves que se repita ejemplo
    # 333 / 10 = 33,3   return 1
    # 33,3 / 10 = 3,3   return 1
    # 3,3 / 10 = 0,33   if 0,33 < 1 return 1
    # se sumarán los 3 return será igual a 3
    return 1 + suma_recursiva(div)
# Metodo1

number = int(input('Ingresa un número grande: '))

lentNumber = str(number)

print(f'Usando len {len(lentNumber)}')

# Metodo2
print(f'Calculando con function recursiva {suma_recursiva(number)}')
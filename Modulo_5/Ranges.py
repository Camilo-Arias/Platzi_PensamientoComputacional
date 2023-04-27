# range(comienzo, termina, pasos)

def printSecuencia(secu):
    my_instrutions = ('impares', 'pares')
    """Definirá si imprime pares o impares

    secu == String (impar o par)
    return (print(impar o par))
    """

    if secu == my_instrutions[0]:
        # Print pares
        for i in range(0, 101, 2):
            print(i)
    elif secu == my_instrutions[1]:
        # Print impares
        for i in range(1, 100, 2):
            print(i)

# si los comparo será true dado que imprimiría 0, 2, 4, 6
my_range = range(0, 7, 2)
my_other_range = range(0, 8, 2)

# Capture value of client
argu = input("Escribe impares o pares dependiendo que quieres imprimir: ")
# call of function
printSecuencia(argu)
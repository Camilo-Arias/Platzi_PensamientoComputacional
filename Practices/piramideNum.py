limit = int(input('Ingresa el máximo que deseas para la piramide: '))

# se realizará un for inverso de x hasta x-1 ... = 1
for i in range(limit, 0, -1):
    # Se define un for anidado que recibirá el i como indice de inició e imprimirá los números descendientes en una sola linea
    for j in range(i, 0, -1):
        print(j, end=' ')
    # Se imprimirá un print vacio para realizar el salto de linea
    print('')
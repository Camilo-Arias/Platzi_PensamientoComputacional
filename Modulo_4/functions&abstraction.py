def aproximacion(obj):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else: 
        print(f'La raiz cuadrada del {objetivo} es {respuesta}')

def enumeracion(obj):
    respuesta = 0

    while respuesta**2 < objetivo:
        # print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raiz cuadrada exacta')

def busquedaBinaria(obj):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    # El minimo será 1,0
    while abs(respuesta**2 - objetivo) >= epsilon:
        # print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}, epsilon={epsilon}') Linea realizada para entender el funcionamiento
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2
        # print(f'...... {abs(respuesta**2 - objetivo)}')    Linea realizada para entender el funcionamiento

    print(f'La raiz cuadrada del {objetivo} es {respuesta}')

def menu(opcion, obj):
    while opcion != 4:
        if opcion == 1:
            aproximacion(obj)
            break
        elif opcion == 2:
            enumeracion(obj)
            break
        elif opcion == 3:
            busquedaBinaria(obj)
            break
        else:
            print('La opción elegida no existe')
            opcion = int(input('''Menú de opciones
    1) Raiz cuadrada por aproximación
    2) Raiz cuadrada por enumeración
    3) Raiz cuadrada por busqueda binaria
    4) Salir
Elige tu opción: '''))  


objetivo = int(input('Escoge un entero: '))
opcion = int(input('''Menú de opciones
    1) Raiz cuadrada por aproximación
    2) Raiz cuadrada por enumeración
    3) Raiz cuadrada por busqueda binaria
    4) Salir
Elige tu opción: '''))

menu(opcion, objetivo)
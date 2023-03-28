objetivo = int(input('Escoge un numero: '))
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

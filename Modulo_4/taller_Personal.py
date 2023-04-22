def pesoPlanetario(peso, gravedad):
    gravedadTierra = 9.8
    result = (peso / gravedadTierra) * gravedad
    return result

def menu(opcion):
    gravedadMercurio = 3.7
    gravedadVenus = 8.87
    gravedadMarte = 3.711
    gravedadJupiter = 24.79
    gravedadSaturno = 10.44
    gravedadUrano = 8.87
    gravedadNeptuno = 11.15
    gravedadPluton = 0,62
    gravedadLuna = 1.622

    while opcion != 0:
        pesoTerrestre = float(input("ingrese su peso en kilogramos con (.) si tiene decimales: "))
        if opcion == 1:
            print(f'Su peso en Mercurio es: {pesoPlanetario(pesoTerrestre, gravedadMercurio)}')
            break
        elif opcion == 2:
            print(f'Su peso en Venus es: {pesoPlanetario(pesoTerrestre, gravedadVenus)}')
            break
        elif opcion == 3:
            print(f'Su peso en Marte es: {pesoPlanetario(pesoTerrestre, gravedadMarte)}')
            break
        elif opcion == 4:
            print(f'Su peso en Jupiter es: {pesoPlanetario(pesoTerrestre, gravedadJupiter)}')
            break
        elif opcion == 5:
            print(f'Su peso en Saturno es: {pesoPlanetario(pesoTerrestre, gravedadSaturno)}')
            break
        elif opcion == 6:
            print(f'Su peso en Urano es: {pesoPlanetario(pesoTerrestre, gravedadUrano)}')
            break
        elif opcion == 7:
            print(f'Su peso en Neptuno es: {pesoPlanetario(pesoTerrestre, gravedadNeptuno)}')
            break
        elif opcion == 8:
            print(f'Su peso en Pluton es: {pesoPlanetario(pesoTerrestre, gravedadPluton)}')
            break
        elif opcion == 9:
            print(f'Su peso en Luna es: {pesoPlanetario(pesoTerrestre, gravedadLuna)}')
            break
        else:
            print('La opción elegida no existe')
            opcion = int(input('''Menú de opciones
    1) Peso Mercurio
    2) Peso Venus
    3) Peso Marte
    4) Peso Jupiter
    5) Peso Saturno
    6) Peso Urano
    7) Peso Neptuno
    8) Peso Pluton
    9) Peso Luna
    0) Salir
Elige tu opción: '''))  

opcion = int(input('''Menú de opciones
    1) Peso Mercurio
    2) Peso Venus
    3) Peso Marte
    4) Peso Jupiter
    5) Peso Saturno
    6) Peso Urano
    7) Peso Neptuno
    8) Peso Pluton
    9) Peso Luna
    0) Salir
Elige tu opción: '''))  

menu(opcion)
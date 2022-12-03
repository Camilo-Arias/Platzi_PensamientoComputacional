nombre1 = input('Buenos días, puedes ingresar el nombre del primer usuario: ')
nombre2 = input('Buenos días, puedes ingresar el nombre del segundo usuario: ')
edad1 = int(input('Ingresa la edad del primer usuario: '))
edad2 = int(input('Ingresa la edad del segundo usuario: '))

if edad1 < edad2:
    print(f'El usuario {nombre2}, es mayor que el usuario {nombre1}')
elif edad1 > edad2:
    print(f'El usuario {nombre1}, es mayor que el usuario {nombre2}')
else:
    print(f'{nombre2} y {nombre1}, tienen la misma edad')

maxPrint = int(input('Ingresa un número máximo que quieres que se plasme: '))

for i in range(1, (maxPrint + 2)):
    if i > maxPrint:
        for j in range((maxPrint - 1), 0, -1):
            print('* ' * j)
    else:
        print('* ' * i)
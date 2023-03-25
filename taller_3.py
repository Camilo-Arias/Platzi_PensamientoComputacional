import random

alea = random.randint(1,2)
num_user = int(input("Ingrese un número entre 1 y 2: "))

if alea == num_user:
    print("los números son iguales")
else:
    print(f'El número aleatorio fue {alea} y el número insertado por el usuario fue {num_user}')
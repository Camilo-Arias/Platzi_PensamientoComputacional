#Escribir un programa que almacene la cadena de caracteres contraseña en una variables, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas

password = input("Introduce tu contraseña: ")

password_correct = input("Introduce tu contraseña nuevamente: ")

if password != password_correct:
    print("La contraseña ingresada no concuerda con la contraseña ingresada inicialmente")
else:
    print("¡¡¡Felicidades!!!, ingresaste correctamente")
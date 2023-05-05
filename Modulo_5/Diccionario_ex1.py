diccionario = {
  "key0": [1,2], 
  "key1": "Listo", 
  "key2": 1234, 
  "key3": 00
  }

# Muestra las llaves del diccionario
# print(diccionario.keys())
# # Muestra los valores de las llaves.
# print(diccionario.values())
# # llamando los valores del diccionario
# print(diccionario['key0'])
# # Cambiando valor del diccionario
# diccionario['key1'] = "Hola Mundo"
# print(diccionario['key1'])
# imprimiendo llave donde está el valor enviado en C
lugar = 0
c = [1,2]
for index, value in diccionario.items():
  # print(index, value)
  if value == c:
    lugar = index

if lugar != 0:
  print(lugar)
else:
  print('no existe')
import math

# Reto a realizar:
# tenemos un cliente que va a realizar una tranferencia bancaria pero contamos con las siguientes
# condiciones:
# 1) Cliente Verificado (True and False)
# 2) Destino Verificado (True and False), en mi caso se lo di como input al usuario y lo comparo como no null
# 3) Saldo mayor al monto a tranferir más el costo de transferencia

# 4) Costo transacción
# Si el banco destino es el mismo al banco origen el costo de transaccion será de 0 USD
# Si el banco destino es diferente al banco origen el costo de transacción será superior a 1, dependerá
#     Del monto de transacción por cada 0 que lleve el monto el costo ira aumentando de a 10 USD
#     Ejemplo: 10 USD costo 1 USD, 100 USD costo 10 USD.
# 5) Solo se pueden hacer tranferencias en hora de 9 a 12 o de 15 a 20

userAccount = True
userBalance = 2000
schedule = [9, 12, 15, 20]
originBank = input('Ingrese el banco origen: ')
targetBank = input('Ingrese el banco destino: ')
transferBalance = float(input('Ingrese el monto a enviar: '))
transferTime = int(input('Ingrese la hora en la cual está realizando la transacción: '))

fee = math.floor(transferBalance/10)

if transferTime < schedule[1] and transferTime >= schedule[0] or transferTime < schedule[3] and transferTime >= schedule[2]:
    if targetBank != originBank:
        if fee >= 1 or fee <= 100:
            if fee > 100:
                fee = 100
                transferBalance = transferBalance + fee
            else:
                transferBalance = transferBalance + fee
            if userAccount:
                if len(originBank) != 0:
                    if transferBalance <= userBalance:
                        print(f'Tranferencia exitosa, el costo de tranferencia fue de: {fee}')
                    else:
                       print(f'El saldo a tranferir supera los fondos de la cuenta por: {transferBalance-userBalance}')
                else: 
                    print('El banco origen no puede estar vacio')
            else:
                print('la cuenta tiene que estar verificada')
    else:
        if userAccount:
            if len(originBank) != 0:
                if transferBalance <= userBalance:
                    print('Tranferencia exitosa')
                else:
                    print('El saldo a tranferir supera los fondos de la cuenta')
            else: 
                print('El banco origen no puede estar vacio')
        else:
            print('la cuenta tiene que estar verificada')
else:
    print('¡Los bancos ya están cerrados!')
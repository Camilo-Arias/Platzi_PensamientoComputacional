contador_segundos = 0
contador_minutos = 0
contador_horas = 0
contador_días = 0

while contador_días < 2:
    while contador_horas < 24:
        print(f'Hora {contador_horas+1}')
        contador_horas += 1
        while contador_minutos < 60:
            print(f'minutos {contador_minutos+10}')
            contador_minutos += 10
        contador_minutos = 0    
    print(f'Día {contador_días+1}')
    contador_días += 1
    contador_horas = 0

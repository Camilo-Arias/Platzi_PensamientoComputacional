day = 24
hour = 0
minutes = 0
seconds = 0
count = 0

while hour < day:
    minutes += 60
    while count < minutes:
        seconds += 60
        count += 1
    hour += 1
print(f'En un día hay: {seconds} segundos')

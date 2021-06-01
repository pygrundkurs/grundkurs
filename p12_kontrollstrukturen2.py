from random import random

# Zufällige zwischen 0 und 0.999999
# Aufgabe: Gebe mit 42 % wahrscheinlichkeit gewonnen aus

zufalls_zahl = random()
print(zufalls_zahl)

if zufalls_zahl < 0.42:
    print('Gewonnen')


cnt = 0

for i in range(0, 10000000):
    zufalls_zahl = random()

    if zufalls_zahl < 0.42:
        cnt += 1  # cnt = cnt + 1


print(cnt)



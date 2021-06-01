from random import random

cnt = 0

for i in range(0, 10000000):
    zufall = random()

    if zufall < 0.42:
        cnt += 1

print(cnt)

# Definition des Zählers
i = 0

# Bis wann soll die Schleife laufen?
while i < 10:
    # Was soll bei jedem Durchlauf geschehen?
    print(i)
    i += 1

# While wird verwendet wenn man nicht weis wie lange etwas dauert
# ODER etwas für immer laufen soll
zahl = 10000
cnt = 0

while zahl > 10:
    zahl = zahl / 3
    print(zahl)
    cnt += 1

print('Durchläufe: ', cnt)

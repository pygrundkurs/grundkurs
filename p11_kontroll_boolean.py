if True:
    print('True')

if False:
    print('False')

if 42:
    print('42')


print(bool(42))

zahl = 42

if zahl:
    print('Zahl hat einen Wert')


if 0:
    print('bla')

# Alle Zahlen ausser 0 sind True
print(bool(0))
print(bool(1))
print(bool(-1))

# Was ist False (ausser False)
# 0 '' [] () {} False None

if 'hallo':
     print('ja')

print(bool('hallo'))
print(bool(''))

zahl = 42

# zahl != 0
if zahl:
    print('Yep Zahl hat einen Wert')

zahl = 0

if not zahl:
    print('Zahl ist 0')

if zahl == 0:
    print('Zahl ist 0')

wort = ''

if not wort:
    print('FEHLER')


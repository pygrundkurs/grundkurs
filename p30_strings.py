# Strings / Zeichenketten
wort = 'Hallo Welt'

# Komplett groß
print(wort.upper())

# Komplett klein
print(wort.lower())

print('hallo'.capitalize())

print(wort.replace('Welt', 'Python'))

wort = wort.replace('Welt', 'Python')
print(wort)

# Endet der String mit etwas
print(wort.endswith('Python'))
print(wort.startswith('bla'))

print(wort)
# An Welcher Stelle (Index) steht etwas
print(wort.find('Python'))
print(wort.find('Hallo'))
print(wort.find('allo'))

# -1 -> wenn das Wort den Text nicht enthält
print(wort.find('asdf'))

if wort.find('asdf') == -1:
    print('Wort enthätl asdf nicht')

print(wort.isnumeric())
print('42'.isnumeric())

# Trim (Leerzeichen am Anfang und Ende entfernen)
print(' hallo welt '.strip())

# Teilt einen String anhand eines ZEichen in eine Liste
print('hallo,welt,42'.split(','))

print(' --- '.join(['Bernd', 'Maria', 'Tanja']))

text = 'Hallo Welt'

# Teile ausgeben
print(text[3])
print(text[:5])
print(text[6:10])
print(text[:1])
print(text[::2])

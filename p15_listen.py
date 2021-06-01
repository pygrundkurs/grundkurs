# Liste -> Index
# 0, 1, 2, 3
zahlen = [1, 2, 42, 3]

print(zahlen[1])
print(zahlen)

zahlen[1] = 23
print(zahlen)

# Neues Element einfügen
# Zwei Listen miteinander verbinden
zahlen += [99]
print(zahlen)

zahlen.append(77)
print(zahlen)

namen = ['Bernd', 'Maria', 'Tanja']

# Ein Element löschen
# namen.remove(namen[1]) # Über index löschen
# Löscht das Element und baut den Index neu auf
namen.remove('Maria')

print(namen)
print(namen[1])

# Append immer am Ende
namen.append('Maria')
namen.append('Jana')
namen.append('Jens')

# Insert an dem mitgegeben INdex
namen.insert(1, 'bla')

print(namen)

# Sortieren
namen.sort(reverse=True)
print(namen)

print(namen.pop(1))
print(namen)

# Teile ausgeben
# Start:Ende (Exklusiv):Interval
print(namen[:3])  # Ersten 3 Elemente
print(namen[::2])  # Jedes 2. Element
print(namen[1])
print(namen[::3])
print(namen)

vektor = [[1, 2], [3, 4], [5, 42]]

print(vektor[2][1])

# Multidimensionale Arrays
multi = [2, [3, [4, [5, [6, [7, [8, [[3, 4, 42]]]]]]]]]

print(multi[1][1][1][1][1][1][1][0][2])

# Gemischte Datentypen
# SOLLTEN vermieden werden
gemischt = ['Maria', 42, 6.219]

# wie groß ist meine Liste?
print(namen.count('Jens'))

# KEINE Methode, sondern eine Funktion
print(len(namen))

# OOP
# 2 Punkte
# x: 20 y: 22
# x: 10 y: 12

punkte_als_liste = [[20, 22], [10, 12]]
punkte_als_dict = [
    {'x': 20, 'y': 22},
    {'x': 10, 'y': 12}
]

print(punkte_als_dict[1]['x'])


# Die Klasse
class Punkt:
    x = 0
    y = 0
    z = 0


# Punkt p1 = new Punkt()
# Das hier das Objekt
p1 = Punkt()
p2 = Punkt()

p1.x = 22
p1.y = 20
p2.x = 10
p2.y = 12
p2.z = 4454

print(p1.x)
print(p1.z)
print(p2.x)
print(p2.z)
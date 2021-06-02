from random import random


class Auto:
    # Falsche Art
    # # Attribute
    # hersteller = ''
    # modell = ''
    # ps = None

    def __init__(self, hersteller, modell, ps, farbe='weiß'):
        # Der Konstruktor initialisiert die Instanzvariablen
        self.hersteller = hersteller
        self.modell = modell
        self.ps = ps
        self.farbe = farbe

    # Methoden
    def fahren(self):
        return self.ps * random()


# Mercedes mercedes = new Auto();
mercedes = Auto('Mercedes', 'CLA SB', 159)
bmw = Auto('BMW', 'z5', 400, 'schwarz')
# nix = Auto() -- Fehler

print(mercedes.fahren())
print(bmw.fahren())
# print(nix.fahren())

immer_klein = 42


class Auto:
    pass


def is_meaning_of_life():
    return True


def get_meaning_of_life():
    return 42


class Auto:
    def has_ps(self):
        """
        Gibt den PS Wert zurück
        :return: boolean
        """
        return True

    def get_ps(self):
        """
        Gibt PS zurück
        :return: int
        """
        return 42

    def set_ps(self, ps):
        """
        Setzt PS
        :param ps: int
        """
        self.ps = ps

"""
Bennennung von Funktionen

* Komplett klein, mit _ getrennt
* Nur ASCII
* Wenn Sie einen Boolean zurückgeben fangen sie mit is_ oder has_
* get_ oder set_
* oder einem Verb (Beschreibt was getan wird)
* Funktionsname sollte andeuten ob etwas zurückgegeben wird oder nicht
"""

# test = [].append('asdf')
wort = 'hallo welt'
wort = wort.replace('welt', 'python')


print(type(wort))

#           0        1          2
namen = ['Bernd', 'Tanja', 'Michael']

kunde = {
    'vorname': 'Bernd',
    'nachname': 'Huber',
    'alter': 42
}

print(kunde['alter'])

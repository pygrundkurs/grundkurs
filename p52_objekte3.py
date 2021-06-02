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

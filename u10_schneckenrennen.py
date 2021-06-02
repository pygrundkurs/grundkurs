from random import random


class Rennschnecke:
    def __init__(self, name, rasse, max_v):
        self.name = name
        self.rasse = rasse
        self.max_v = max_v
        self.position = 0

    def krieche(self):
        strecke = self.max_v * random()
        self.position += strecke

    def to_string(self):
        return self.name + ' (' + self.rasse + ') ' + str(self.max_v) + ' === ' + str(self.position)


class Rennen:
    def __init__(self, name, laenge):
        self.name = name
        self.laenge = laenge
        self.teilnehmer = []
        self.anzahl_teilnehmer = 0

    def add_rennschnecke(self, schnecke):
        self.teilnehmer.append(schnecke)
        self.anzahl_teilnehmer += 1



rudi = Rennschnecke('Rudi', 'Weinbergschnecke', 10)
fritz = Rennschnecke('Fritz', 'Weinbergschnecke', 9)
mariechen = Rennschnecke(' ', 'Weinbergschnecke', 11)

nuerburg = Rennen('Nürburg', 100)
nuerburg.add_rennschnecke(rudi)
nuerburg.add_rennschnecke(fritz)
nuerburg.add_rennschnecke(mariechen)

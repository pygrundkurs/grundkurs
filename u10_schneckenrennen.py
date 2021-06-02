# https://wiki.freitagsrunde.org/Javakurs/%C3%9Cbungsaufgaben/Rennschnecke

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
        # __str__ als bessere Alternative
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

    def del_rennschnecke(self, name):
        self.teilnehmer.remove(name)

        for sn in self.teilnehmer:
            if sn.name == name:
                self.teilnehmer.remove(sn)
                self.anzahl_teilnehmer -= 1
                break

    def to_string(self):
        # __str__ als Alternative
        text = self.name + ' (' + str(self.laenge) + ') \n'

        for sn in self.teilnehmer:
            text += sn.to_string() + '\n'

        return text

    def ermittle_gewinner(self):
        for sn in self.teilnehmer:
            if sn.position >= self.laenge:
                return sn

        return None

    def lasse_schnecken_kriechen(self):
        for sn in self.teilnehmer:
            sn.krieche()

    def durchfuehren(self):
        # == -> is
        while self.ermittle_gewinner() is None:
            self.lasse_schnecken_kriechen()

        return self.ermittle_gewinner()


s1 = Rennschnecke('Rudi', 'Weinbergschnecke', 10)
s2 = Rennschnecke('Fritz', 'Weinbergschnecke', 9)
s3 = Rennschnecke('Mariechen', 'Weinbergschnecke', 11)

nuerburg = Rennen('Nürburg', 100)
nuerburg.add_rennschnecke(s1)
nuerburg.add_rennschnecke(s2)
nuerburg.add_rennschnecke(s3)

# Nicht die Schnecke
# nuerburg.del_rennschnecke(rudi)
# Nur der NAME rudi.name
# nuerburg.del_rennschnecke('Rudi')

nuerburg.durchfuehren()
print(nuerburg.to_string())

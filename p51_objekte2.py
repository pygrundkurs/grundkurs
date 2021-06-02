class Kunde:
    # Eigenschaften / Attribute / Instanzvariablen / Properties
    vorname = ''
    nachname = ''
    alter = 0

    # Methoden
    def print_info(self):
        # self == this
        print('Vorname:', self.vorname)
        print('Nachname:', self.nachname)

    def set_vorname(self, vorname):
        self.vorname = vorname


jens = Kunde()
tanja = Kunde()

jens.vorname = 'Jens'
jens.nachname = 'Müller'
jens.alter = 42

tanja.vorname = 'Tanja'
tanja.nachname = 'Huber'
tanja.alter = 22

jens.print_info()
print('-----')
tanja.print_info()

jens.vorname = 'Joseph'

# Über einen Setter
jens.set_vorname('Joseph')
jens.print_info()

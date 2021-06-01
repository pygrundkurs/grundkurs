# Funktionale Programmierung

"""
public static void printHallo() {
    System.out.println("Hallo");
}
"""


def print_hallo():
    # Definition der Funktion
    print('Hallo Python')


# Aufruf der Funktion
print_hallo()
print_hallo()

"""
public static void addiere(int zahl1, int zahl2) {
    System.out.println(zahl1 + zahl2);
}
"""


def addiere(zahl1, zahl2):
    print(int(zahl1) + int(zahl2))


addiere(20, 22)
addiere('20', 22)
asdf = ['asdf', 'basdf', 'dfsdf', 'asdwf']


def gebe_namen_aus(namen):
    for name in namen:
        print(name)


gebe_namen_aus(['Bernd', 'Maria', 'Tanja'])
gebe_namen_aus(asdf)

import z01_modul
import random
# from random import random
from z01_modul import guten_morgen

z01_modul.guten_morgen()
print(random.random())

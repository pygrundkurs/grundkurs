# Datentypen
# int zahl = 42;
# String wort = "Hallo Welt";
# double pi = 3.1415925;

# Zahlen
# 8-bit Prozessor (2^8 = 256)
# 0 bis 255 ODER -128 bis +127
# 00000000 - 11111111
# IPv4: 2^8.2^8.2^8.2^8
# 0.0.0.0
# 255.255.255.255
# rgb(255,0,0)
# [u]byte tinyint = 42;

# 16-bit Prozessor (2^16 = 65536)
# short kleinezahl = 4242;
# Neztwerkports: 1-65535

# 32-bit Prozessor (2^32 = 4.290.000.000)
# int zahl = 42; // int32

# 64-bit Prozessoren (2^64 = 1,89e^20)
# long
# int zahl = 42; // int64

zahl = 42

print(type(zahl))

# Kommazahlen
# float pi = 3.14159f; 2^32
# double pi = 3.141592524; 2^64

pi = 3.1415925
print(type(pi))

print(1.1234567890123456789)
print(4.1234567890123456789)
print(123123123.1234567890123456789)

print(0.5 + 0.5)
print(0.5 + 0.3 + 0.2)
print(0.5 + 0.2 + 0.2 + 0.1)
print(0.5 + 0.2 + 0.1)
print(round(0.5 + 0.2 + 0.2 + 0.1))

# String
wort = 'Hallo'
print(type(wort))

# Boolean
wahr = True
falsch = False
print(42 == 42)
print(23 == 42)
print(type(wahr))

# Arrays (Listen)
# int[] zahlen = {1, 2, 3, 4};
zahlen = [1, 2, 3, 4]

print(type(zahlen))

# Tuple
namen = ('Bernd', 'Maria', 'Tanja')
print(type(namen))


# Funktionen
# public static void print_hallo()
def print_hallo():
    print('Hallo')


print(type(print_hallo))

# None -> Leere
print(type(None))


# int zahl;

class Test:
    def print_hallo(self):
        print('Hallo')


print(type(Test))

# class Test {}
# Klassen Objekte bilden
# Test t1 = new Test();
t1 = Test()

print(type(t1))
t1.print_hallo()

import math

print(math.pi)
print(type(math))

# // Das ist ein Kommentar
# /* */
"""
Primitive Datentypen (int, float, String, boolean)
Komplexe Datentypen (Listen, Tuples, Dict, Objekte, Klassen ...)
"""

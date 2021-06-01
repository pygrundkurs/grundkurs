# Zuweisungsoperator
a = 'b'

# Verknüpfungsoperator
print('hallo ' + 'welt')

# Vergleichsoperatoren
print(42 == 42)

# > >= < <= == !=
print(42 != 23)

# == -> Überprüft den Inhalt und den DATENTYP
print(42 == '42')
print('42' == '42')

# AUSNAHME
print(42 == 42.0)

# Logische Operatoren
# 42 == 42 && 42 > 10
# True and False = False
# False and False = False
# False and True = False
# True and True = True

print(42 == 42 and 42 < 10)

# Logische ODER
# ||
# True and False = True
# False and False = False
# False and True = True
# True and True = True
print(42 == 42 or 42 < 10)

# Logische NICHT
# !

print(not False)
print(not True)

print(not 42 == 42)
print(42 != 42)

datei_existiert = False

#if datei_existiert == False:
if not datei_existiert:
    print('FEhler DATEI EXISTIERT NICHT')



kunde_als_liste = ['Bernd', 'Huber', 42]

kunde = {
    'vorname': 'Bernd',
    'nachname': 'Huber',
    'alter': 42
}

print(kunde['vorname'])
print(kunde['nachname'])

print(kunde.get('alter', 'Gibts nicht'))
# print(kunde['asdf'])

laueft_noch = True

# while True

while laueft_noch:
    eingabe = input('Sinn des Lebens? ')

    if eingabe == '42':
        laueft_noch = False
    else:
        print('Du bist noch auf der Suche')

print('Du hast den SInn gefunden')

# Cäsar Chiffre
# text zum verschlussen, zahl (chiphre)

# Hallo -> 3 Stellen im Alphabet -> Kdoor
# z -> c

def encrypt(text, cipher):
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '  # Unser Alphabet
    text_verschluesselt = ''  # Unser verschlüsselter Text

    for b in text:  # Schleife über jeden Buchstaben
        position_im_alphabet = abc.find(b)  # Die SUche im Alphabet nach der Position (int)
        neue_position = position_im_alphabet + cipher  # Die Cipher drauf addieren

        if neue_position > len(abc) - 1:  # Prüfen das wir nicht ausserhalb des Alphabets sind
            neue_position -= len(abc)

        neuer_buchstabe = abc[neue_position]  # Den Buchstaben an der neuen Position im abc finden
        text_verschluesselt += neuer_buchstabe  # Den Buchstaben an text_verschluesselt dranhängen

    return text_verschluesselt


print(encrypt('Hallo', 1))
print(encrypt('Hallo', 2))
print(encrypt('Hallo', 3))
print(encrypt('Python macht Spass', 3))

zahl = 666

"""
if (zahl == 42) { 
    System.out.println("Zahl gefunden");
} else {
   System.out.println("Du bist noch auf der Suche");
}
"""

if zahl == 42:
    # Block Anfang
    print('Sinn gefunden')
    # Block Ende
elif zahl == 666:
    # Reihenfolge beachten!
    print('?!?!?!?!')
elif zahl > 100:
    print('Life is simple')
else:
    print('Du bist noch auf der Suche')

print('Wird immer ausgegeben')

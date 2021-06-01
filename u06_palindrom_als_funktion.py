def get_wort_umgedreht(wort):
    return wort[::-1]


def is_palindrom(wort):
    umgedreht = get_wort_umgedreht(wort)

    if umgedreht.lower() == wort.lower():
        return True

    return False


print(is_palindrom('Hallo'))
print(is_palindrom('Anna'))
print(is_palindrom('Rentner'))
print(is_palindrom('Reliefpfeiler'))

eingabe = input('Wort? ')
print(is_palindrom(eingabe))
def addiere(zahl1, zahl2):
    return zahl1 + zahl2
    # AB hier ist die FUnktion beendet


ergebnis = addiere(20, 22)
print(ergebnis)


def is_sinn(zahl):
    if zahl == 42:
        return True
    else:
        return False


print(is_sinn(42))
print(is_sinn(23))


def is_sinn_schoen(zahl):
    if zahl == 42:
        return True

    # Der Code wird nur erreicht, wenn die if bendingung False war
    return False


print(is_sinn_schoen(42))
print(is_sinn_schoen(23))


def is_sinn_schoener(zahl):
    return zahl == 42


print(is_sinn_schoener(42))
print(is_sinn_schoener(23))


def nur_eine_sache(zahl1, zahl2):
    ergebnis_addition = zahl1 + zahl2
    ergebnis_multiplikation = zahl1 * zahl2

    # return [ergebnis_addition, ergebnis_multiplikation]
    return {
        'addition': ergebnis_addition,
        'multiplikation': ergebnis_multiplikation,
    }


ergebnis = nur_eine_sache(20, 22)
print(ergebnis['addition'])
print(ergebnis['multiplikation'])


def print_text(text, bold=False):
    # Optionale Parameter
    # bold hat den Standardwert False, solange nichts anderes übergeben wird
    if bold:
        print('<b>' + text + '<b>')
    else:
        print(text)


print_text('hallo', False)
print_text('hallo', True)
print_text('hallo')


def exponential_rechnen(zahl, exp=2):
    print(zahl ** exp)


exponential_rechnen(10)
exponential_rechnen(3)
exponential_rechnen(3, 3)
exponential_rechnen(2, 32)
exponential_rechnen(2, 64)


# def so_nicht(argument_1, argument_2=42, argument_3):
#     pass


def mehrere_benannte_parameter(argument_1, argument_2=42, argument_3=223):
    print(argument_1 + argument_2 + argument_3)


mehrere_benannte_parameter(23, argument_3=23)


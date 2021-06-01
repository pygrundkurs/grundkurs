# Aufgabe: Gib die ersten 1000 Primzahlen aus
# 2,3,5,7,11,13,17,19

# Die Aufgabe aufteilen in kleinere Aufgaben
# Wie ermittle ich ob etwas eine Primzahl ist?
# Danach: WIe gebe Ich die ersten 1000 Primzahlen aus?


cnt = 0  # Wieviele Primzahlen haben wir schon gefunden?
zahl = 3  # Startzahl zum testen

# Schleife läuft bis wir 1000 Primzahlen gefunden haben
while cnt < 1001:
    is_prime = True  # Wir gehen erstmal davon aus das es sich um eine Primzahl handelt

    # Test ob es eine Primzahl ist
    for i in range(2, zahl):  # Schleife geht von 2 bis exklusiv der `zahl` (z.b. bei 13 von 2 bis 12)
        # 12 % 2 = 0 == 0
        if zahl % i == 0:  # Wenn unsere `zahl` teilbar ist durch eine dieser, dann ist es keine Primzahl
            is_prime = False  # Dementsprechend setzen wir die Variable auf False
            break  # Und hören auf weiter zu testen

    if is_prime:  # Falls es nicht teilbar war (und somit eine Primzahl ist)
        cnt += 1  # Anzahl der gefunden Primzahlen erhöhen
        print(zahl, end=', ')  # Primzahl mit , am Ende ausgeben (statt \n)

        if cnt % 20 == 0:  # Alle 20 gefunden Primzahlen
            print('')  # ein Zeilenumbruch

    zahl += 1  # IMMER nach jedem Durchlauf, wählen wir eine neue Zahl zum testen

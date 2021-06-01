alter = 42

# In Abhängigkeit des Alters wollen wir Tickets verkaufen
# Personen unter 18: Kinderticket
# Senioren ab 65: Seniorenticket
# Erwachsene: Erwaschenenticket

if alter < 18:
    print('kinderticket')
elif alter > 64:
    print('senioren')
else:
    print('erwachsenen')


if 65 > alter > 17:
    print('Erwachsenenticket')
elif alter > 64:
    print('Senioren')
else:
    print('Kinder')

print('hallo')

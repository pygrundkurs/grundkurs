import csv342 as csv

kunden = []

with open('test.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        kunden.append(
            row
        )

print(kunden)

for kunde in kunden:
    print(kunde['vorname'])

# Palindrom
# Wort was von hinten und vorne gleich ist
# anna = anna
# hallo = ollah
# rentner = rentner
# reliefpfeiler = reliefpfeiler

wort = input('Wort? ')
wort_umgedreht = ''

# for (int i = wort.length - 1; i >= 0; i--)
# (4, 3, 2, 1, 0)
for i in range(len(wort) - 1, -1, -1):
    buchstabe = wort[i]
    wort_umgedreht += buchstabe

print(wort_umgedreht)

if wort_umgedreht.lower() == wort.lower():
    print('Ist ein Palindrom')
else:
    print('Ist kein Palindrom')

# Mit while
i = len(wort) - 1  # 4
wort_umgedreht = ''

while i >= 0:
    buchstabe = wort[i]
    wort_umgedreht += buchstabe
    i -= 1

print(wort_umgedreht)

# Python Lösungen
#
# if wort == reversed(wort):
#     print('Paldindrom')

print(wort[::-1])

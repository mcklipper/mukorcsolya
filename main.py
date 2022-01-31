from pathlib import Path
from Versenyzo import Versenyzo


def osszPontszam(nev: str):
    eredmeny = 0.0

    i = 0
    while versenyzok[i].nev != nev:
        i += 1
    eredmeny += versenyzok[i].osszPontszam()

    i = 0
    while i < len(dontosok) and dontosok[i].nev != nev:
        i += 1
    if i < len(dontosok):
        eredmeny += dontosok[i].osszPontszam()

    return eredmeny


fajl = Path('rovidprogram.csv').open(encoding='utf-8')
versenyzok = []

elsoSor = True
for sor in fajl:
    if elsoSor:
        elsoSor = False
        continue
    versenyzok.append(Versenyzo(sor.strip().split(';')))

fajl = Path('donto.csv').open(encoding='utf-8')
dontosok = []

elsoSor = True
for sor in fajl:
    if elsoSor:
        elsoSor = False
        continue
    dontosok.append(Versenyzo(sor.strip().split(';')))

versenyzokSzama = len(versenyzok)
print(f'2. feladat\n\tA rövidprogramban { versenyzokSzama } induló volt.')

i = 0
while i < versenyzokSzama and dontosok[i].orszagKod.upper() != 'HUN':
    i += 1

print('3. feladat')
if i < versenyzokSzama:
    print('\tA magyar versenyző bejutott a kűrbe.')
else:
    print('\tA magyar versenyző nem jutott be a kűrbe.')

versenyzoNeve = input('5. feladat\n\tKérem a versenyző nevét: ')
i = 0
while i < versenyzokSzama and versenyzok[i].nev != versenyzoNeve:
    i += 1

if i == versenyzokSzama:
    print('\tIlyen nevű induló nem volt.')
else:
    print(f'6. feladat\n\tA versenyző összpontszáma: { osszPontszam(versenyzoNeve) }')

versenyzokOrszagonkent = {}
for versenyzo in dontosok:
    if versenyzo.orszagKod not in versenyzokOrszagonkent:
        versenyzokOrszagonkent[versenyzo.orszagKod] = 1
    else:
        versenyzokOrszagonkent[versenyzo.orszagKod] += 1

print('7. feladat')
for x in versenyzokOrszagonkent:
    if versenyzokOrszagonkent[x] > 1:
        print(f'\t{x}: {versenyzokOrszagonkent[x]} versenyző')

vegeredmeny = []
for v in versenyzok:
    vegeredmeny.append((v.nev, v.orszagKod, osszPontszam(v.nev)))

vegeredmeny.sort(key=lambda tup: tup[2], reverse=True)

ujfajl = Path('vegeredmeny.csv').open(encoding='utf-8', mode='w+')
for i in range(len(vegeredmeny)):
    ujfajl.write(f'{i + 1};{vegeredmeny[i][0]};{vegeredmeny[i][1]};{round(vegeredmeny[i][2], 2)}\n')

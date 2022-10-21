nev:str = input('név: ')
max_p:int = int(input('maximális pontszám: '))
akt_p:int = int(input('elért pontszám: '))

if akt_p > max_p:
    print('Hibás adatokat adtál meg!')
else:
    sz:float = akt_p/max_p*100
    oszt:str = '_'
    if sz < 51: oszt = 'elégtelen'
    elif sz < 65: oszt = 'elégséges'
    elif sz < 77: oszt = 'közepes'
    elif sz < 90: oszt = 'jó'
    else: oszt = 'jeles'

    print(f'{nev} {round(sz, 1)}%-ot ért el a dolgozaton, osztályzata: {oszt}')
import random

talalat:int = 0
for i in range(5):
    x:int = random.randint(10, 99)
    y:int = random.randint(10, 99)
    sm:int = x + y
    df:int = x - y
    if df < 0: df *= -1
    print(f'{i+1}. kör: ')
    print(f'  A két szám összege: {sm}; különbsége: {df}. Mi lehet a két szám?')
    tx:int = int(input('    egyik szám: '))
    ty:int = int(input('    másik szám: '))
    if (x == tx and y == ty) or (x == ty and y == tx):
        print('  helyes!')
        talalat += 1
    else:
        print(f'  sajnos nem, a két szám {x} és {y}')
print(f'végeztünk, helyes találataid száma: {talalat}')
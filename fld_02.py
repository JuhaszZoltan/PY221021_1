a:int = int(input('háromszög "a" oldala: '))
b:int = int(input('háromszög "b" oldala: '))
c:int = int(input('háromszög "c" oldala: '))

if a+b<=c or a+c<=b or b+c<=a:
    print('ilyen oldalhosszokkal háromszög nem szerkeszthető!')
else:
    s = (a + b + c) / 2
    t = (s*(s-a)*(s-b)*(s-c)) ** .5
    print(f'a háromszög területe: {round(t, 2)} cm^2')
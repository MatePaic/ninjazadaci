a = int(input('Unesi duljinu stranice a: '))
b = int(input('Unesi duljinu stranice b: '))
c = int(input('Unesi duljinu stranice c: '))

if a != b != c != a:
    print('Trokut je raznostraničan')
elif a == b == c:
    print('Trokut je jednakostraničan')
else:
    print('Trokut je jednakokračan')
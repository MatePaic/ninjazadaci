x_koordinata = 0
y_koordianata = 0

while True:
    smjer = input('Unesite željeni smjer(U(p), D(own), L(eft), R(ight), Q(uit): ').lower()
    if smjer == 'u':
        x_koordinata += 1
    elif smjer == 'd':
        x_koordinata -= 1
    elif smjer == 'l':
        y_koordianata -= 1
    elif smjer == 'r':
        y_koordianata += 1
    elif smjer == 'q':
        break
    else:
        print('Ne prepoznaje smjer')
print(f'koordinate su: {x_koordinata, y_koordianata}')








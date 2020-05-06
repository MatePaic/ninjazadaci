krvna_grupa_primatelja = input('Krva grupa primatelja(A, B, AB, 0): ').lower()
krvna_grupa_donora = input('Krvna grupa donora(A, B, AB, 0:)  ').lower()
rh_primatelja = input('Rh primatelja(+, -): ')
rh_donora = input('Rh donora(+, -): ')

if (rh_primatelja == '+' and (rh_donora == '+' or rh_donora == '-'))\
        or (rh_primatelja == '-' and rh_primatelja == '-'):

    if krvna_grupa_donora == '0':
        print("Dozvoljena transfuzija")
    elif krvna_grupa_primatelja ==krvna_grupa_donora:
        print('Dozvoljena transfuzija')
    elif krvna_grupa_primatelja == 'ab':
        print('Dozvoljena transfuzija')
    else:
        print('Nedozvoljena transfuzija')

else:
    print('Nedozvoljena transfuzija')





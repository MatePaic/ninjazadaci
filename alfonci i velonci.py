alfonci = 5000000
velonci = 9000000
broj_godina = 0

while velonci >= alfonci:
    broj_godina += 1
    alfonci = alfonci * 1.06

    if broj_godina % 4 == 0:
        velonci = velonci * 1.05 - 500000

    else:
        velonci = velonci * 1.02

print('Broj Alfonaca ce premašiti broj Velonaca za {0} godina. Ukupan broj Alfonaca te godine je {1}'.format(broj_godina, alfonci))



težina = float(input('Težina prtljage: '))

if težina < 0 or težina > 50:
    print('Nedopušteni iznos')
elif težina < 15:
    print('Nema nadoplate')
else:
    naplata = (težina - 15) * 50
    print(f'Nadoplata iznosi {naplata:.2f}')

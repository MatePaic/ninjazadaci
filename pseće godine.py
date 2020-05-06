ljudske_godine = int(input('Unesi ljudske godine: '))


if ljudske_godine < 3:
    psece_godine = ljudske_godine * 10.5
    print(f'Pas ima {psece_godine} psece godine')
else:
    psece_godine = 10.5 + 10.5 + 4 * ljudske_godine - 2 * 4
    print(f'Pas ima {psece_godine} pseće godine')

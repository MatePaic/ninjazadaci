brojRedaka = int(input('Unesi broj redaka: '))
num = 1
for row in range(1, brojRedaka + 1):
    for col in range(1, row + 1):
        print(num,end=' ' )
        num += 1
    print()
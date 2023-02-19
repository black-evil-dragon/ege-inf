"""
for N in range(100):
    binN = str(bin(N)[2:])

    binN = binN + f'{binN.count("1") % 2}'
    binN = binN + f'{binN.count("1") % 2}'


    R = int(binN, 2)

    if R > 83:
        print(N, R)


for N in range(100):
    binN = str(bin(N)[2:])

    if binN.count('1') % 2 != 0:
        binN += '11'
    else:
        binN += '00'

    R = int(binN, 2)

    if R > 114:
        print(N, R)

"""
for N in range(100):
    binN = str(bin(N)[2:])

    binN = binN + f'{binN.count("1") % 2}'
    binN = binN + f'{binN.count("1") % 2}'

    R = int(binN, 2)

    if R > 97:
        print(N, R)



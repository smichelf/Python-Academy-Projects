import random
oddelovac='-' * 48
konec = False
print('Hi there!\n' + oddelovac)
while not konec:
    print("I've generated a random 4 digit number for you.\n" + "Let's play a bulls and cows game.\n" + oddelovac)
#
# computer number generation
#
    moznosti=['1','2','3','4','5','6','7','8','9']
    pcislo=list()
    for i in range(4):
        pcislo.append(random.choice(moznosti))
        moznosti=['0','1','2','3','4','5','6','7','8','9']
        for c in pcislo:
            moznosti.remove(c)
#
    bulls = 0
    steps = 0
#    print(pcislo)
    while bulls < 4:
        bulls = 0
        cows = 0
        obulls = 'bulls'
        ocows = 'cows'
        ucislo = list(input('Enter a number (0 to finish): '))
        steps += 1
        if ucislo[0] == '0':
            konec = True
            break
#
# count bulls and cows
#
        for i in range(4):
            if ucislo[i] in pcislo:
                if pcislo.index(ucislo[i]) == i:
                    bulls += 1
                else:
                    cows += 1
#
        if bulls == 1: obulls = 'bull'
        if cows == 1: ocows = 'cow'
        print(bulls, obulls + ',', cows,ocows, '\n' + oddelovac)
    if not konec:
        print("Correct, you've guessed the right number\nin " + str(steps) + ' guesses!\n' + oddelovac)
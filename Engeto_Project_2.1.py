
def welcome_gamer():
    print('Hi there!\n' + oddelovac)
#
# computer number generation
#
def generate_number():
    moznosti = list('123456789')
    pcc = list()
    for i in range(4):
        pcc.append(random.choice(moznosti))
        moznosti = list('0123456789')
        for c in pcc:
            moznosti.remove(c)
    print("I've generated a random 4 digit number for you.\n" + "Let's play a bulls and cows game.\n" + oddelovac)
    return pcc
#
# Count bulls and cows
#
def count_result(unumber, pnumber):
    res = {'bulls': 0, 'cows': 0}
    for i in range(4):
        if unumber[i] in pnumber:
            if pnumber.index(unumber[i]) == i:
                res['bulls'] += 1
            else:
                res['cows'] += 1
    return res

def user_guessing(pnum):
    result = {'bulls': 0, 'cows': 0}
    global konec
    steps = 0
    while result['bulls'] < 4:
        uscislo = input('Enter a number (0 to finish): ')
        if uscislo[0] == '0':
            konec = True
            break
        if len(set(uscislo)) != 4 or not uscislo.isnumeric():
            print('Input is not numeric, contain duplicity or is not 4 digits long.')
            continue
        ucislo=list(uscislo)
        steps += 1
        result=count_result(ucislo, pnum)
        print(result['bulls'], 'bulls' if result['bulls'] != 1 else 'bull', ',',
              result['cows'], 'cows' if  result['cows'] != 1 else 'cow', '\n' + oddelovac + '\n', end='')
    else:
        print("Correct, you've guessed the right number\nin " + str(steps) + ' guesses!\n' + oddelovac)

import random
oddelovac='-' * 48
konec = False
#
welcome_gamer()
while not konec:
    pcislo = generate_number()
    user_guessing(pcislo)
else:
    print('Good bye player, see you soon again.')
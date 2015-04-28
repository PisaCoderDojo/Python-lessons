import random

randomNum = random.randrange(1,11)

for i in range(0,6):
    print('tentativo numero '+str(i))
    inputNum = int(input())
    if (randomNum==inputNum):
        print('indovinato!')
        break
    else:
        print('sbagliato, riprova..')

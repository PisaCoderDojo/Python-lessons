import random

numero_random = random.randrange(1, 10000)

for tentativo in range(0, 100):
    print ('tentativo numero ' + str(tentativo))

    striga_inserita = input()
    numero_inserito = int(striga_inserita)

    if numero_inserito > numero_random:
        print ('troppo grande! riprova..\n')

    if numero_inserito < numero_random:
        print ('troppo piccolo! riprova..\n')

    if numero_random == numero_inserito:
        print ('indovinato!\n')
        break

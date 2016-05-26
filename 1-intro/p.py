import random

numero_random = random.randrange(1, 10)

yes = "y"
while(yes =="y"):
    for tentativo in 1, 2, 3, 4, 5:
        print ('tentativo numero ' + str(tentativo))

        striga_inserita = input('inserisci il numero ')
        numero_inserito = int(striga_inserita)

        if numero_random == numero_inserito:
            print ('indovinato!\n')
            break
        else:
            print('sbagliato, riprova...\n')
    yes = input("Vuoi fare un'altra partita ? (y,n)")

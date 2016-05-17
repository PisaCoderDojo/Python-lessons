import random

# Far decidere al giocare l’intervallo dei numeri da indovinare.
# richiede conoscenza liste

min_input = input("Inserisci il  numero minimo ")
max_input = input("Inserisci il  numero massimo ")

numero_random = random.randrange(int(min_input), int(max_input))

print("Ho scelto un numero a caso tra "+min_input+ " e "+ max_input)

ripeti_gioco = True

while(ripeti_gioco==True):
    for tentativo in 1, 2, 3, 4, 5:
        print ('tentativo numero ' + str(tentativo))

        striga_inserita = input('inserisci il numero ')
        numero_inserito = int(striga_inserita)

        if numero_random == numero_inserito:
            print ('indovinato!\n')
            break
        else:
            print('sbagliato, riprova...\n')

    scelta = input("Vuoi fare un'altra partita ? (y,n) ")
    if scelta == 'n':
        ripeti_gioco = False
    else:
        ripeti_gioco = True

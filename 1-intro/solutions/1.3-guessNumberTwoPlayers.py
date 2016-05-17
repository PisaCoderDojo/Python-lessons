import random

# Far decidere al giocare l’intervallo dei numeri da indovinare.
# richiede conoscenza liste

ripeti_gioco = True

while(ripeti_gioco==True):
    min_input = input("Inserisci il  numero minimo ")
    max_input = input("Inserisci il  numero massimo ")

    numero_random  = input("[Giocatore 1] \ninserisci il numero tra ["+min_input +" "+max_input+" ], che Giocatore 2 deve indovinare ")
    numero_random = int(numero_random)
    print("\n"*100)

    print("[Giocatore 2] \nindovina il numero scelto dal giocatore 1 tra ["+min_input +" "+max_input+" ]")

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

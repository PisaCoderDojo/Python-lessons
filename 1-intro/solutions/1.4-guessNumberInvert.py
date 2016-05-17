import random

# invertire la modalità di gioco, l'utente definisce il numero ed il
# computer cerca di indovinarlo.

ripeti_gioco = True

while(ripeti_gioco==True):
    min_input = int(input("Inserisci il  numero minimo "))
    max_input = int(input("Inserisci il  numero massimo (escluso) "))

    numero_random  = input("[utente] inserisci il numero tra ["+ str(min_input) +" "+str(max_input)+"], che il computer deve indovinare ")
    tentativi =  input("[utente] inserisci il numero massimo di tentativi possibili per il computer ")
    numero_random = int(numero_random)
    tentativi = int(tentativi)

    spazio_valori = list(range(min_input, max_input))  # create a list of values containing the numbers in the range.

    for tentativo in range(tentativi):
        input('[utente] premi invio per prossimo tentativo al copmuter')
        print ('[pc] tentativo numero ' + str(tentativo))
        random_position = random.randint(0 , len(spazio_valori) - 1)  ## ATTENZIONE: len() -1
        numero = spazio_valori.pop(random_position)
        if numero_random == numero:
            print ('Il computer ha indovinato!\n')
            break
        else:
            print('sbagliato, riprova...\n')

    scelta = input("Vuoi fare un'altra partita ? (y,n) ")
    if scelta == 'n':
        ripeti_gioco = False
    else:
        ripeti_gioco = True

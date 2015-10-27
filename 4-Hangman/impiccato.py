import random
IMPICCATO_IMG = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

PAROLE = ['coniglio','rana','abecedario','mela','farfalla']

# ritorna una parola random dalla lista di parole
def getParolaRandom(listaParole):
    index = random.randint(0, len(listaParole) - 1)
    return listaParole[index]

# stanpa l'impiccato e le lettere giuste e sbagliate
def stampaImpiccato(impiccatoImg, lettereSbagliate, lettereCorrette, parolaSegreta):
    print(impiccatoImg[len(lettereSbagliate)])
    print()

    # stampa le lettere sbagliate
    print('Lettere Sbagliate:', end=' ')
    for lettera in lettereSbagliate:
        print(lettera, end=' ')
    print()

    spazi = []
    #costruise la lista degli spazi inserendo o la lettera indovinata o un trattino
    for i in range(len(parolaSegreta)):
        if parolaSegreta[i] in lettereCorrette:
            spazi.append(parolaSegreta[i])
        else:
            spazi.append('_')

    #stampa la lista degli spazi a schermo
    for lettere in spazi:
        print(lettere, end=' ')
    print()

# ritorna la lettera scelta dall'utente, controlando che l'input sia valido
def getLettera(lettereUsate):
    while True:
        print('Indovina una lettera.')
        lettera = input()
        lettera = lettera.lower() # trasformiamo la lettera in minuscolo
        if len(lettera) != 1:
            print('Inserisci una singola lettera.')
        elif lettera in lettereUsate:
            print('Hai già provato questa lettera.')
        elif lettera not in 'abcdefghijklmnopqrstuvwxyz':
            print('Inserisci una LETTERA.')
        else:
            return lettera

# Questa funzione ritorna True se l'utente vuole giocare ancora, altrimenti False
def giocaAncora():
    print('Vuoi giocare ancora? (si/no)')
    return input().lower() == 'si'

# ritorna True se il giocatore ha vinto e False altrimenti
def controllaVittoria(parolaSegreta, lettereCorrette):
    vittoria = True
    print(parolaSegreta)
    for i in range(len(parolaSegreta)):
        if parolaSegreta[i] not in lettereCorrette:
            vittoria = False
            break
    return vittoria

print('I M P I C C A T O')
lettereSbagliate = []
lettereCorrette = []
parolaSegreta = getParolaRandom(PAROLE)
giocoFinito = False

while True:
    stampaImpiccato(IMPICCATO_IMG, lettereSbagliate, lettereCorrette, parolaSegreta)

    # fai scrivere la lettera da indovinare all'utente
    lettera = getLettera(lettereSbagliate + lettereCorrette)

    # controlla se la lettera è giusta o no
    if lettera in parolaSegreta:
        lettereCorrette.append(lettera)

        # controlla se il giocatore ha vinto
        vittoria = controllaVittoria(parolaSegreta,lettereCorrette)
        if vittoria:
            print('La parola segreta è "' + parolaSegreta + '"! Hai vinto!')
            giocoFinito = True
    else:
        lettereSbagliate.append(lettera)

        # controlla se il giocatore ha perso
        if len(lettereSbagliate) == len(IMPICCATO_IMG) - 1:
            stampaImpiccato(IMPICCATO_IMG, lettereSbagliate, lettereCorrette, parolaSegreta)
            print('Hai finito le possibilità!\nDopo ' + str(len(lettereSbagliate)) + ' lettere sbagliate e ' + str(len(lettereCorrette)) + ' lettere corrette, la parola segreta era "' + parolaSegreta + '"')
            giocoFinito = True

    # se il gioco è finito chiedi se vuole giocare ancora
    if giocoFinito:
        if giocaAncora():
            lettereSbagliate = []
            lettereCorrette = []
            giocoFinito = False
            parolaSegreta = getParolaRandom(PAROLE)
        else:
            break

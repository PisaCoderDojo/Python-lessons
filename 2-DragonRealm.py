import random
import time

def intro():
    print('Ti trovi in una terra piena di draghi. Di fronte a te,')
    print('vedi due caverne. In una il drago è amichevole')
    print('e ti darà i suoi tesori, nell\'altra il drago')
    print('è avido e cattivo, e ti mangerà non appena ti vedrà.')

def scegliNumeroCaverna():
    caverna=''
    while caverna!='1' and caverna!='2':
        print ('In quale caverna vuoi entrare? (1 o 2)')
        caverna = input()
    return caverna

def controllaCaverna(numCaverna):
    print('Ti avvicini alla caverna...')
    time.sleep(2)
    print('E\' scura e spaventosa...')
    time.sleep(2)
    print('Un grande drago salta fuori di fronte a te! Apre le sue fauci e...')
    time.sleep(2)

    rand = random.randrange(1,3)

    if (str(rand) == numCaverna):
        print('ti da il suo tesoro!')
    else:
        print('ti mangia in un sol boccone!')


continua='yes'
while continua=='yes' or continua=='y':

    intro()

    numCaverna = scegliNumeroCaverna()

    controllaCaverna(numCaverna)

    print('Vuoi giocare ancora?')
    continua = input()

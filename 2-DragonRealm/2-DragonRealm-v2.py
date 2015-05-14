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
    print('\nTi avvicini alla caverna...', end='')
    time.sleep(2)
    print('\rE\' scura e spaventosa...  ',end='')
    time.sleep(2)
    print('\rUn grande drago salta fuori di fronte a te! Apre le sue fauci e...',end='')
    time.sleep(2)

    rand = random.randrange(1,3)

    if (str(rand) == numCaverna):
        print('\rti da il suo tesoro!                                              ')
    else:
        print('\rti mangia in un sol boccone!                                      ')
    print()


continua='yes'
while continua=='yes' or continua=='y':

    intro()

    numCaverna = scegliNumeroCaverna()

    controllaCaverna(numCaverna)

    print('Vuoi giocare ancora?')
    continua = input()

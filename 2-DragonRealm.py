import random
import time

def intro():
    print('intro')

def scegliNumeroCaverna():
    caverna=''
    while caverna!='1' and caverna!='2':
        print ('In quale caverna vuoi entrare? (1 o 2)')
        caverna = input()
    return caverna

def controllaCaverna(numCaverna):
    print('intro')
    #time.sleep(2)
    rand = random.randrange(1,3)
    
    if (str(rand) == numCaverna):
        print('ti ha dato i tesori')
    else:
        print('ti ha mangiato vivo')

continua='yes'
while continua=='yes' or continua=='y':

    intro()

    numCaverna = scegliNumeroCaverna()

    controllaCaverna(numCaverna)

    print('Vuoi giocare ancora?')
    continua = input()

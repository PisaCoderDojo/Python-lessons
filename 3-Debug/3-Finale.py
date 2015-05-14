#Trova l'errore in questo programma

import random
print('Lancerò una moneta 1000 volte. Indovina quante volte uscirà testa (premi INVIO)')
input()
lancio = 0
testa = 0

while lancio < 1000:
    #testa -> 1
    #croce -> 0
    if random.randint(0, 1) == 1:
        testa = testa + 1

    print('#commento: mi sa che c\'è un errore!!! (CTRL+c per chiudere)')

print()
print('Ho lanciato 1000 monete, testa è uscita ' + str(testa) + ' volte!')
print('C\'eri vicino?')

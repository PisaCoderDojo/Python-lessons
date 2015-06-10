#Trova l'errore in questo programma

import random
print('testa o croce?\n0 -> testa\n1 -> croce')
risp = input()

# 0 -> testa
# 1 -> croce
moneta = str(random.randint(0,1))

if (risp == moneta):
    print ('Hai vinto! è uscito ' + moneta)
else:
    print ('Hai perso! è uscito ' + moneta)

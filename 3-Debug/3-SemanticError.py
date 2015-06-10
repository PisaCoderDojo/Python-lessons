#Trova l'errore in queto programma

import random

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)

print('Quant\'è ' + str(number1) + ' + ' + str(number2) + '?')

answer = input()

if int(answer) == number1 + number2:
    print('Corretto!')
else:
    print('No! La risposta giusta è ' + str(number1 + number2))

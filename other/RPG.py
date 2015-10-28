import random

enemyHPTOT = 30
meHPTOT = 100

enemyHP = 30
meHP = 100

def printHp():
    print ("HP [", end='')
    for i in range(0,meHP,5):
        print ("|", end='')
    for i in range (meHP,meHPTOT,5):
        print (" ", end='')
    print ("]", end='')

    print ("\t\t\t\t", end='')

    print ("HP [", end='')
    for i in range(0,enemyHP,5):
        print ("|", end='')
    for i in range (enemyHP,enemyHPTOT,5):
        print (" ", end='')
    print ("]", end='')

print ("Me \t\t\t\t Enemy")
print ("action:\n\t-1 attack\n\t -2 life")
printHp()

while enemyHP >= 0 and meHP >= 0:

    action = int(input())

    if action==1:
        enemyHP = enemyHP -10
    else:
        meHP = meHP +50

    damage = random.randrange(20,50)
    meHP = meHP - damage

    printHp()

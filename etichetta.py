#Trova l'errore in questo programma
import math
def stampaEtichetta(nome):
    length = len(nome)+10
    printLine(' ','-','\n|',length)
    printLine(' ',5,'')
    print(nome,end='')
    printLine(' ',5,'|\n')
    printLine('-',length,'\n')

def printLine(first,s,end,num):
    print(first,end='')
    for i in range(0,num):
        print(s,end='')
    print(end,end='')

print('Generatore di etichete. Qual\'è il tuo nome?')
inp=input()
stampaEtichetta(inp)

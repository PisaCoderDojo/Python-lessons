import math

print('C I F R A R I O    D I    C E S A R E   v.2')
print('1 per criptare\n2 per decriptare')

key = None
while key != str(1) and key != str(2):
    key = input()

instr=input('inserisci la scriga...')
outstr=''

char = [ chr(x) for x in range(ord('A'),ord('Z')+1) ] + [ chr(x) for x in range(ord('a'),ord('z')+1) ]
nChar = len(char)-1

for l in instr:
    if key==str(1):
        pos = char.index(l)+2
    elif key==str(2):
        pos = char.index(l)-2

    if pos>nChar:
        pos-=nChar+1
    if pos<0:
        pos+=nChar+1
    outstr+=char[pos]
print(outstr)

import math

print('C I F R A R I O    D I    C E S A R E   v.1')
print('1 per criptare\n2 per decriptare')

key = None
while key != str(1) and key != str(2):
    key = input()

instr=input('inserisci la scriga...')
outstr=''

for l in instr:
    if key==str(1):
        outstr+=chr(math.floor( ((ord(l)+2-ord('A')) % (ord('z')-ord('A'))) + ord('A') ) )
    elif key==str(2):
        outstr+=chr(math.floor( ((ord(l)-2-ord('A')) % (ord('z')-ord('A'))) + ord('A') ) )

print(outstr)

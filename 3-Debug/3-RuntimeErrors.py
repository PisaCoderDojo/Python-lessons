#Trova l'errore in questo programma

def scriviNome():
    print('il tuo nome è '+nome)

def leggiNome():
    tuoNome = input('scrivi il tuo nome... ')
    scriviNome()

leggiNome()

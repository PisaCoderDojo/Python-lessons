import sys
import pygame
from random import randint

# Inizializzazione del motore grafico PyGame
pygame.init()
clock = pygame.time.Clock()

# Creazione della finestra in cui il programma verrà visualizzato
pygame.display.set_caption("Acchiappa la Talpa")
dimScreen = LARGHEZZA, ALTEZZA = 800, 600
screen = pygame.display.set_mode(dimScreen)

sfondo = pygame.image.load("erba.jpg")
talpa = pygame.image.load("talpa.png")
talpaRect = talpa.get_rect()
font = pygame.font.SysFont('Calibri', 25, True, False)

LARGHEZZA_TALPA = 100
ALTEZZA_TALPA = 75
tempoPrec = 0

colpita = 0
mancata = 0

# Ripeti fino a quando l'untente non esce e ad ogni iterazione
# genera un nuovo fotogramma da disegnare all'interno della finestra.
while True:
    # Gestore delle azioni dell'utente
    for event in pygame.event.get():
        # Se l'utente clicca il bottone chiudi sulla finestra
        if event.type == pygame.QUIT:
            pygame.quit()   # Chiudi la finestra di PyGame
            exit(0)         # Interrompi il programma python
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if talpaRect.collidepoint(pos):
                print('presa! punteggio: ' + str(colpita))
            else:
                print('mancata! punteggio: ' + str(mancata))

    screen.blit(sfondo, (0, 0))

    millisecondi = pygame.time.get_ticks()
    if millisecondi - tempoPrec > 700:
        talpaRect.x = randint(0, LARGHEZZA - 100 + 1)
        talpaRect.y = randint(0, ALTEZZA - 75 + 1)
        tempoPrec = millisecondi

    screen.blit(talpa, talpaRect)

    colpiteText = font.render('colpite: '+str(colpita), True, (255,255,255))
    mancateText = font.render('mancate: '+str(mancata), True, (255,255,255))
    screen.blit(colpiteText, (0,10))
    # Aggiorna lo schermo con tutto quello che è stato disegnato.
    # Questo comando DEVE essere eseguito dopo i comandi di disegno.
    pygame.display.flip()
    clock.tick(60)

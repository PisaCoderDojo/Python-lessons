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

font = pygame.font.SysFont('Calibri', 25, False, False)

# Ripeti fino a quando l'untente non esce e ad ogni iterazione
# genera un nuovo fotogramma da disegnare all'interno della finestra.
while True:
    # Gestore delle azioni dell'utente
    for event in pygame.event.get():
        # Se l'utente clicca il bottone chiudi sulla finestra
        if event.type == pygame.QUIT:
            pygame.quit()   # Chiudi la finestra di PyGame
            exit(0)         # Interrompi il programma python

    # Aggiorna lo schermo con tutto quello che è stato disegnato.
    # Questo comando DEVE essere eseguito dopo i comandi di disegno.
    pygame.display.flip()
    clock.tick(60)

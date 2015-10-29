import sys
import pygame
from random import randint
from math import floor

# Inizializzazione del motore grafico PyGame
pygame.init()
clock = pygame.time.Clock()

# Creazione della finestra in cui il programma verrà visualizzato
pygame.display.set_caption("Prendi la talpa")
dimScreen = LARGHEZZA, ALTEZZA = 800, 600
screen = pygame.display.set_mode(dimScreen)

# Definizione di alcuni colori
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Definizione delle constanti per le dimenzioni o le posizioni degli ogetti
# da sisegnare a schermo
TALPA_DIM = 111
COLPITE_POS = (10, 10)
MANCATE_POS = (10, 25)
BARRA_POS_X = 115
BARRA_COLPITE_Y = 17
BARRA_MANCATE_Y = 32

# Creazione degli oggetti grafici da animare a schermo
talpaImg = pygame.image.load("talpa.png")
talpa = talpaImg.get_rect()
sfondoImg = pygame.image.load("erba.jpg")
# font, dimensione, grassetto, corsivo
font = pygame.font.SysFont('Calibri', 25, False, False)

# Variabili per gestire le animazioni
tempo = 0
colpite, mancate = 0, 0

# Ripeti fino a quando l'untente non esce e ad ogni iterazione
# genera un nuovo fotogramma da disegnare a all'interno della finestra.
while True:
    # Gestore delle azioni dell'utente
    for event in pygame.event.get():
        # Se l'utente clicca il bottone chiudi sulla finestra
        if event.type == pygame.QUIT:
            pygame.quit()   # Chiudi la finestra di PyGame
            exit(0)         # Interrompi il programma python
        # Se l'utente clicca con il mouse all'interno della finestra di gioco
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position on the mouse click on the screem
            pos = pygame.mouse.get_pos()   # rileva posizione del click (x,y)
            if talpa.collidepoint(pos):
                colpite += 1    # la talpa è stata colpita
            else:
                mancate += 1    # la talpa non è stata colpita

    # verifica che siamo passati almeno 600 millisecondi (0.6 secondi)
    if pygame.time.get_ticks() - tempo > 600:
        # sposta la talpa in una posizione casuale
        talpa.x = randint(0, LARGHEZZA - TALPA_DIM)
        talpa.y = randint(0, ALTEZZA - TALPA_DIM)
        tempo = pygame.time.get_ticks()

    # Genera un'immagine dal testo specificato, questa non viene però ancora
    # aggiunta alla shermo. "True" per attivare anti-aliased del testo.
    colpiteTesto = font.render("Colpite:   " + str(colpite), True, BLACK)
    mancateTesto = font.render("Mancate: " + str(mancate), True, BLACK)
    fpsText = font.render("fps: " + str(floor(clock.get_fps())), True, WHITE)

    # Sovrapponiamo tutti gli elementi grafici creati fino ad ora sullo schermo
    # per creare il fotogramma finale. Qui l'ordine è importante, gli oggetti
    # eseguiti per prima vengono messi sulo sfondo
    screen.blit(sfondoImg, (0, 0))
    screen.blit(talpaImg, talpa)
    screen.blit(colpiteTesto, COLPITE_POS)
    screen.blit(mancateTesto, MANCATE_POS)
    screen.blit(fpsText, (LARGHEZZA - 70, ALTEZZA - 20))

    # Aggiungiamo allo schermo delle linee di 10px di altezza per rappresentare
    # le talpe colpite o mancate.
    if(colpite > 0):
        pygame.draw.line(screen,  # schermo su cui disegnare la linea
                         GREEN,   # il colore della linea
                         (BARRA_POS_X, BARRA_COLPITE_Y),               # inizio
                         (BARRA_POS_X + colpite * 10, BARRA_COLPITE_Y),  # fine
                         10)      # spessore in pixel
    if(mancate > 0):
        pygame.draw.line(screen,  # schermo su cui disegnare la linea
                         RED,    # colore della linea
                         (BARRA_POS_X, BARRA_MANCATE_Y),               # inizio
                         (BARRA_POS_X + mancate * 10, BARRA_MANCATE_Y),  # fine
                         10)     # spessore in pixel

    # Aggiorna lo schermo con tutto quello che è stato disegnato.
    # Questo comando DEVE essere eseguito dopo i comandi di disegno.
    pygame.display.flip()
    clock.tick(60)

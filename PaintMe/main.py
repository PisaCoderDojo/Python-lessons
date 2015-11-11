import sys
import pygame

# Inizializzazione del motore grafico PyGame
pygame.init()
clock = pygame.time.Clock()

# Creazione della finestra in cui il programma verrà visualizzato
pygame.display.set_caption("Pain Me")
dimScreen = LARGHEZZA, ALTEZZA = 800, 600
screen = pygame.display.set_mode(dimScreen)

# Definizione di alcuni colori
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# font, dimensione, grassetto, corsivo
font = pygame.font.SysFont('Calibri', 25, False, False)
mouse = pygame.mouse
canvas = screen.copy()
canvas.fill(WHITE)

redTxt = font.render("rosso", True, WHITE)
redRect = pygame.Rect(0, 0, 60, 30)

greenTxt = font.render("verde", True, WHITE)
greenRect = pygame.Rect(65, 0, 60, 30)

blackTxt = font.render("nero", True, WHITE)
blackRect = pygame.Rect(130, 0, 60, 30)

# Variabili per gestire le animazioni
tempo = 0
colorePenna = BLACK
mousePosVecchia = None

SPESSORE_LINEA = 8
SPESSORE_PUNTO = 3
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

    click_sinistro, click_centrale, click_destro = mouse.get_pressed()
    if click_sinistro:
        mousePos = mouse.get_pos()
        if redRect.collidepoint(mousePos):
            colorePenna = RED
        elif greenRect.collidepoint(mousePos):
            colorePenna = GREEN
        elif blackRect.collidepoint(mousePos):
            colorePenna = BLACK
        else:
            pygame.draw.circle(canvas, colorePenna, mousePos, SPESSORE_PUNTO)
            if mousePosVecchia != None:
                pygame.draw.line(canvas, colorePenna, mousePosVecchia, mousePos, SPESSORE_LINEA)
            mousePosVecchia = mousePos
    else:
        mousePosVecchia = None

    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))
    pygame.draw.circle(screen, colorePenna, (mouse.get_pos()), SPESSORE_PUNTO)
    pygame.draw.rect(screen, RED, redRect, 0)
    screen.blit(redTxt, redRect.topleft)
    pygame.draw.rect(screen, BLACK, blackRect, 0)
    screen.blit(blackTxt, blackRect.topleft)
    pygame.draw.rect(screen, GREEN, greenRect, 0)
    screen.blit(greenTxt, greenRect.topleft)

    # Aggiorna lo schermo con tutto quello che è stato disegnato.
    # Questo comando DEVE essere eseguito dopo i comandi di disegno.
    pygame.display.flip()
    clock.tick(60)

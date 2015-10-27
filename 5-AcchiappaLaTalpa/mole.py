import sys
import pygame
from random import randint

# Initialize  the game engine
pygame.init()
clock = pygame.time.Clock()

# initialize the height and width of the screen
pygame.display.set_caption("Prendi la talpa")
dimScreen = LARGHEZZA, ALTEZZA = 800, 600
screen = pygame.display.set_mode(dimScreen)

# Define some colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

TALPA_DIM = 111
COLPITE_POS = [10, 10]
MANCATE_POS = [10, 25]
BARRA_POS_X = 115
BARRA_COLPITE_Y = 17
BARRA_MANCATE_Y = 32

talpaImg = pygame.image.load("talpa.png")
talpa = talpaImg.get_rect()
sfondoImg = pygame.image.load("erba.jpg")
# Select the font to use, size, bold, italics
font = pygame.font.SysFont('Calibri', 25, False, False)

tempo = 0
colpite, mancate = 0, 0


# Loop until the user clicks the close button.
while True:
    for event in pygame.event.get():      # User did something
        if event.type == pygame.QUIT:     # If user clicked close
            pygame.quit()  # Be IDLE friendly
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position on the mouse click on the screem
            pos = pygame.mouse.get_pos()
            if talpa.collidepoint(pos):
                colpite += 1
            else:
                mancate += 1

    if pygame.time.get_ticks() - tempo > 600:
        talpa.x = randint(0, LARGHEZZA - TALPA_DIM)
        talpa.y = randint(0, ALTEZZA - TALPA_DIM)
        tempo = pygame.time.get_ticks()

    # Render the text. "True" means anti-aliased text. This creates an image
    # of the letters, but does not put it on the screen
    colpiteTesto = font.render("Colpite:   " + str(colpite), True, BLACK)
    mancateTesto = font.render("Mancate: " + str(mancate), True, BLACK)

    screen.blit(sfondoImg, (0, 0))
    screen.blit(talpaImg, talpa)
    screen.blit(colpiteTesto, COLPITE_POS)
    screen.blit(mancateTesto, MANCATE_POS)

    # Draw on the screen  line for hit and miss points, 10 pixels wide each.
    if(colpite > 0):  # green line hit
        pygame.draw.line(screen, GREEN, [BARRA_POS_X, BARRA_COLPITE_Y],
                         [BARRA_POS_X + colpite * 10, BARRA_COLPITE_Y], 10)
    if(mancate > 0):  # red line miss
        pygame.draw.line(screen, RED, [BARRA_POS_X, BARRA_MANCATE_Y],
                         [BARRA_POS_X + mancate * 10, BARRA_MANCATE_Y], 10)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
    clock.tick(60)

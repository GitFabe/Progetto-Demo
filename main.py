import pygame
import sys

#inizializza moduli tutti di Pygame
pygame.init()

#def dimensioni ioco
dimensione = (800, 600)

#crea finestra
finestra = pygame.display.set_mode(dimensione)

#modulo display

#imposta titolo
pygame.display.set_caption("Test 1")

#def colore
sfondo_colore = (150, 150, 250)

#loop del gioco
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    finestra.fill(sfondo_colore)

    pygame.display.update()

    


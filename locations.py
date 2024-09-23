
import pygame
import sys

pygame.init()

#loop del gioco
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    finestra.fill(sfondo_colore)

    pygame.display.update()
     
    screen = pygame.display.set_mode((800, 600))
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0,0,0), (400, 300), 5)

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

    pygame.draw.rect(screen, (127, 0, 255), (100, 100), (40, 20))

#mettere poi update in fondo

    pygame.draw.line((0, 0, 0), (100, 400), (700,400), 5)
    pygame.draw.polygon(screen, (0,0,0), [(300, 200), (400,150), (200,400)])
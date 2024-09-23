import pygame
pygame.init()

clock = pygame.time.Clock()
resolution = (800,600)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Gioco Demo')

running = True



while running:
    rgbColor = (255,255,255)
    screen.fill(rgbColor)
    #faccia
    pygame.draw.circle(screen, (0,0,0), (400,300), 100, 5)
    #occhi
    pygame.draw.circle(screen, (50,50,50), (450,275), 15, 3)
    pygame.draw.circle(screen, (50,50,50), (350,275), 15, 3)
    #bocca
    pygame.draw.rect(screen, (127,0,255), (365,350, 65,15), 5)
    #naso
    pygame.draw.line(screen, "black", (400, 275), (375,325), 5)
    pygame.draw.line(screen, "black", (425, 325), (375,325), 4)
    #cappello
    pygame.draw.polygon(screen, (0,0,0), [(275, 225), (400,180), (525,225)])

    #caricamento immagini
    

    #scalare

    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Hai cliccato fra")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            print("Hai premuto tastiera fra")

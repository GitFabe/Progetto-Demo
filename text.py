import pygame
pygame.init()

clock = pygame.time.Clock()
resolution = (800,600)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Gioco Demo')

running = True

#caricare font
pygame.font.Font(None,12)

#render del testo
pygame.font.Font.render(None, 'Benvenuto nel nostro gioco', True, (0, 0, 0))

while running:
    rgbColor = (255,255,255)
    screen.fill(rgbColor)

    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
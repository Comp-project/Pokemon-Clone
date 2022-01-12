import pygame
pygame.init()

lscreen = pygame.image.load('Images/LoadingScreen.png')
screen = pygame.display.set_mode((800,600))

def blitls(lscreen, screen,txt1):
    txtX = 250
    txtY = 500
    font = pygame.font.Font('PokemonGb-RAeo.ttf', 20)
    running = True
    i = 255
    x = 0
    while running:
        screen.fill((0,0,0))
        screen.blit(lscreen, (0,0))

        if i == 255:
            while i > 0:
                x += 1
                font2 = font.render(txt1, True, (255 - x, 255 - x, 255 - x))
                screen.blit(font2,(txtX,txtY))
                pygame.display.update()
                i -= 1
                if i <= 0:
                    break

        elif i == 0:
            while i < 255:
                x -= 1
                font2 = font.render(txt1, True, (255 - x, 255 - x, 255 - x))
                screen.blit(font2, (txtX, txtY))
                pygame.display.update()
                i += 1
                if i >= 255:
                    break


        for event4 in pygame.event.get():
            if event4.type == pygame.KEYDOWN:
                running = False
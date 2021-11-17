import pygame
pygame.init()

bbimg = pygame.image.load('Images/bulback.png')
sbimg = pygame.image.load('Images/sqback.png')
cbimg = pygame.image.load('Images/charback.png')
pbimg = pygame.image.load('Images/pikaback.png')
bsc = pygame.image.load('Images/BattleScreen.png')
pbsc = pygame.image.load('Images/plainbsb.png')
trback = pygame.image.load('Images/trback.png')
pikaimg = pygame.image.load('Images/pikaimg.png')
hpbars = pygame.image.load('Images/healthbars.png')
greenbars = pygame.image.load('Images/greenbar.png')
arrow = pygame.image.load('Images/arrowcursor.png')

greenbar2 = greenbars.copy()

fightstate = 1

running = True

screen = pygame.display.set_mode((800,600))

arrowcoordinatex, arrowcoordinatey = 40,520

while running:
    screen.blit(bsc, (0,0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.blit(pikaimg, (450, 60))
    screen.blit(cbimg, (75,275))
    screen.blit(pbsc, (0,450))
    font = pygame.font.Font('Raleway-Medium.ttf', 30)
    font2 = pygame.font.Font('PokemonGb-RAeo.ttf', 20)
    text4 = font2.render('Pikachu',True, (0, 0, 0))
    text5 = font2.render('Charmander', True, (0, 0, 0))
    screen.blit(hpbars, (0,0))
    screen.blit(greenbars, (165, 115))
    screen.blit(greenbar2, (601, 411))
    screen.blit(text4,(34,69))
    screen.blit(text5, (466, 372))


    if fightstate == 1:
        text1 = font.render('FIGHT', True, (0,0,0))
        text2 = font.render('HEAL', True, (0,0,0))
        text3 = font.render('RUN', True, (0,0,0))
        screen.blit(text1, (75,510))
        screen.blit(text2, (375,510))
        screen.blit(text3, (675, 510))
        screen.blit(arrow, (arrowcoordinatex,arrowcoordinatey))

        for event1 in pygame.event.get():
            if event1.type == pygame.KEYDOWN:
                if event1.key == pygame.K_RIGHT:
                    if arrowcoordinatex != 640:
                        screen.blit(arrow, (arrowcoordinatex + 300,arrowcoordinatey))
                        arrowcoordinatex += 300
                    else:
                        screen.blit(arrow, (40,arrowcoordinatey))
                        arrowcoordinatex = 40


    pygame.display.update()
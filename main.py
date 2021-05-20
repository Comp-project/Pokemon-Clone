import pygame

pygame.init()

playerimg = pygame.image.load('pokesprite1.png')
playerimgB = pygame.image.load('pokespriteB.png')
playerimgL = pygame.image.load('pokespriteL.png')
playerimgR = pygame.image.load('pokespriteR.png')
map = pygame.image.load('map.png')

playerX = 32
playerY = 352
xchange = 0

screen = pygame.display.set_mode((800,600))

def playerdisp(playerimg,playerX,playerY):
    screen.blit(playerimg, (playerX,playerY))

def mapdraw():
    screen.blit(map, (0,0))

pimg = playerimg

FPS = 2
fpsClock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            playerX += 32
            pimg = playerimgR

        elif event.key == pygame.K_LEFT:
            playerX -= 32
            pimg = playerimgL

        elif event.key == pygame.K_UP:
            playerY -= 32
            pimg = playerimgB

        elif event.key == pygame.K_DOWN:
            playerY += 32
            pimg = playerimg


    if event.type == pygame.KEYUP:
        playerY+=0
        playerX+=0

    screen.fill((0,0,0))

    mapdraw()

    playerdisp(pimg,playerX,playerY)

    pygame.display.update()
    fpsClock.tick(FPS)

#Not yet worked on creating boundaries for the image and the buildings, ponds etc. Will do that tom.
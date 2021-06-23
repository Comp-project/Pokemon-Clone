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

    pygame.key.get_pressed()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if (playerY > -33 and playerY < 97 and playerX == 256) or (playerY > 383 and playerY < 513 and playerX == 288) or playerX == 768:
                playerX += 0
            else:
                playerX += 32
                pimg = playerimgR

        elif event.key == pygame.K_LEFT:
            if (playerY > -33 and playerY < 65 and playerX == 96) or (playerY > 95 and playerY < 225 and playerX ==160) or (playerY > 383 and playerY < 513 and playerX == 640) or (playerY > 383 and playerY < 545 and playerX == 160) or playerX == -32:
                playerX += 0
            else:
                playerX -= 32
                pimg = playerimgL

        elif event.key == pygame.K_UP:
            if (playerX > -1 and playerX < 129 and playerY == 256) or (playerX > 287 and playerX < 769 and playerY == 128) or playerY == -32:                playerY += 0
            else:
                playerY -= 32
                pimg = playerimgB

        elif event.key == pygame.K_DOWN:
            if (playerX > 319 and playerX < 609 and playerY == 352) or (playerX > -33 and playerX < 129 and playerY == 352) or playerY == 544:
                playerY += 0
            else:
                playerY += 32
                pimg = playerimg


    if event.type == pygame.KEYUP:
        playerY+=0
        playerX+=0

    screen.fill((0,0,0))

    print("X = ", playerX)
    print("Y = ", playerY)

    mapdraw()

    playerdisp(pimg,playerX,playerY)

    pygame.display.update()
    fpsClock.tick(FPS)

#Not yet worked on creating boundaries for the image and the buildings, ponds etc. Will do that tom.
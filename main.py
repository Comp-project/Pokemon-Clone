import pygame
import random

pygame.init()

playerimg = pygame.image.load('pokesprite1.png')
playerimgB = pygame.image.load('pokespriteB.png')
playerimgL = pygame.image.load('pokespriteL.png')
playerimgR = pygame.image.load('pokespriteR.png')
map = pygame.image.load('map.png')
whitescreen = pygame.image.load('whitescreen.png')

playerX = 32
playerY = 352
xchange = 0

screen = pygame.display.set_mode((800,600))

def playerdisp(playerimg,playerX,playerY):
    screen.blit(playerimg, (playerX,playerY))

def mapdraw():
    screen.blit(map, (0,0))

pimg = playerimg

#FPS = 7
#fpsClock = pygame.time.Clock()

running = True
counter = 0

while running:
    if counter>0:
        counter -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t1 = (playerX,playerY)

    player_rect = pygame.Rect(playerX, playerY, playerimgR.get_width(), playerimgR.get_height())
    grass_rect = pygame.Rect(352, 224, 448, 300)


    if event.type == pygame.KEYDOWN and counter == 0:
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
            if (playerX > -1 and playerX < 129 and playerY == 256) or (playerX > 287 and playerX < 769 and playerY == 128) or playerY == -32 or (playerX > 319 and playerX <609 and playerY == 544 ):
                playerY += 0
            else:
                playerY -= 32
                pimg = playerimgB

        elif event.key == pygame.K_DOWN:
            if (playerX > 319 and playerX < 609 and playerY == 352) or (playerX > -33 and playerX < 129 and playerY == 352) or playerY == 544 or (playerX > 63 and playerX < 129 and playerY == 64):
                playerY += 0
            else:
                playerY += 32
                pimg = playerimg

        grasscv = random.randint(1, 11)


    if event.type == pygame.KEYUP:
        playerY+=0
        playerX+=0

    t2 = (playerX,playerY)

    if t1 != t2:
        counter = 12

    if player_rect.colliderect(grass_rect) and grasscv == 1 and t1 != t2:
        screen.blit(whitescreen, (0, 0))
    else:
        screen.fill((0,0,0))

        print("X = ", playerX)
        print("Y = ", playerY)

        mapdraw()

        playerdisp(pimg,playerX,playerY)

    pygame.display.update()
    #fpsClock.tick(FPS)
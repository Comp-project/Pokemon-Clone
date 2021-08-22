import pygame
import random

pygame.init()

pygame.mixer.music.load("Littleroot Town - Pokémon Omega Ruby & Alpha Sapphire Music Extended HD.wav")
pygame.mixer.music.play(-1)

playerimgf = pygame.image.load('walk front idle.png')
playerimgf1 = pygame.image.load('walk front 1.png')
playerimgf2 = pygame.image.load('walk front 2.png')
playerimgl = pygame.image.load('walk left idle.png')
playerimgl1 = pygame.image.load('walk left 1.png')
playerimgl2 = pygame.image.load('walkleft 2.png')
playerimgr = pygame.image.load('R0.png')
playerimgr1 = pygame.image.load('R1.png')
playerimgr2 = pygame.image.load('R2.png')
playerimgb = pygame.image.load('walk back idle.png')
playerimgb1 = pygame.image.load('walk back 1.png')
playerimgb2 = pygame.image.load('walk back 2.png')

batsc = pygame.image.load('BattleScreen.png')
bulbimg = pygame.image.load('bulbimg.png')
bulbsp = pygame.image.load('bulbsp.png')
pikaimg = pygame.image.load('pikaimg.png')
pikasp = pygame.image.load('pikasp.png')
charsp = pygame.image.load('charsp.png')
charimg = pygame.image.load('Charimg.png')
sqimg = pygame.image.load('sqimg.png')
sqsp = pygame.image.load('sqsp.png')
trback = pygame.image.load('trback.png')
#image of character in battle screen
bsbanner = pygame.image.load('BattleScreenBanner.png')
#says catch - c, run away - r
map = pygame.image.load('map.png')
whitescreen = pygame.image.load('whitescreen.png')

#all the images

playerX = 32
playerY = 352
xchange = 0

#inital position coordinates

screen = pygame.display.set_mode((800,600))

def playerdisp(playerimg,playerX,playerY):
    screen.blit(playerimg, (playerX,playerY))

def mapdraw():
    screen.blit(map, (0,0))

pimg = playerimgf


running = True
counter = 0

while running:
    if counter>0:
        counter -= 1
    #reducing counter. refer line 121

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t1 = (playerX,playerY)

    player_rect = pygame.Rect(playerX, playerY, playerimgf.get_width(), playerimgf.get_height())
    grass_rect = pygame.Rect(352, 224, 448, 300)


    if event.type == pygame.KEYDOWN and counter == 0:
        if event.key == pygame.K_RIGHT:
            if (playerY > -33 and playerY < 97 and playerX == 256) or (playerY > 383 and playerY < 513 and playerX == 288) or playerX == 768:
                playerX += 0
            else:
                playerX += 32
                keypressvar = "r"

                #keypressvar to choose which image to display. refer line 122

                pimg = playerimgr

            #pimg is the image it will display when the character is not moving. so i default it to the idle image at the end of the section for the particular key i have pressed


        elif event.key == pygame.K_LEFT:
            if (playerY > -33 and playerY < 65 and playerX == 96) or (playerY > 95 and playerY < 225 and playerX ==160) or (playerY > 383 and playerY < 513 and playerX == 640) or (playerY > 383 and playerY < 545 and playerX == 160) or playerX == -32:
                playerX += 0
            else:
                playerX -= 32
                keypressvar = "l"

                pimg = playerimgl

        elif event.key == pygame.K_UP:
            if (playerX > -1 and playerX < 129 and playerY == 256) or (playerX > 287 and playerX < 769 and playerY == 128) or playerY == -32 or (playerX > 319 and playerX <609 and playerY == 544 ):
                playerY += 0
            else:
                playerY -= 32
                keypressvar = "u"

                pimg = playerimgb


        elif event.key == pygame.K_DOWN:
            if (playerX > 319 and playerX < 609 and playerY == 352) or (playerX > -33 and playerX < 129 and playerY == 352) or playerY == 544 or (playerX > 63 and playerX < 129 and playerY == 64):
                playerY += 0
            else:
                playerY += 32
                keypressvar = "d"

                pimg = playerimgf

        grasscv = random.randint(1, 11)

        #grass collision variable with a 10% chance of pokemon appearance being triggered


    if event.type == pygame.KEYUP:
        playerY+=0
        playerX+=0

    t2 = (playerX,playerY)

    #t1 - initial pos, t2 - position after movement. so if these are diff counter will be set to 12, to skip 12 loops to prevent continuous movement of the character

    if t1 != t2:
        counter = 12

    if player_rect.colliderect(grass_rect) and grasscv == 1 and t1 != t2:
        #triggering pokemon encounter if character is on grass and 10% chance

        pokemon1 = random.randint(1, 4)
        #a random number to decide which pokemon shows up

        running1 = True

        while running1:

            screen.blit(batsc, (0, 0))
            screen.blit(trback,(0,180))
            screen.blit(bsbanner, (0,450))
            if pokemon1 == 1:
                screen.blit(pikaimg, (450, 60))
            elif pokemon1 == 2:
                screen.blit(charimg, (450, 60))
            elif pokemon1 == 3:
                screen.blit(sqimg, (450, 60))
            elif pokemon1 == 4:
                screen.blit(bulbimg, (450, 60))

            for event1 in pygame.event.get():
                if event1.type == pygame.KEYDOWN:
                  running1 = False
            pygame.display.update()



    else:
        screen.fill((0,0,0))

        print("X = ", playerX)
        print("Y = ", playerY)

        mapdraw()

    #So i kept it such that every time the character moves, the counter goes to 12, and it does not take input for 12 loops (to prevent continuous movement
    #So when the program is not taking input, it displays the image at the position according to the value of the counter. hope u understand

    if counter <13 and counter>9:
        if keypressvar == "r":
            playerdisp(playerimgr1, playerX - 24, playerY)
        elif keypressvar == "l":
            playerdisp(playerimgl1, playerX + 24, playerY)
        elif keypressvar == "u":
            playerdisp(playerimgb1, playerX, playerY + 24)
        elif keypressvar == "d":
            playerdisp(playerimgf1, playerX, playerY - 24)

    elif counter <10 and counter>6:
        if keypressvar == "r":
            playerdisp(playerimgr, playerX - 16, playerY)
        elif keypressvar == "l":
            playerdisp(playerimgl, playerX + 16, playerY)
        elif keypressvar == "u":
            playerdisp(playerimgb, playerX, playerY + 16)
        elif keypressvar == "d":
            playerdisp(playerimgf, playerX, playerY - 16)

    elif counter <7 and counter>3:
        if keypressvar == "r":
            playerdisp(playerimgr2, playerX - 8, playerY)
        elif keypressvar == "l":
            playerdisp(playerimgl2, playerX + 8, playerY)
        elif keypressvar == "u":
            playerdisp(playerimgb2, playerX, playerY + 8)
        elif keypressvar == "d":
            playerdisp(playerimgf2, playerX, playerY - 8)

    elif counter <4 and counter >0:
        if keypressvar == "r":
            playerdisp(playerimgr, playerX, playerY)
        elif keypressvar == "l":
            playerdisp(playerimgl, playerX, playerY)
        elif keypressvar == "u":
            playerdisp(playerimgb, playerX, playerY)
        elif keypressvar == "d":
            playerdisp(playerimgf, playerX, playerY)

    else:
        playerdisp(pimg,playerX,playerY)

    #the above is for when the counter is 0

    pygame.display.update()
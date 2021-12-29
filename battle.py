import time

import pygame
import random

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
# all the images added above

greenbar2 = pygame.image.load('Images/greenbar.png')
# duplicating health bar - one for player's health, the other for opponent

fightstate = 1
# a fight state variable - will be 1 when the fight is going on, will be 2 if player wins, will be 3 if opponent wins ( will tell more about this tomorrow)
greenbarlength = 168
running = True

playerhealth = 100
pchealth = 100
damage = -20 - (random.random() * 10) // 1
heal = +25

screen = pygame.display.set_mode((800, 600))


def pattack():
    global pchealth
    pchealth += -20 - (random.random() * 10) // 1
    if pchealth <= 0:
        pchealth = 0


def pheal():
    global playerhealth
    playerhealth += 20 + (random.random() * 10) // 1
    if playerhealth >= 100:
        playerhealth = 100


def pcattack():
    global playerhealth
    playerhealth += -20 - (random.random() * 10) // 1
    if playerhealth <= 0:
        playerhealth = 0


def pcheal():
    global pchealth
    pchealth += 20 + (random.random() * 10) // 1
    if pchealth >= 100:
        pchealth = 100

catchvar = -1

# functions we made yesterday in school

arrowcoordinatex, arrowcoordinatey = 40, 520
# coordinates of the arrow cursor to navigate between options)

while running:

    bannertextvar = True

    temppch, tempplh, playerdamagedealt, pcdamagedealt, playerheal, pchealed = 0, 0, 0, 0, 0, 0

    # health variables used to calculate stuff like damage dealt or healed by player and opponent per round

    screen.blit(bsc, (0, 0))

    screen.blit(pikaimg, (450, 60))
    screen.blit(cbimg, (75, 275))
    screen.blit(pbsc, (0, 450))
    font = pygame.font.Font('Raleway-Medium.ttf', 30)
    font2 = pygame.font.Font('PokemonGb-RAeo.ttf', 20)
    text4 = font2.render('Pikachu', True, (0, 0, 0))
    text5 = font2.render('Charmander', True, (0, 0, 0))
    screen.blit(hpbars, (0, 0))
    screen.blit(greenbars, (165, 115))
    screen.blit(greenbar2, (601, 411))
    screen.blit(text4, (34, 77))
    screen.blit(text5, (466, 372))

    ph1 = playerhealth
    pch1 = pchealth

    # below code is for showing stuff like pokemon fainted after HP of one pokemon reaches 0
    if pchealth == 0:
        while True:
            screen.blit(bsc, (0, 0))
            screen.blit(cbimg, (75, 275))
            screen.blit(pbsc, (0, 450))
            screen.blit(hpbars, (0, 0))
            screen.blit(greenbars, (165, 115))
            screen.blit(greenbar2, (601, 411))
            if catchvar == -1:
                text8 = font2.render('The wild Pikachu fainted!', True, (0, 0, 0))
            elif catchvar == 1:
                text8 = font2.render('The wild Pikachu escaped!', True, (0,0,0))
            elif catchvar == 0:
                text8 = font2.render('You caught the wild Pikachu', True, (0,0,0))
            screen.blit(text8, (40, 505))
            pygame.display.update()

    elif playerhealth == 0:
        while True:
            screen.blit(bsc, (0, 0))
            screen.blit(pikaimg, (450, 60))
            screen.blit(pbsc, (0, 450))
            screen.blit(hpbars, (0, 0))
            screen.blit(greenbars, (165, 115))
            screen.blit(greenbar2, (601, 411))
            text8 = font2.render('Charmander fainted!', True, (0, 0, 0))
            screen.blit(text8, (40, 505))
            pygame.display.update()

    # 2 variables for the initial values of health, used later for health bar

    if fightstate == 1:
        text1 = font.render('FIGHT', True, (0, 0, 0))
        text2 = font.render('HEAL', True, (0, 0, 0))
        text3 = font.render('RUN', True, (0, 0, 0))
        screen.blit(text1, (75, 510))
        screen.blit(text2, (375, 510))
        screen.blit(text3, (675, 510))
        screen.blit(arrow, (arrowcoordinatex, arrowcoordinatey))

    for event1 in pygame.event.get():

        if event1.type == pygame.QUIT:
            running = False

        if event1.type == pygame.KEYDOWN:
            if event1.key == pygame.K_RIGHT:

                # code for controlling the cursor

                if arrowcoordinatex != 640:
                    screen.blit(arrow, (arrowcoordinatex + 300, arrowcoordinatey))
                    arrowcoordinatex += 300
                else:
                    screen.blit(arrow, (40, arrowcoordinatey))
                    arrowcoordinatex = 40

            if event1.key == pygame.K_a:

                if arrowcoordinatex == 40:

                    # the following will execute if the cursor is in the first position, ie the x coordinate is 40

                    pattack()

                    playerdamagedealt = str(pch1 - pchealth)
                    temppch = pchealth

                    pcmovedetermine = random.random()

                    # pcmovedetermine is a random.random function to determine whether the pc will heal or attack

                    if pcmovedetermine > 0.5:

                        pcattack()

                        pcdamagedealt = str(ph1 - playerhealth)

                        # pcdamagedealt, pcdamagehealed, playerdamagedealt, playerdamagehealed, temppch, tempplh are all variables for calculating how much damage has been dealt or healed per round

                    else:
                        pcheal()

                        pchealed = str(pchealth - temppch)

                if arrowcoordinatex == 340:
                    pheal()

                    tempplh = playerhealth

                    playerheal = str(playerhealth - ph1)

                    pcmovedetermine = random.random()

                    if pcmovedetermine > 0.5:
                        pcattack()

                        pcdamagedealt = str(tempplh - playerhealth)


                    else:
                        pcheal()

                        pchealed = str(pchealth - pch1)

            print('player', playerhealth)
            print('opponent', pchealth)

            if event1.key == pygame.K_c:

                pchealth_roundedoff = round(pchealth/10)
                percentagecatch = 10-pchealth_roundedoff
                pokecatchsuccess = random.randint(1,11)
                if pokecatchsuccess <= percentagecatch:
                    print('Caught successfully')
                    catchvar = 0
                    pchealth = 0
                else:
                    print('Catch unsuccessful')
                    catchvar = 1
                    pchealth = 0




    # the below line is to only show damage dealt or healed per round if a move has taken place. ie it will not display shit like 0 health healed and 0 damage dealth

    if temppch != 0 or tempplh != 0:
        screen.blit(pbsc, (0, 450))

        if tempplh == 0:
            text6 = 'You dealt {} HP worth of damage.'.format(playerdamagedealt)

            if pcmovedetermine > 0.5:
                text7 = 'The opponent dealt {} HP worth of damage to you.'.format(pcdamagedealt)
            else:
                text7 = 'The opponent healed {} HP.'.format(pchealed)

        else:
            text6 = 'You healed {} HP'.format(playerheal)

            if pcmovedetermine > 0.5:
                text7 = 'The opponent dealt {} HP worth of damage to you.'.format(pcdamagedealt)
            else:
                text7 = 'The opponent healed {} HP.'.format(pchealed)

        blittext6 = font2.render(text6, True, (0, 0, 0))
        blittext7 = font2.render(text7, True, (0, 0, 0))

        while True:
            screen.blit(blittext6, (40, 478))
            screen.blit(blittext7, (40, 544))

            pygame.display.update()
            for event2 in pygame.event.get():
                if event2.type == pygame.KEYDOWN:
                    bannertextvar = False
                    break

            if not bannertextvar:
                break

    # below lines of code is to blit the HP and healthbars

    playerhpprint = font2.render('{}/100'.format(str(playerhealth)), True, (0, 0, 0))
    pchpprint = font2.render('{}/100'.format(str(pchealth)), True, (0, 0, 0))
    screen.blit(playerhpprint, (610, 440))
    screen.blit(pchpprint, (220, 77))
    greenbars = pygame.transform.scale(greenbars, ((pchealth / 100) * 168, 16))
    greenbar2 = pygame.transform.scale(greenbar2, ((playerhealth / 100) * 168, 16))

    # above code is for controlling the cursor arrow

    pygame.display.update()

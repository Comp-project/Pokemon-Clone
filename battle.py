import pygame
import random
import pickle

pygame.init()

bbimg = pygame.image.load('Images/bulback.png')
sbimg = pygame.image.load('Images/sqback.png')
cbimg = pygame.image.load('Images/charback.png')
pbimg = pygame.image.load('Images/pikaback.png')
bsc = pygame.image.load('Images/BattleScreen.png')
pbsc = pygame.image.load('Images/plainbsb.png')
trback = pygame.image.load('Images/trback.png')

pikaimg = pygame.image.load('Images/pikaimg.png')
bulbimg = pygame.image.load('Images/bulbimg.png')
charimg = pygame.image.load('Images/Charimg.png')
sqimg = pygame.image.load('Images/sqimg.png')

hpbars = pygame.image.load('Images/healthbars.png')
greenbars = pygame.image.load('Images/greenbar.png')
arrow = pygame.image.load('Images/arrowcursor.png')
# all the images added above

greenbar2 = pygame.image.load('Images/greenbar.png')

opponentchoose = pygame.image.load('Images/opponentchoose.png')
pokemonchoose = pygame.image.load('Images/pokemonchoose.png')
# duplicating health bar - one for player's health, the other for opponent

fightstate = 1
# a fight state variable - will be 1 when the fight is going on, will be 2 if player wins, will be 3 if opponent wins ( will tell more about this tomorrow)
greenbarlength = 168
running = True

playerhealth = 100
pchealth = 100

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


#dif is difficulty variable
def pcattack(dif):
    global playerhealth
    playerhealth += -20 - (random.random() * 10 * dif) // 1
    if playerhealth <= 0:
        playerhealth = 0


def pcheal(dif):
    global pchealth
    pchealth += 20 + (random.random() * 10 * dif) // 1
    if pchealth >= 100:
        pchealth = 100

catchvar = -1

arrowcoordinatex, arrowcoordinatey = 40, 520
# coordinates of the arrow cursor to navigate between options)
running = True

while running:
    screen.blit(opponentchoose, (0,0))
    pygame.display.update()
    for event2 in pygame.event.get():
        if event2.type == pygame.KEYDOWN:
            if event2.key == pygame.K_1:
                oppname = 'Bulbasaur'
                print(oppname)
                dif = 1
                running = False
            elif event2.key == pygame.K_2:
                oppname = 'Squirtle'
                print(oppname)
                dif = 1.1
                running = False

            elif event2.key == pygame.K_3:
                oppname = 'Charmander'
                print(oppname)
                dif = 1.2
                running = False

            elif event2.key == pygame.K_4:
                oppname = 'Pikachu'
                print(oppname)
                dif = 1.3
                running = False

running = True
while running:

    screen.blit(pokemonchoose, (0,0))
    fh = open('pokemoninfo.bin','rb')
    pokemonlist = pickle.load(fh)
    imgblitcounter = 0
    for i in pokemonlist.values():
        if i == 'Pikachu':
            screen.blit(pikaimg, (0 + imgblitcounter,260))
            imgblitcounter += 150
        if i == 'Bulbasaur':
            screen.blit(bulbimg, (0 + imgblitcounter,260))
            imgblitcounter += 150
        if i == 'Squirtle':
            screen.blit(sqimg, (0 + imgblitcounter,260))
            imgblitcounter += 150
        if i == 'Charmander':
            screen.blit(charimg, (0 + imgblitcounter,260))
            imgblitcounter += 150

    for event1 in pygame.event.get():
        if event1.type == pygame.KEYDOWN:

            if event1.key == pygame.K_1:
                pokename = pokemonlist[1]
                running = False

            if event1.key == pygame.K_2:
                pokename = pokemonlist[2]
                running = False

            if event1.key == pygame.K_3:
                pokename = pokemonlist[3]
                running = False

            if event1.key == pygame.K_4:
                pokename = pokemonlist[4]
                running = False

    pygame.display.update()


running = True

while running:

    bannertextvar = True

    temppch, tempplh, playerdamagedealt, pcdamagedealt, playerheal, pchealed = 0, 0, 0, 0, 0, 0

    # health variables used to calculate stuff like damage dealt or healed by player and opponent per round

    screen.blit(bsc, (0, 0))

    if oppname == 'Pikachu':
        oppimg = pikaimg
    elif oppname == 'Squirtle':
        oppimg = sqimg
    elif oppname == 'Bulbasaur':
        oppimg = bulbimg
    elif oppname == 'Charmander':
        oppimg = charimg

    if pokename == 'Pikachu':
        pokeimg = pbimg
    elif pokename == 'Charmander':
        pokeimg = cbimg
    elif pokename == 'Bulbasaur':
        pokeimg = bbimg
    elif pokename == 'Squirtle':
        pokeimg = sbimg

    screen.blit(oppimg, (450, 60))
    screen.blit(pokeimg, (75, 275))
    screen.blit(pbsc, (0, 450))
    font = pygame.font.Font('Raleway-Medium.ttf', 30)
    font2 = pygame.font.Font('PokemonGb-RAeo.ttf', 20)
    text4 = font2.render(oppname, True, (0, 0, 0))
    text5 = font2.render(pokename, True, (0, 0, 0))
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
            screen.blit(pokeimg, (75, 275))
            screen.blit(pbsc, (0, 450))
            screen.blit(hpbars, (0, 0))
            screen.blit(greenbars, (165, 115))
            screen.blit(greenbar2, (601, 411))
            if catchvar == -1:
                text8 = font2.render(F'The wild {oppname} fainted!', True, (0, 0, 0))
            elif catchvar == 1:
                text8 = font2.render(F'The wild {oppname} escaped!', True, (0,0,0))
            elif catchvar == 0:
                text8 = font2.render(F'You caught the wild {oppname}', True, (0,0,0))
            screen.blit(text8, (40, 505))
            pygame.display.update()

    elif playerhealth == 0:
        while True:
            screen.blit(bsc, (0, 0))
            screen.blit(oppimg, (450, 60))
            screen.blit(pbsc, (0, 450))
            screen.blit(hpbars, (0, 0))
            screen.blit(greenbars, (165, 115))
            screen.blit(greenbar2, (601, 411))
            text8 = font2.render(F'{pokename} fainted!', True, (0, 0, 0))
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

                        pcattack(dif)

                        pcdamagedealt = str(ph1 - playerhealth)

                        # pcdamagedealt, pcdamagehealed, playerdamagedealt, playerdamagehealed, temppch, tempplh are all variables for calculating how much damage has been dealt or healed per round

                    else:
                        pcheal(dif)

                        pchealed = str(pchealth - temppch)

                if arrowcoordinatex == 340:
                    pheal()

                    tempplh = playerhealth

                    playerheal = str(playerhealth - ph1)

                    pcmovedetermine = random.random()

                    if pcmovedetermine > 0.5:
                        pcattack(dif)

                        pcdamagedealt = str(tempplh - playerhealth)


                    else:
                        pcheal(dif)

                        pchealed = str(pchealth - pch1)

                if arrowcoordinatex == 640:
                    catchvar = 1
                    pchealth = 0

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

    # above code is for controlling the cursor arrow'''

    pygame.display.update()

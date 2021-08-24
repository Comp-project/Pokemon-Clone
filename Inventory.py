import pygame

def showinv(screen, invimg, playerinventory, pokedict, charsp, sqsp, bulbsp, pikasp):
    textX = 100
    textY = 128
    running2 = True

    while running2:
        screen.blit(invimg, (50, 67))
        font = pygame.font.Font('PokemonGb-RAeo.ttf', 20)

        for i in playerinventory:
            font1 = font.render(pokedict[i], True, (255, 255, 255))
            screen.blit(font1, (textX, textY + i * 50))
            if pokedict[i] == "Pikachu":
                screen.blit(pikasp,(350,textY + i * 50 - 25))
            elif pokedict[i] == "Charmander":
                screen.blit(charsp, (350, textY + i * 50 - 25))
            elif pokedict[i] == "Squirtle":
                screen.blit(sqsp, (350, textY + i * 50 - 25))
            elif pokedict[i] == "Bulbasaur":
                screen.blit(bulbsp, (350, textY + i * 50 - 25))


        for event3 in pygame.event.get():
            if event3.type == pygame.KEYDOWN:
                running2 = False

        pygame.display.update()
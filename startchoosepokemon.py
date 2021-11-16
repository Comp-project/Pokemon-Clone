import pygame

startchoose = pygame.image.load("Images/startchoose.png")

def blitcs(screen, startchoose, pokemonID, pokedict, playerinventory):
    running = True

    while running:
        screen.fill((0, 0, 0))
        screen.blit(startchoose, (50, 67))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pokemonID+= 1
                    playerinventory.append(pokemonID)
                    pokedict[pokemonID] = 'Charmander'
                    running = False

                if event.key == pygame.K_2:
                    pokemonID += 1
                    playerinventory.append(pokemonID)
                    pokedict[pokemonID] = 'Pikachu'
                    running = False

                if event.key == pygame.K_3:
                    pokemonID += 1
                    playerinventory.append(pokemonID)
                    pokedict[pokemonID] = 'Squirtle'
                    running = False

                if event.key == pygame.K_4:
                    pokemonID += 1
                    playerinventory.append(pokemonID)
                    pokedict[pokemonID] = 'Bulbasaur'
                    running = False
    return
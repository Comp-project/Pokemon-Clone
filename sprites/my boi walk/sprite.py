import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")



walkRIGHT = [pygame.image.load('R0.png'),pygame.image.load('R1.png'),pygame.image.load('R2.png')]
walkLEFT = [pygame.image.load('walk left idle.png'),pygame.image.load('walk left 1.png'),pygame.image.load('walkleft 2.png')]
walkUP = [pygame.image.load('walk back idle.png'),pygame.image.load('walk back 1.png'),pygame.image.load('walk back 2.png')]
walkDOWN = [pygame.image.load('walk front 1.png'),pygame.image.load('walk front 2.png')]
bg = pygame.image.load('bg.png')
char = pygame.image.load('walk front idle.png')

clock = pygame.time.Clock()
x = 50
y = 50

height = 25
width = 20
walkCount = 0
left = False
right = False
up = False
down =False
vel = 5


def draw() :
    global walkCount
    win.blit(bg, (0,0))

    if walkCount +1 >= 27 :
        walkCount = 0
    if left:
        win.blit(walkLEFT[walkCount//3],(x,y)) 
        walkCount += 1
    elif right:
        win.blir(walkRIGHT[walkCount//3],(x,y))
        walkCount += 1
    if left:
        win.blit(walkUP[walkCount//3],(x,y)) 
        walkCount += 1
    elif right:
        win.blit(walkDOWN[walkCount//3],(x,y))
        walkCount += 1
    else :
        win.blit(char,(x,y))   
    pygame.display.update()

run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and x > vel: 
        x -= vel
        left = True
        right = False
        up = False
        down = False

    elif keys[pygame.K_d] and x < 500 - vel - width:  
        x += vel
        right =True
        left = False
        up = False
        down = False

    elif keys[pygame.K_w] :
        y += vel
        up = True
        down = False
        right = False
        left = False
    elif keys[pygame.K_s]:
        y -= vel
        up = False
        down = True
        right = False
        left = False


   
    draw() 
    
    
pygame.quit()

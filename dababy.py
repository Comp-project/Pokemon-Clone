#was pretty sleepy tried to explaint he best i can 
# some silly mistakes might be there but logic is solid 
#just go through
# see if you can get a better idea



import pygame
from _typeshed import Self

from pygame import fastevent

pygame.init()

green = (0,255,0)
maxhealth = 100
pchealth  = 100
phealth = 100
scalefactor = 2
dmg = -20 
heal = 10
m = True

playerattack = True

screen =  pygame.display.set_mode((100,100))

a = False # a is an arbitrary value 

attack_img = pygame.image.load('imglocation.png')
heal_img = pygame.image.load('imglocation.png')

class attack():
    def __init__(self,x,y,image):   # i saw this online didn understand everything but i can explain most of it
        self.image = image             # just assigns image a callable objext
        self.rect = self.image.rect() #makes the image a rect
        self.rect.topleft = (x,y)  # coordinates of img
        self.clicked = False  #checking for click event( if this isnt there multiple clicks are registered)
    
    def draw():
        action = False  
        pos =pygame.mouse.get_pos() # gives position of mouse

        if self.rect.collidepoint(pos): # if mouse pos collides withe rect
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # if it does and they left click 
				self.clicked = True # our variable changes 
				action = True #retruns true
            
            if pygame.mouse.get_pressed()[0] == 0: #when they arent pressing 
                self.clicked = False #variable resets 
        
        screen.blit(self.image,(self.rect.x,self.rect.y)) # bliting button img
        return action


attack_button = attack(x ,y , attack_img) # assigns the calling of the class to a variable
heal_button = attack(x,y, heal_img)

# call attack_button.draw()

def phealthbar(currenthealth,value): # since for the player value can be -ve or +ve for heal or dmg
    while m :
        temp  = currenthealth
        if currenthealth + value < temp : #after damage the new value will be less than old so this is a way to check if we actually hurt ourpokemon
            for i in range(0,value+1): # i wante dlike a decending health bar but if this doesnt work we can directly blit the new health
            pygame.draw.rect(screen ,green , (x , y , scalefactor*(temp - i), 7 )) #change values of rectangle (the actual health bar )
            m = False

        elif currenthealth + value > temp : # same concept except its a heal so we heal our selves
            for i in range(0,value+1):
            pygame.draw.rect(screen ,green , (x , y , scalefactor*(temp + i), 7 )) #change values
            m = False
            

def pchealthbar(currenthealth,damage): #health bar for pc pokemon
    while True :
        temp  = currenthealth
        for i in range(0,damage+1):
            pygame.draw.rect(screen ,green , (x , y , scalefactor*(temp - i), 7 )) #change values
        break




def heal_mod():
    if heal_button.draw():
        if playerattack == True :
            phealthbar(phealth,heal)
    playerattack = False
    phealth += heal
    

    
def pattackmod() :
    if attack_button.draw(): # if action is true that is they pressed attack 
        if playerattack = True: # registers players move
            if pchealth > 20 : # same logiv as below
                pygame.blit('teh pokemon has attacked',(x,y))
                pchealthbar(pchealth,dmg)
            pchealth = pchealth + dmg
            
            elif pchealth - dmg == 0:
                pygame.blit('teh pokemon has faint',(x,y))
                pchealth = 0 
                pchealthbar(pchealth,dmg)
    playerattack = False

def pcattackmod() :
    if playerattack == False:
        if phealth > 20 :  #checking to see if the pokemon can withstand attack
            pygame.blit('teh wild pokemon has attacked',(x,y)) # we have to blit an img sayign that
            phealthbar(phealth,dmg)
        phealth = phealth + dmg

        elif phealth - dmg == 0: #if health is 20 rather than addign <= 20 i just did this 
            pygame.blit('ur pokemon has faint',(x,y))
            phealth = 0 
            phealthbar(phealth,dmg)
    playerattack = True # resets value now its players tur 



    

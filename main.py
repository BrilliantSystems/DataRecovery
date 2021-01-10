'''

'''

#imports
import pygame, keyboard, random, tile

#pygame init
pygame.init()
window = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
version = "0.001a"
pygame.display.set_caption("Data Recovery [PROTOTYPE] "+str(version))
gamecrash=False
x=100
y=100


#tile definitions
test = tile.Tile("test.png")

while not gamecrash:
    #Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamecrash = True

    x+=0.1
    y+=0.1

    #clear screen
    window.fill((0,0,0))

    #sprites go here
    test.Draw(x,y,window)

    #End Frame
    pygame.display.update()
    




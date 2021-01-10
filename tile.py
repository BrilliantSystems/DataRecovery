import pygame

class Tile:
    def __init__(self,art):
        self.Sprite = pygame.image.load(art)

    def Draw(self,x,y,window):
        window.blit(self.Sprite,(x,y))
import pygame

class Segment:
    def __init__(self,pos):
        self.pos=pos 
        self.width=1
        self.height=40
        self.rect=pygame.Rect(int(pos.x),int(pos.y),self.width,self.height) 

    def draw(self,surface,trailing):
        self.rect = pygame.draw.circle(surface,(0,0,255) if trailing else (0,255,255) , self.pos, 15)
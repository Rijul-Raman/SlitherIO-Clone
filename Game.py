import pygame 
from pygame import Vector2 as v2
import random
import sys
from Player import Player
from Orb import Orb
from Camera import Camera
from Segment import Segment

FPS = 60

class Game:
    def __init__(self): 
        self.dimensions=v2(1200,800)
        self.bgcolor=(15, 14, 15)
        self.orb_size=20
        self.number_of_orbs=10

        pygame.init()

        self.window=pygame.display.set_mode((self.dimensions.x,self.dimensions.y))

        self.clock=pygame.time.Clock()
        
        self.player=Player(self)
        self.PLAYER_UPDATE=pygame.USEREVENT
        pygame.time.set_timer(self.PLAYER_UPDATE,self.player.speed)

        self.camera=Camera(self)
        
        self.orbs=[]
        self.init_orbs(self.number_of_orbs)

    def init_orbs(self,number_of_orbs):
        for i in range(0,number_of_orbs):
            pos=v2(random.randint(0,self.dimensions.x-self.orb_size),random.randint(0,self.dimensions.y-self.orb_size))
            self.orbs.append(Orb(pos,self))

            for index1,orb1 in enumerate(self.orbs):
                for index2,orb2 in enumerate(self.orbs):
                    if pygame.Rect.colliderect(orb1.rect,orb2.rect) and index1!=index2:
                        self.orbs.pop(index1)
                        self.init_orbs(1)

            for orb in self.orbs:
                for seg in self.player.segments:
                    if pygame.Rect.colliderect(orb.rect,seg.rect):
                        self.orbs.remove(orb)
                        self.init_orbs(1)
                        
    def render(self):
        for orb in self.orbs:
            orb.draw()
        self.player.draw()

    def update(self):
        self.player.update()
        self.camera.update()

        for seg in self.player.segments:
            seg.pos=self.camera.transformed_coords(seg.pos)

        for orb in self.orbs:
            if orb.update():
                self.orbs.remove(orb)
                self.init_orbs(1)
                self.player.score+=1
                self.player.update_length()
                print("Score:",self.player.score)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==self.PLAYER_UPDATE:
                    self.update()
            self.clock.tick(FPS)
            self.window.fill(self.bgcolor)
            self.render()
            pygame.display.update()
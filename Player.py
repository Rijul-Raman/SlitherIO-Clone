import pygame
from pygame import Vector2 as v2
from Segment import Segment

class Player:
    def __init__(self,game):
        self.score=0
        self.game=game
        self.speed=15
        self.segments=[]
        for i in range(0,80):
            self.segments.append(Segment(game.dimensions/2-i*v2(1,0)))
    
    def update_length(self):                
        for i in range(0,self.score):
            self.segments.append(Segment(self.game.dimensions/2-i*v2(1,0)))
    
    def draw(self):
        for index in range(len(self.segments)-1,-1,-1):
            self.segments[index].draw(self.game.window,index)

    def update(self):
        mouse_pos=v2(pygame.mouse.get_pos()) - self.segments[0].rect.center
        if mouse_pos!=v2(0,0):
            direction=mouse_pos.normalize()
        else:
            direction=v2(0,0)

        self.segments=self.segments[:-1]
        self.segments.insert(0,Segment(self.segments[0].pos+direction*1))
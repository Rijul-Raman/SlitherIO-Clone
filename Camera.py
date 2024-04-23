import pygame

class Camera:
    def __init__(self,game):
        self.game=game 
        self.pos=game.player.segments[0].pos
    
    def update(self):
        self.pos=self.game.player.segments[0].pos

    def transformed_coords(self,coords):
        return coords - (self.pos - (self.game.dimensions)/2)
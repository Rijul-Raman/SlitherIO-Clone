import pygame
import random

class Orb:
    def __init__(self,pos,game):
        self.colors = [(175,12,12), (224, 208, 29), (42, 138, 18), (14, 150, 146), (14, 55, 176), (161, 8, 74)]
        self.color=random.choice(self.colors)
        self.game=game
        pos=game.camera.transformed_coords(pos)
        self.rect=pygame.Rect(int(pos.x),int(pos.y),game.orb_size,game.orb_size)

    def draw(self):
        pygame.draw.rect(self.game.window,self.color,self.rect)

    def update(self):
        if pygame.Rect.colliderect(self.rect,self.game.player.segments[0].rect):
            return True
        self.rect.topleft=self.game.camera.transformed_coords(self.rect.topleft)
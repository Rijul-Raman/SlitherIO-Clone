import pygame 
import random
import time
from . import Player, Orb, Camera, Segments

FPS = 60
MIN_ORB_RADIUS = 3
MAX_ORB_RADIUS = 10

class Game:
    def __init__(self, window_dimensions, window_color):
        pygame.init()
        self.window_dimensions = window_dimensions
        self.window = pygame.display.set_mode(self.window_dimensions)
        self.window_color = window_color
        self.quit = False
        self.player = Player()
        self.clock = pygame.time.Clock()
        self.food_orbs = []
        self.camera = Camera()
        self.init_food_orbs()
        self.last_spawn_time = time.time()
        self.spawn_interval = random.randint(3,6)
    
    def init_food_orbs(self):
        if(time.time()-self.last_spawn_time > self.spawn_interval):
            x = random.randint(0, self.window_dimensions[0])
            y = random.randint(0, self.window_dimensions[1])
            radius = random.randint(MIN_ORB_RADIUS, MAX_ORB_RADIUS)
            orb = Orb(x, y, radius)
            self.food_orbs.append(orb)
            self.last_spawn_time = time.time()
    
    def update(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.quit = True
        
        self.food_orbs = [orb for orb in self.food_orbs if not orb.collide_with_player(self.player.rect)]
        self.camera_update(self.player)
        self.init_food_orbs()
    
    def render(self):
        self.window.fill(self.window_color)
        self.player.render(self.window, self.camera)

        for orb in self.food_orbs:
            orb.render(self.window, self.camera)
        
        pygame.display.flip()
    
    def run(self):
        while not self.quit:
            self.update()
            self.render()
            self.clock.tick(FPS)

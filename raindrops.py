import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group

class Raindrop(Sprite):
    def __init__(self):
        super(Raindrop, self).__init__()
        self.image = pygame.image.load('raindrop.bmp')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        
raindrops = Group()

for i in range(5):
    drop = Raindrop()
    drop.rect.x += drop.width * i
    raindrops.add(drop)
    
def update_drops(raindrops, screen):
    for drop in raindrops:
        drop.rect.y += 2
    if drop.rect.y >= screen_rect.height:
        for drop in raindrops:
            drop.rect.y = 0

while True:
    screen_l = 1200
    screen_w = 800
    screen = pygame.display.set_mode((screen_l, screen_w))
    screen.fill((255, 255, 255))
    screen_rect = screen.get_rect()
    raindrop = Raindrop()
    # ~ raindrop.rect.x = screen_rect.centerx
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    raindrops.draw(screen)
    update_drops(raindrops, screen)    
    pygame.display.flip()
    

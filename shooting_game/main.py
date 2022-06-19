import random

import pygame
from pygame.locals import *
    

class Python(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("python.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.x = pos_x
        self.y = pos_y
        self.rect.center = (self.x, self.y)
        self.python_group = pygame.sprite.Group()
        
    def put_mutible(self):
        
        for i in range(20):
            new_python = Python(random.randrange(0, 600), random.randrange(0, 600))
            self.python_group.add(new_python)
            
   
class Gun(pygame.sprite.Sprite):
    def __init__(self, win):
        super().__init__()
        self.image = pygame.image.load("gun.png").convert_alpha()
        self.fire_sound = pygame.mixer.Sound("fire_sound.mp3")
        self.win = win
        self.rect = self.image.get_rect()
        pygame.mouse.set_visible(0)
        self.cross_hair_group = pygame.sprite.Group()

        
    
    def shooting(self):
        self.fire_sound.set_volume(0.3)
        self.fire_sound.play()
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()         


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.win = pygame.display.set_mode((600, 600))
        self.NAME = "My shooting game"
        self.BG_COLOR = (255, 255, 255)
        self.CLOCK = pygame.time.Clock()
        self.gun = Gun(self.win)
        self.gun.cross_hair_group.add(self.gun)
        self.python = Python(0, 0)
        self.python.put_mutible()
        
    def update(self):
        self.win.fill(self.BG_COLOR)
        self.python.python_group.draw(self.win)
        self.gun.cross_hair_group.update()
        self.gun.cross_hair_group.draw(self.win)
        
        self.CLOCK.tick()
        pygame.display.flip()
        
    def run(self):
        pygame.display.set_caption(self.NAME)
        flag = True
        while flag:
            self.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    flag = False
                if event.type == MOUSEBUTTONDOWN:
                    self.gun.shooting()
                    pygame.sprite.spritecollide(self.gun, self.python.python_group, True)
        pygame.quit()
                    
                    

if __name__ == "__main__":
    game = Game()
    game.run()

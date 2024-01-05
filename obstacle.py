import pygame
from random import randint, choice

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type, scale_factor=3):
        super().__init__()
        

        if type == 'fly':
            fly_1 = pygame.image.load('graphics/fly/bat1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/fly/bat2.png').convert_alpha()
            self.frames = [pygame.transform.scale(fly_1, (int(fly_1.get_width() * scale_factor), int(fly_1.get_height() * scale_factor))),
                           pygame.transform.scale(fly_2, (int(fly_2.get_width() * scale_factor), int(fly_2.get_height() * scale_factor)))]
            y_pos = 410
        else:
            slime_1 = pygame.image.load('graphics/snail/slime-attack-2.png')
            slime_2 = pygame.image.load('graphics/snail/slime-attack-3.png').convert_alpha()
            self.frames = [pygame.transform.scale(slime_1, (int(slime_1.get_width() * scale_factor), int(slime_1.get_height() * scale_factor))),
                           pygame.transform.scale(slime_2, (int(slime_2.get_width() * scale_factor), int(slime_2.get_height() * scale_factor)))]
            y_pos = 540

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(1300, 1600), y_pos))


    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0 
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
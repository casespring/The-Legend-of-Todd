import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_run_1 = pygame.image.load('graphics/player/run1.png').convert_alpha()
        player_run_2 = pygame.image.load('graphics/player/run2.png').convert_alpha()
        player_run_3 = pygame.image.load('graphics/player/run3.png').convert_alpha()
        player_run_4 = pygame.image.load('graphics/player/run4.png').convert_alpha()
        player_run_5 = pygame.image.load('graphics/player/run5.png').convert_alpha()
        player_run_6 = pygame.image.load('graphics/player/run6.png').convert_alpha()
        player_run_7 = pygame.image.load('graphics/player/run7.png').convert_alpha()
        player_run_8 = pygame.image.load('graphics/player/run8.png').convert_alpha()
        self.player_run = [player_run_1, player_run_2, player_run_3, player_run_4, player_run_5, player_run_6, player_run_7, player_run_8]
        self.player_index = 0
        player_jump_1 = pygame.image.load('graphics/player/jump1.png')
        print(player_jump_1)
        player_jump_2 = pygame.image.load('graphics/player/jump2.png')
        print(player_jump_2)
        player_jump_3 = pygame.image.load('graphics/player/jump3.png')
        print(player_jump_3)
        player_jump_4 = pygame.image.load('graphics/player/jump4.png')
        print(player_jump_4)
        player_jump_5 = pygame.image.load('graphics/player/jump5.png')
        print(player_jump_5)
        player_jump_6 = pygame.image.load('graphics/player/jump6.png')
        print(player_jump_6)
        player_jump_7 = pygame.image.load('graphics/player/jump7.png')
        player_jump_8 = pygame.image.load('graphics/player/jump8.png')
        player_jump_9 = pygame.image.load('graphics/player/jump9.png')
        self.player_jump = [player_jump_1, player_jump_2, player_jump_3, player_jump_4, player_jump_5, player_jump_6, player_jump_7, player_jump_8,player_jump_9] 
        self.player_jump_index = 0
        # self.playerl_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
        print(self.player_index)

        self.image = self.player_run[self.player_index]
        self.rect = self.image.get_rect(midbottom=(100, 540), width=60, height=80)
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.1)
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 540:
            self.gravity = -20
            self.jump_sound.play()
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 540:
            self.rect.bottom = 540

    def animation_state(self):
        if self.rect.bottom < 540:
            self.player_jump_index += 0.1
            if self.player_jump_index >= len(self.player_jump):self.player_jump_index = 0 
            self.image = self.player_jump[int(self.player_jump_index)]
            # self.image = self.playerl_jump
        else:
            self.player_index += 0.3
            if self.player_index >= len(self.player_run):self.player_index = 0
            self.image = self.player_run[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
import pygame
from sys import exit 
from random import randint, choice
import math 
from player import Player
from obstacle import Obstacle

# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         player_run_1 = pygame.image.load('graphics/player/run1.png').convert_alpha()
#         player_run_2 = pygame.image.load('graphics/player/run2.png').convert_alpha()
#         player_run_3 = pygame.image.load('graphics/player/run3.png').convert_alpha()
#         player_run_4 = pygame.image.load('graphics/player/run4.png').convert_alpha()
#         player_run_5 = pygame.image.load('graphics/player/run5.png').convert_alpha()
#         player_run_6 = pygame.image.load('graphics/player/run6.png').convert_alpha()
#         player_run_7 = pygame.image.load('graphics/player/run7.png').convert_alpha()
#         player_run_8 = pygame.image.load('graphics/player/run8.png').convert_alpha()
#         self.player_run = [player_run_1, player_run_2, player_run_3, player_run_4, player_run_5, player_run_6, player_run_7, player_run_8]
#         self.player_index = 0
#         player_jump_1 = pygame.image.load('graphics/player/jump1.png')
#         print(player_jump_1)
#         player_jump_2 = pygame.image.load('graphics/player/jump2.png')
#         print(player_jump_2)
#         player_jump_3 = pygame.image.load('graphics/player/jump3.png')
#         print(player_jump_3)
#         player_jump_4 = pygame.image.load('graphics/player/jump4.png')
#         print(player_jump_4)
#         player_jump_5 = pygame.image.load('graphics/player/jump5.png')
#         print(player_jump_5)
#         player_jump_6 = pygame.image.load('graphics/player/jump6.png')
#         print(player_jump_6)
#         player_jump_7 = pygame.image.load('graphics/player/jump7.png')
#         player_jump_8 = pygame.image.load('graphics/player/jump8.png')
#         player_jump_9 = pygame.image.load('graphics/player/jump9.png')
#         self.player_jump = [player_jump_1, player_jump_2, player_jump_3, player_jump_4, player_jump_5, player_jump_6, player_jump_7, player_jump_8,player_jump_9] 
#         self.player_jump_index = 0
#         # self.playerl_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
#         print(self.player_index)

#         self.image = self.player_run[self.player_index]
#         self.rect = self.image.get_rect(midbottom=(100, 540), width=60, height=80)
#         self.gravity = 0

#         self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
#         self.jump_sound.set_volume(0.1)
    
#     def player_input(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_SPACE] and self.rect.bottom >= 540:
#             self.gravity = -20
#             self.jump_sound.play()
    
#     def apply_gravity(self):
#         self.gravity += 1
#         self.rect.y += self.gravity
#         if self.rect.bottom >= 540:
#             self.rect.bottom = 540

#     def animation_state(self):
#         if self.rect.bottom < 540:
#             self.player_jump_index += 0.1
#             if self.player_jump_index >= len(self.player_jump):self.player_jump_index = 0 
#             self.image = self.player_jump[int(self.player_jump_index)]
#             # self.image = self.playerl_jump
#         else:
#             self.player_index += 0.3
#             if self.player_index >= len(self.player_run):self.player_index = 0
#             self.image = self.player_run[int(self.player_index)]

#     def update(self):
#         self.player_input()
#         self.apply_gravity()
#         self.animation_state()

# class Obstacle(pygame.sprite.Sprite):
#     def __init__(self, type, scale_factor=1.1):
#         super().__init__()

#         if type == 'fly':
#             fly_1 = pygame.image.load('graphics/fly/bat1.png').convert_alpha()
#             fly_2 = pygame.image.load('graphics/fly/bat2.png').convert_alpha()
#             self.frames = [pygame.transform.scale(fly_1, (int(fly_1.get_width() * scale_factor), int(fly_1.get_height() * scale_factor))),
#                            pygame.transform.scale(fly_2, (int(fly_2.get_width() * scale_factor), int(fly_2.get_height() * scale_factor)))]
#             y_pos = 410
#         else:
#             slime_1 = pygame.image.load('graphics/snail/slime-attack-2.png')
#             slime_2 = pygame.image.load('graphics/snail/slime-attack-3.png').convert_alpha()
#             self.frames = [pygame.transform.scale(slime_1, (int(slime_1.get_width() * scale_factor), int(slime_1.get_height() * scale_factor))),
#                            pygame.transform.scale(slime_2, (int(slime_2.get_width() * scale_factor), int(slime_2.get_height() * scale_factor)))]
#             y_pos = 540

#         self.animation_index = 0
#         self.image = self.frames[self.animation_index]
#         self.rect = self.image.get_rect(midbottom=(randint(1300, 1600), y_pos))


#     def animation_state(self):
#         self.animation_index += 0.1
#         if self.animation_index >= len(self.frames): self.animation_index = 0 
#         self.image = self.frames[int(self.animation_index)]

#     def update(self):
#         self.animation_state()
#         self.rect.x -= 6
#         self.destroy()

#     def destroy(self):
#         if self.rect.x <= -100:
#             self.kill()

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Distance: {current_time}',False, 'Gray')
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 6 

            if obstacle_rect.bottom == 540:
                screen.blit(snail_surf,obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []
    
def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True 

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        obstacle_group.empty()
        return False
    else: return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 540:
        player_surf = playerL_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):player_index = 0
        player_surf = player_walk[int(player_index)]

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
game_death_screen = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.play(loops = -1)
bg_music.set_volume(0.1)

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

forest_surface = pygame.image.load('graphics/Cartoon_Forest_BG_02.png').convert()
forest_surface = pygame.transform.scale(forest_surface, (1280,620))
forest_surface_width = forest_surface.get_width()
scroll = 0
tiles = math.ceil(1280 / forest_surface_width) + 1
# print(tiles)
ground_surface = pygame.image.load('graphics/forest_ground.jpg').convert_alpha()
ground_surface = pygame.transform.scale(ground_surface, (1280, 240))
ground_surface_width = ground_surface.get_width()
ground_scroll = 0
tiles_ground = math.ceil(1280/ ground_surface_width) + 1

# score_surf = test_font.render('My game', False, (64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))

snail_frame_1 = pygame.image.load('graphics/snail/slime-attack-2.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/slime-attack-3.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

fly_frame_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk_1 = pygame.image.load('graphics/player/run1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/player/run2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
playerL_jump = pygame.image.load('graphics/player/jump1.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,540))
player_gravity = 0

#intro screen
player_stand = pygame.image.load('graphics/Player/idle1.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (640, 360))

player_dead = pygame.image.load('graphics/Player/dead.png').convert_alpha()
player_dead = pygame.transform.rotozoom(player_dead,0,2)
player_dead_rect = player_dead.get_rect(center = (640, 360))

game_name = test_font.render('The Legend of Todd', False, ('Grey'))
game_name_rect = game_name.get_rect(center = (640, 240)) 

game_message = test_font.render('Press Space to Start', False, ('Grey'))
game_message_rect = game_message.get_rect(center = (640, 550))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

#increase speed
current_time = 0
speed_multiplier = 1
last_speed_increase_time = 0

obstacle_spawn_timer = pygame.USEREVENT + 4
pygame.time.set_timer(obstacle_spawn_timer, 3000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 540:
                    player_gravity = -20  
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            if event.type == obstacle_timer and game_active:
                 obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail']), scale_factor=1.8))
            # if game_active and pygame.time.get_ticks() - obstacle_timer > 3000:
            #     obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail']), scale_factor=2))
            #     last_obstacle_spawn_time = pygame.time.get_ticks()

                # if randint(0,2):
                #     obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
                # else:
                #     obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100), 210)))
            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else: snail_frame_index = 0 
                snail_surf = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:fly_frame_index = 0 
                fly_surf = fly_frames[fly_frame_index] 



    if game_active:
        for i in range(0, tiles):
            screen.blit(forest_surface,(i * forest_surface_width + scroll, 0))
        for i in range(0, tiles_ground):
            screen.blit(ground_surface, (i * ground_surface_width + ground_scroll, screen.get_height() - ground_surface.get_height() + 60))
        score = display_score()
        scroll -= 2
        ground_scroll -= 2

        if abs(scroll) > forest_surface_width:
            scroll = 0
        
        if abs(ground_scroll) > ground_surface_width:
            ground_scroll = 0 

        player.draw(screen)
        player.update()
 
        obstacle_group.draw(screen)
        obstacle_group.update()

        # Check if the time is a multiple of 50 and increase speed
        current_time = int(pygame.time.get_ticks() / 1000) - start_time
        if current_time % 5 == 0 and current_time != last_speed_increase_time:
            speed_multiplier += 0.3  # Increase the speed multiplier (adjust as needed)

            # Update obstacle speed based on the new multiplier
            for obstacle in obstacle_group:
                obstacle.rect.x -= int(10 * speed_multiplier)

            # Update the time when the last speed increase occurred
            last_speed_increase_time = current_time
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # game_active = collisions(player_rect,obstacle_rect_list)
        game_active = collision_sprite()

        # if snail_rect.colliderect(player_rect):
        #     game_active = False
    else:
        screen.fill((94,129,169))
        screen.blit(forest_surface,(0,0))
        screen.blit(ground_surface, (0,540))
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,540)
        player_gravity = 0

        score_message = test_font.render(f'Your Distance: {score}', False,('Gray'))
        score_message_rect = score_message.get_rect(center = (640, 550))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
            screen.blit(player_stand, player_stand_rect)
        else: 
            screen.blit(player_dead, player_dead_rect)
            screen.blit(score_message,score_message_rect)

    pygame.display.update()
    clock.tick(60)
# from pickle import REDUCE

import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 3200, 2000
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE , pygame.OPENGL)
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame Setup Test")

# Colors
WHITE = pygame.Color('#eceff4')
RED = pygame.Color('#bf616a')
ORANGE = pygame.Color('#d08770')
YELLOW = pygame.Color('#ebcb8b')
GREEN = pygame.Color('#a3be8c')
PURPLE = pygame.Color('#b48ead')

# Game loop
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#Loading Assets
image1 = pygame.image.load("02-DogBark/2dogs.JPG")
font1 = pygame.font.SysFont("jetbrains mono", 200)
caption1 = font1.render("DogBark", True, WHITE)
bark_sound = pygame.mixer.Sound("02-DogBark/bark.wav")
pygame.mixer.music.load("03-ClickInTheCircle/drums.wav")

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

caption1_flag = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bark_sound.play()
            print(distance(player_pos, pygame.mouse.get_pos()))
            if distance(player_pos, pygame.mouse.get_pos()) > 40:
                print("Outside")
                caption1_flag = 150
                pygame.mixer.music.stop()
            else:
                pygame.mixer.music.play(-1)

    # Drawing
    screen.fill(WHITE)

    screen.blit(image1, (500, 250))
    if caption1_flag > 0:
        screen.blit(caption1, (500, 250))

    pygame.draw.rect(screen, RED, (710, 490, 100, 100)) # Draw a blue square
    pygame.draw.rect(screen, ORANGE, (810, 490, 100, 100)) # Draw a blue square
    pygame.draw.rect(screen, YELLOW, (910, 490, 100, 100)) # Draw a blue square
    pygame.draw.rect(screen, GREEN, (1010, 490, 100, 100)) # Draw a blue square
    pygame.draw.rect(screen, PURPLE, (1110, 490, 100, 100)) # Draw a blue square
    pygame.draw.circle(screen, RED, (760, 450), 50) # Draw a blue square
    pygame.draw.circle(screen, ORANGE, (860, 450), 50) # Draw a blue square
    pygame.draw.circle(screen, YELLOW, (960, 450), 50) # Draw a blue square
    pygame.draw.circle(screen, GREEN, (1060, 450), 50) # Draw a blue square
    pygame.draw.circle(screen, PURPLE, (1160, 450), 50) # Draw a blue square

    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
    pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline
    pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
    pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
    pygame.draw.circle(screen, (0, 0, 0), (242, 162), 7)  # black pupil
    pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
    pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
    pygame.draw.circle(screen, (0, 0, 0), (398, 162), 7)  # black pupil

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
        if player_pos.y < 0:
            player_pos.y = 0
        if player_pos.y > HEIGHT:
            player_pos.y = HEIGHT
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
        if player_pos.y < 0:
            player_pos.y = 0
        if player_pos.y > HEIGHT:
            player_pos.y = HEIGHT
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        if player_pos.x < 0:
            player_pos.x = 0
        if player_pos.x > WIDTH:
            player_pos.y = WIDTH
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        if player_pos.x < 0:
            player_pos.x = 0
        if player_pos.x > WIDTH:
            player_pos.x = WIDTH

    caption1_flag -= 1

    # Update the display
    pygame.display.flip()

    dt = clock.tick(300) / 1000

# Quit
pygame.quit()
sys.exit()
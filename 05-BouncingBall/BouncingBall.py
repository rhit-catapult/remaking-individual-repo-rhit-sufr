import pygame
import sys
import random

WIDTH = 2560
HEIGHT = 1440


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move

class Ball:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = 10
        self.speed_x = random.randint(-10, 10)
        self.speed_y = random.randint(-10, 10)

    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # TODO: Create an instance of the Ball class called ball1
    ball0 = Ball(screen, WIDTH / 2, HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball
        if ball0.x < 0:
            ball0.x = 0
            ball0.speed_x = -ball0.speed_x
        if ball0.x > WIDTH:
            ball0.x = WIDTH
            ball0.speed_x = -ball0.speed_x
        if ball0.y < 0:
            ball0.y = 0
            ball0.speed_y = -ball0.speed_y
        if ball0.y > HEIGHT:
            ball0.y = HEIGHT
            ball0.speed_y = -ball0.speed_y
        ball0.move()

        # TODO: Draw the ball
        ball0.draw()

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball

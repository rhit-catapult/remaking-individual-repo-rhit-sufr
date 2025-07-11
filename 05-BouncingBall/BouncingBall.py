import pygame
import sys
import random
import math

WIDTH = 2560
HEIGHT = 1440


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move

class Ball:
    def __init__(self, screen, x, y, radius, speed_x, speed_y):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y


class Balls:
    def __init__(self, screen):
        self.screen = screen
        self.balls = []

    def generate(self, x, y, radius, speed_x, speed_y):
        new_ball = Ball(self.screen, x, y, radius, speed_x, speed_y)
        self.balls.append(new_ball)

    def delete(self, index):
        self.balls.pop(index)


class Player:
    def __init__(self, screen, x, y, time):
        self.screen = screen
        self.x = x
        self.y = y
        self.time = time

    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), 20)

    def move(self, keys):
        vec_x = 0
        vec_y = 0

        if keys[pygame.K_w]:
            vec_y -= 1
        if keys[pygame.K_s]:
            vec_y += 1
        if keys[pygame.K_a]:
            vec_x -= 1
        if keys[pygame.K_d]:
            vec_x += 1

        if vec_x != 0 and vec_y != 0:
            vec_x = math.sqrt(2)
            vec_y = math.sqrt(2)

        self.x += vec_x * 15
        self.y += vec_y * 15

        if self.x < 0:
            self.x = 0
        if self.x > WIDTH:
            self.x = WIDTH
        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT:
            self.y = HEIGHT


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # TODO: Create an instance of the Ball class called ball1
    ball_list = Balls(screen)
    ball_list.generate(WIDTH / 2, HEIGHT / 2, 10, random.randint(-10, 10), random.randint(-10, 10))

    player = Player(screen, WIDTH / 2, HEIGHT / 4, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        player.time += 1
        screen.fill(pygame.Color('gray'))

        for one_ball in ball_list.balls:
            # TODO: Move the ball
            if one_ball.x < 0:
                one_ball.x = 0
                one_ball.speed_x = -one_ball.speed_x
                ball_list.generate(one_ball.x, one_ball.y, one_ball.radius, one_ball.speed_x + random.randint(-2, 2),
                                   one_ball.speed_y + random.randint(-2, 2))
            if one_ball.x > WIDTH:
                one_ball.x = WIDTH
                one_ball.speed_x = -one_ball.speed_x
                ball_list.generate(one_ball.x, one_ball.y, one_ball.radius, one_ball.speed_x + random.randint(-2, 2),
                                   one_ball.speed_y + random.randint(-2, 2))
            if one_ball.y < 0:
                one_ball.y = 0
                one_ball.speed_y = -one_ball.speed_y
                ball_list.generate(one_ball.x, one_ball.y, one_ball.radius, one_ball.speed_x + random.randint(-2, 2),
                                   one_ball.speed_y + random.randint(-2, 2))
            if one_ball.y > HEIGHT:
                one_ball.y = HEIGHT
                one_ball.speed_y = -one_ball.speed_y
                ball_list.generate(one_ball.x, one_ball.y, one_ball.radius, one_ball.speed_x + random.randint(-2, 2),
                                   one_ball.speed_y + random.randint(-2, 2))
            one_ball.move()

            player.move(pygame.key.get_pressed())

            # TODO: Draw the ball
            one_ball.draw()
            player.draw()

        # print(len(ball_list.balls))
        if len(ball_list.balls) > 50:
            ball_list.delete(random.randint(0, 50))

        pygame.display.update()


main()

# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball

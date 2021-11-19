import pygame
import random
pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Runny Animals")
icon = pygame.image.load("media/fox_logo.png")
pygame.display.set_icon(icon)

rick_width = 40
rick_height = 80

rick_x = display_width // 3
rick_y = display_height - rick_height - 20

# Enemies variables
bottle_width = 15
bottle_height = 45

bottle_x = display_width - 45
bottle_y = display_height - bottle_height - 45

clock = pygame.time.Clock()

make_jump = False
jump_counter = 30


class Bottle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self):
        if self.x >= self.width:
            pygame.draw.rect(display, (0, 204, 0), (self.x, self.y, self.width, self.height))
            self.x -= self.speed
        else:
            self.x = display_width + 50


def run_game():
    global make_jump
    game = True
    bottle_arr = []
    create_bottle(bottle_arr)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True

        if make_jump:
            jump()

        display.fill((45, 93, 156))
        draw_bottle(bottle_arr)

        pygame.draw.rect(display, (153, 0, 75), (rick_x, rick_y, rick_width, rick_height))
        pygame.display.update()
        clock.tick(60)


def jump():
    global rick_y, jump_counter, make_jump
    if jump_counter >= -30:
        rick_y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False


def create_bottle(array):
    array.append(Bottle(display_width + 100, display_height - 100, 10, 70, 4))  # Add random generator to display_width
    array.append(Bottle(display_width + 200, display_height - 100, 10, 70, 4))  # and height instead of static values.
    array.append(Bottle(display_width + 400, display_height - 100, 10, 70, 4))  # vars: x, y, width, height, speed


def draw_bottle(array):
    for bottle in array:
        bottle.move()


run_game()

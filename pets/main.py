import pygame

pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Rick The Disaster")

rick_width = 60
rick_height = 100

rick_x = display_width // 3

icon = pygame.image.load("media/icon.png")
pygame.display.set_icon(icon)


def run_game():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill((45, 93, 156))
        pygame.display.update()


run_game()

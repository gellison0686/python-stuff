import pygame
import os

WIDTH, HEIGHT = 1100, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PAPA G SMELLS")

RED = (255, 0, 0)

FPS = 60

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

def draw_window():
    WIN.fill(RED)
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (150, 200))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == '__main__':
    main()

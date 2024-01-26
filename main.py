import pygame
from start_screen import start_screen

FPS = 60
W, H = 10, 20
TILE = 45

game_size = W * TILE, H * TILE


def main() -> None:
    """
    Main body of the whole game. This like a container form where we can start the game or change settings
    """
    pygame.init()
    size = game_size
    surface = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    running = start_screen(surface, clock, FPS)
    while running:
        pass

    pygame.quit()


if __name__ == '__main__':
    main()

import pygame
from start_screen import start_screen

FPS = 60  # test


def main() -> None:
    """
    Main body of the whole game. This like a container form where we can start the game or change settings
    """
    pygame.init()
    size = pygame.display.get_desktop_sizes()[0]
    surface = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    running = start_screen(surface, clock, FPS)
    while running:
        pass

    pygame.quit()


if __name__ == '__main__':
    main()

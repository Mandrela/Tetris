import pygame
from start_screen import start_screen
from result_screen import result_screen
from game import game
from icecream import ic

FPS = 60


def main() -> None:
    """
    Main body of the whole game. This like a container form where we can start the game or change settings
    """
    pygame.init()
    width, height = pygame.display.get_desktop_sizes()[0]
    surface = pygame.display.set_mode((width // 2, height // 2))
    clock = pygame.time.Clock()

    running = start_screen(surface, clock, FPS)
    while running:
        result = game(clock, FPS)
        if result == -1:
            break
        running, do_data = result_screen(surface, clock, FPS, result)
        if do_data:  # запись в БД
            pass

    pygame.quit()


if __name__ == '__main__':
    main()

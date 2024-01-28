import pygame
from start_screen import start_screen
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

    running = start_screen(surface, clock, FPS)  # анимация пока кривишна и некрасивишна, но не суть ;)
    while running:
        result = game(surface, clock, FPS)  # вот над функцией game ты и будешь работать. в нее передается все нужное
        if result == -1:
            running = False

    pygame.quit()


if __name__ == '__main__':
    main()

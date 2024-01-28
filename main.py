import pygame
from start_screen import start_screen

FPS = 60
W, H = 10, 20
TILE = 45

game_size = W * TILE, H * TILE


def main() -> None:  # Я короче не особо понял где надо было код писать, если сможешь переместить все в main было бы славно, а то у меня тут не особо работало, а там по кд ошибка UnboundLocalError: local variable 'какая-то переменная' referenced before assignment
    """
    Main body of the whole game. This like a container form where we can start the game or change settings
    """
    pygame.init()
    surface = pygame.display.set_mode(game_size)
    clock = pygame.time.Clock()

    running = start_screen(surface, clock, FPS)
    while running:
        pass

    pygame.quit()


if __name__ == '__main__':
    main()

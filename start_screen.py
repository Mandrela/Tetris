import pygame
import math
from icecream import ic


class Text:
    def __init__(self, pos: tuple[float, float], text: list[str], color: str = '#FFFFFF',
                 text_size: int = 50, speed: int = 0):
        self.x, self.y = pos
        self.text = text
        self.color = color
        self.text_size = text_size
        self.speed = speed
        self.font = pygame.font.Font('SAIBA-45.otf', self.text_size)
        self.ccnt = 0

    def render(self, surface: pygame.Surface, delta_time: int):
        self.ccnt += self.speed * delta_time / 1000
        for i in range(len(self.text)):
            line = self.font.render(self.text[i], 1, self.color)
            line.set_alpha(round(64 * math.cos(self.ccnt) + 191))
            surface.blit(line, line.get_rect(center=(self.x, self.y + i * self.text_size + 10)))


def start_screen(surface: pygame.Surface, clock: pygame.time.Clock, fps: int) -> bool:
    """
    Just a beautiful start screen
    :param surface: where to render
    :param clock:
    :param fps:
    :returns: True if start_screen was escaped correctly (space bar) False otherwise
    """

    # TODO: TETRIS_animation here

    w, h = ic(surface.get_rect()[2:])
    text = Text((w // 2, h // 5 * 4), ['Press any key', ' to continue'], color='#5FD4B1', text_size=w // 50, speed=5)
    dtime = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYUP:
                # TODO: START_animation here
                return True
        surface.fill('#000000')

        text.render(surface, dtime)

        pygame.display.flip()
        dtime = clock.tick(fps)


if __name__ == '__main__':
    pygame.init()
    size = pygame.display.get_desktop_sizes()[0]
    size = (size[0] // 2, size[1] // 2)
    surfaced = pygame.display.set_mode(size)
    clocc = pygame.time.Clock()

    start_screen(surfaced, clocc, fps=60)

    pygame.quit()

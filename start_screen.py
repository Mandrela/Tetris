import pygame
from icecream import ic


class Text:
    def __init__(self, pos: tuple[float, float], text: str, color: str = '#FFFFFF',
                 text_size: int = 50, speed: int = 5, amplitude: int = 2):
        self.x, self.y = pos
        self.text = text
        self.color = color
        self.text_size = text_size
        self.speed = speed
        self.amp = amplitude

    def render(self, surface: pygame.Surface):
        font = pygame.font.SysFont('Roboto', self.text_size)
        surface.blit(font.render(self.text, 1, self.color), (self.x, self.y))


def start_screen(surface: pygame.Surface, clock: pygame.time.Clock, fps: int) -> bool:
    """
    Just a beautiful start screen
    :param surface: where to render
    :param clock:
    :param fps:
    :returns: True if start_screen was escaped correctly (space bar) False otherwise
    """
    h, w = ic(surface.get_rect()[2:])
    text = Text((h // 2, w // 2), 'Test')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYUP and event.key == 32:
                return True
        surface.fill('#000000')

        text.render(surface)

        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    pygame.init()
    size = pygame.display.get_desktop_sizes()[0]
    size = (size[0] // 2, size[1] // 2)
    surfaced = pygame.display.set_mode(size)
    clocc = pygame.time.Clock()

    start_screen(surfaced, clocc, 60)

    pygame.quit()

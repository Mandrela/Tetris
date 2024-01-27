import pygame
from icecream import ic
from figures import *

TILE = 45
W, H = 10, 20

grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE)
        for x in range(10) for y in range(20)]


anim_count, anim_speed, anim_limit = 0, 60, 2000


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
        dx = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYUP and event.key == 32:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and figure[1].x > 0 and figure != figures[4] and figure != figures[6]:
                    dx = -1
                if event.key == pygame.K_LEFT and figure[1].x > 1 and (figure == figures[4] or figure == figures[6]):
                    dx = -1
                elif event.key == pygame.K_RIGHT and figure[3].x < W - 1 and figure != figures[3] and figure != figures[4] and figure != figures[6]:
                    dx = 1
                elif event.key == pygame.K_RIGHT and figure[3].x < W - 2 and (figure == figures[3] or figure == figures[4] or figure == figures[6]):
                    dx = 1
        surface.fill('#000000')
        # text.render(surface)

        # move x
        for i in range(4):
            figure[i].x += dx
        
        # move y
        anim_count += anim_speed
        if anim_count > anim_limit:
            anim_count = 0
            for i in range(4):
                figure[i].y += 1
        

        # прорисовка сетки
        [pygame.draw.rect(surface, (40, 40, 40), i_rect, 1)
         for i_rect in grid]

        # draw figure
        for i in range(4):
            figure_rect.x = figure[i].x * TILE
            figure_rect.y = figure[i].y * TILE
            pygame.draw.rect(surface, pygame.Color('White'), figure_rect)

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

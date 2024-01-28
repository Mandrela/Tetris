import pygame
import math
import time
from icecream import ic
from figures import *

TILE = 45
W, H = 10, 20

grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE)
        for x in range(10) for y in range(20)]


anim_count, anim_speed, anim_limit = 0, 60, 2000


class Effect:
    def __init__(self, w: int, h: int, tg_time: int):
        self.w, self.h = w, h
        self.is_going = True
        self.secs = 0
        self.tg_time = tg_time

    def update(self, dtime: int):
        self.secs += dtime
        if self.secs >= self.tg_time:
            self.is_going = False

    def __bool__(self):
        return self.is_going


class StartAnim(Effect):
    def __init__(self, w, h):
        super().__init__(w, h, 10000)
        self.oh = 0

        self.bg = pygame.Surface((w, h))
        self.text = Text((w // 2, -500), ['Text'])
        self.step = h / 2 / 500

    def play(self, surface: pygame.Surface, dtime: int):
        if self.secs <= 1000:
            surface.blit(self.bg, (0, 0))
        elif self.secs <= 1500:
            surface.blit(self.bg, (0, 0))
            self.text.set_pos(self.w / 2, self.oh)
            self.text.render(surface)
            self.oh += self.step * dtime
        elif self.secs <= 3000:
            pygame.draw.circle(surface, '#FF0000', (self.w // 2, self.h // 2), 5)
            self.text.render(surface)
        else:
            self.text.render(surface)

        super().update(dtime)


class EndAnim(Effect):
    def __init__(self, w, h):
        super().__init__(w, h, 2000)
        self.effect = pygame.Surface((w, h))
        self.effect.fill('#000000')
        self.alpha = 0

    def play(self, surface: pygame.Surface, dtime: int):
        self.alpha += 0.1275 * dtime
        self.effect.set_alpha(self.alpha)
        surface.blit(self.effect, (0, 0))

        super().update(dtime)


class Text:  # TODO: change font and color
    def __init__(self, pos: tuple[float, float], text: list[str], color: str = '#FFFFFF',
                 text_size: int = 50, speed: int = 0):
        self.x, self.y = pos
        self.text = text
        self.color = color
        self.text_size = text_size
        self.speed = speed
        self.font = pygame.font.Font('SAIBA-45.otf', self.text_size)
        self.ccnt = 0

    def render(self, surface: pygame.Surface, dtime: int = 0):
        self.ccnt += self.speed * dtime / 1000
        for i in range(len(self.text)):
            line = self.font.render(self.text[i], 1, self.color)
            line.set_alpha(round(64 * math.cos(self.ccnt) + 191))
            surface.blit(line, line.get_rect(center=(self.x, self.y + i * self.text_size + 10)))

    def set_pos(self, x: float, y: float):
        self.x, self.y = x, y


def start_screen(surface: pygame.Surface, clock: pygame.time.Clock, fps: int) -> bool:
    """
    Just a beautiful start screen
    :param surface: where to render
    :param clock:
    :param fps:
    :returns: True if start_screen was escaped correctly (key pressed) False otherwise
    """

    w, h = ic(surface.get_rect()[2:])
    text = Text((w // 2, h // 5 * 4), ['Press any key', ' to continue'], color='#A168D5', text_size=w // 50, speed=5)

    bg = pygame.Surface((w, h))
    bg.fill('#010101')
    n = w // 70
    n += 0 if n % 2 else 1
    [pygame.draw.line(bg, '#757575', (i * w // n - i % 2 * 30, 0), (i * w // n, h), w // 350) for i in range(1, n)]

    vfx = [StartAnim(w, h)]
    end_anim_flag = True
    text_flag = False
    dtime = 1
    while True:
        dx = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYUP and end_anim_flag and text_flag:
                return True
                vfx.append(EndAnim(w, h))
                end_anim_flag = False
        surface.blit(bg, (0, 0))

        text.render(surface, dtime) if text_flag else None

        for effect in vfx[:]:
            if not effect:
                if isinstance(effect, EndAnim):
                    return True
                if isinstance(effect, StartAnim):
                    text_flag = True
                vfx.remove(effect)
            effect.play(surface, dtime)

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

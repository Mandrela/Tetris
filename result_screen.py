import pygame
from start_screen import Text, EndAnim
from icecream import ic


def result_screen(surface: pygame.Surface, clock: pygame.time.Clock, fps: int, score: int) -> tuple[bool, bool]:
    w, h = surface.get_rect()[2:]
    dtime = 0
    you_loose_text = Text((w // 2, h // 2), ['Your score:', f'{score}'], '#FF0000', w // 20)

    save_data = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, save_data
        surface.fill('#000000')

        you_loose_text.render(surface, dtime)

        pygame.display.flip()
        dtime = clock.tick(fps)


if __name__ == '__main__':
    pygame.init()
    size = pygame.display.get_desktop_sizes()[0]
    size = (size[0] // 2, size[1] // 2)
    surfaced = pygame.display.set_mode(size)
    clocc = pygame.time.Clock()

    result_screen(surfaced, clocc, 60, 0)

    pygame.quit()

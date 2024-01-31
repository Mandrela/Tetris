from icecream import ic
from figures import *
from copy import deepcopy
from random import choice

ic.disable()


TILE = 45
W, H = 10, 20
game_size = W * TILE, H * TILE
game_sc = pygame.display.set_mode(game_size)

grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE)
        for x in range(10) for y in range(20)]


def game(surface: pygame.Surface, clock: pygame.time.Clock, fps: int) -> int:  # не забудь вернуть счет
    w, h = ic(surface.get_rect()[2:])  # вот пример как можно из surface достать размеры экрана
    # Icecream - удобный дебаггер. Ф-ция ic выведет в stdout инфу о том, что ей передали, и вернет эти значения:
    # т.е. в w и h запишутся нужные величины, а ты их сможешь увидеть. Если дебаг больше не нужен, раскомментируй строку
    # в начале (вредно бегать по файлу и что-то удалять)
    # P.S. Есть особенность: данные, пропущенные через ic(), теряют подсказки, т.к. IDE не понимает что вернет ic().

    dtime = 1  # тоже очень важная штука: на разных компах разное кол-во fps. В анимациях, движениях и т.д. используй
    # привязку к времени, а не к кадрам. dtime у тебя всегда будет равен времени, за которое отрисовался предыдущий
    # кадр, в миллисекундах и всегда типа int. Читай строку ниже.

    figure = deepcopy(choice(figures))
    anim_count, anim_speed, anim_limit = 0, 60, 2000
    field = [[0 for i in range(W)] for j in range(H)]
    score = 0
    lines = 0
    scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

    def check_borders():
        if figure[i].x < 0 or figure[i].x > W - 1:
            return False
        elif figure[i].y > H - 1 or field[figure[i].y][figure[i].x]:
            return False
        return True

    while True:  # обращайся за референсами к start_screen
        dx, rotate = 0, False
        game_sc.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1  # еще один бонус работы в функции: можно в любой момент из нее выйти через return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -1
                elif event.key == pygame.K_RIGHT:
                    dx = 1
                elif event.key == pygame.K_DOWN:
                    anim_limit = 100
                elif event.key == pygame.K_UP:
                    rotate = True

        # move x
        figure_old = deepcopy(figure)

        for i in range(4):
            figure[i].x += dx
            if not check_borders():
                figure = deepcopy(figure_old)
                break

        # move y
        anim_count += anim_speed
        if anim_count > anim_limit:
            anim_count = 0
            for i in range(4):
                figure[i].y += 1
                if not check_borders():
                    for i in range(4):
                        field[figure_old[i].y][figure_old[i].x] = pygame.Color('white')
                    figure = deepcopy(choice(figures))
                    anim_limit = 2000
                    break

        # rotate
        center = figure[0]
        figure_old = deepcopy(figure)
        if rotate:
            for i in range(4):
                x = figure[i].y - center.y
                y = figure[i].x - center.x
                figure[i].x = center.x - x
                figure[i].y = center.y + y
                if not check_borders():
                    figure = deepcopy(figure_old)
                    break

        line = H - 1
        lines = 0
        for row in range(H - 1, -1, -1):
            count = 0
            for i in range(W):
                if field[row][i]:
                    count += 1
                field[line][i] = field[row][i]
            if count < W:
                line -= 1
            else:
                lines += 1
        old_score = int(str(score)[:])
        score += scores[lines]
        if score != old_score:
            print(f'Score: {score}')
            old_score = int(str(score)[:])

        # draw grid
        [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]

        for i in range(4):
            figure_rect.x = figure[i].x * TILE
            figure_rect.y = figure[i].y * TILE
            pygame.draw.rect(game_sc, pygame.Color('white'), figure_rect)

        for y, raw in enumerate(field):
            for x, col in enumerate(raw):
                if col:
                    figure_rect.x, figure_rect.y = x * TILE, y * TILE
                    pygame.draw.rect(game_sc, col, figure_rect)

        # game over
        for i in range(W):
            if field[0][i]:
                field = [[0 for i in range(W)] for i in range(H)]
                # anim_count, anim_speed, anim_limit = 0, 60, 2000
                print('------------')
                print(f'Game over!')
                print(f'Total score: {score}')
                print('------------')
                return score
                # score = 0  # можно раскомментировать и будет беск. игра


        pygame.display.flip()
        dtime = clock.tick(fps)


if __name__ == '__main__':  # очень удобная конструкция, если хочешь протестить отдельный элемент, именно поэтому мы
    # разбивали все на несколько файлов
    pygame.init()
    size = pygame.display.get_desktop_sizes()[0]
    # size = (size[0] // 2, size[1] // 2)  # Вот тут можно регулировать размер экрана: на разных компах абсолютные
    # значения ширины и высоты экрана разные, поэтому используй относительные размеры, отталкиваясь от переданных в
    # функцию. Обязательно потести на разных значениях
    surfaced = pygame.display.set_mode(game_size)
    clocc = pygame.time.Clock()

    game(surfaced, clocc, 60)  # Твоя функция должна работать только с тем, что ей дали, если подтягивать что-то извне -
    # сразу начинается жоска головна боль. Не делой так

    pygame.quit()

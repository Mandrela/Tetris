import pygame

W, H = 10, 20
TILE = 45


figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],  # 6 фигур
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figures = [[pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in figure_pos]
           for figure_pos in figures_pos]  # расположение по центру сверху
figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)

figure = figures[3]


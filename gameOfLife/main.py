import pygame
from matrix import Matrix


SIZE = 800
win = pygame.display.set_mode((SIZE, SIZE))
matrix = Matrix(20, SIZE)
pygame.init()
pygame.display.set_caption('Game of Life')


def draw_all():
    win.fill((0, 0, 0))
    matrix.draw_blocks(win)
    matrix.draw_grid(win)
    pygame.display.update()


while True:
    fill = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not matrix.game:
                matrix.size += 1
                matrix.grid.append([0 for _ in range(matrix.size)])
                for row in matrix.grid:
                    row.append(0)
                matrix.neighbours.append([0 for _ in range(matrix.size)])
                for row in matrix.neighbours:
                    row.append(0)
            elif event.key == pygame.K_DOWN and not matrix.game:
                matrix.size = max(1, matrix.size - 1)

            elif event.key == pygame.K_SPACE and not matrix.game:
                pos = pygame.mouse.get_pos()
                x = pos[0] * matrix.size // matrix.dimension
                y = pos[1] * matrix.size // matrix.dimension
                if matrix.grid[x][y]:
                    matrix.remove_only = True
                else:
                    matrix.add_only = True
            elif event.key == pygame.K_c and not matrix.game:
                matrix = Matrix(matrix.size, SIZE)

            elif event.key == pygame.K_RETURN:
                matrix.game = not matrix.game
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                matrix.remove_only = False
                matrix.add_only = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not matrix.game:
            matrix.add_block(pygame.mouse.get_pos())
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not matrix.game:
        fill = True
    if fill:
        matrix.add_block(pygame.mouse.get_pos())
    if matrix.game:
        matrix.game_of_life()
    draw_all()

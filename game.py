import pygame
import numpy as np

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jeu de la Vie")

cell_size = 10
rows = int(500 / cell_size)
columns = int(500 / cell_size)

grid = np.zeros((rows, columns))

for i in range(rows):
    for j in range(columns):
        grid[i, j] = int(np.random.randint(2))

black = (0, 0, 0)
white = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    new_grid = grid.copy()
    for i in range(rows):
        for j in range(columns):
            neighbors = (grid[(i - 1) % rows, (j - 1) % columns] + grid[(i - 1) % rows, j % columns] + grid[
                (i - 1) % rows, (j + 1) % columns] +
                         grid[i % rows, (j - 1) % columns] + grid[i % rows, (j + 1) % columns] +
                         grid[(i + 1) % rows, (j - 1) % columns] + grid[(i + 1) % rows, j % columns] + grid[
                             (i + 1) % rows, (j + 1) % columns])
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1

    grid = new_grid
    screen.fill(black)

    for i in range(rows):
        for j in range(columns):
            color = white if grid[i, j] == 1 else black
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

    pygame.display.update()

pygame.quit()

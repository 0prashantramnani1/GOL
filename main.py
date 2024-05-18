import numpy
import time
import copy

from config import *

pygame.init() # Also initialises display
clock = pygame.time.Clock()

surface = pygame.display.set_mode((WIDTH, HEIGHT))
surface.fill(BACKGROUND)

grid = [[0 for i in range(NUM_BLOCKS_W)] for j in range(NUM_BLOCKS_H)]


def num_neighbors(h, w):
    n = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == 0 and j == 0:
                continue
            r = h + i
            c = w + j
            if r >= 0 and r < NUM_BLOCKS_H and c >= 0 and c < NUM_BLOCKS_W and grid[r][c] == 1:
                n += 1
    return n


def new_life_pos():
    global grid

    tmp_grid = copy.deepcopy(grid)

    for h in range(len(grid)):
        for w in range(len(grid[0])):
            a = num_neighbors(h, w)
            # print("a: ", a)
            if grid[h][w] == 1:
                if a < 2:
                    tmp_grid[h][w] = 0
                elif a > 3:
                    tmp_grid[h][w] = 0
            else:
                if a == 3:
                    tmp_grid[h][w] = 1
    grid = tmp_grid


def print_grid():
    for h in range(len(grid)):
        for w in range(len(grid[0])):
            print(grid[h][w], end = " ")
        print(" ")

def draw_grid():
    global grid

    for h in range(0, HEIGHT, BLOCKSIZE):
        for w in range(0, WIDTH, BLOCKSIZE):
            Rect = pygame.Rect(w, h, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(surface, BACKGROUND, Rect)
            pygame.draw.rect(surface, WHITE, Rect, width=1)
            grid[h//BLOCKSIZE][w//BLOCKSIZE] = 0

def update_grid():
    for h in range(len(grid)):
        for w in range(len(grid[0])):
            Rect = pygame.Rect(w*BLOCKSIZE, h*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
            if grid[h][w] == 1:
                pygame.draw.rect(surface, ALIVE, Rect)
            else:
                pygame.draw.rect(surface, BACKGROUND, Rect)    
            pygame.draw.rect(surface, WHITE, Rect, width=1)
    
    new_life_pos()

def color_tile(pos):
    global grid

    block_w = pos[0]//BLOCKSIZE
    block_h = pos[1]//BLOCKSIZE

    grid[block_h][block_w] = 1

    Rect = pygame.Rect(block_w*BLOCKSIZE, block_h*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
    pygame.draw.rect(surface, ALIVE, Rect)
    pygame.draw.rect(surface, WHITE, Rect, width=1)




running = True
draw_grid()


def main():
    global running
    
    life = False

    while running:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                color_tile(event.pos)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                life = ~life
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                draw_grid()
        if life:
            update_grid()
        pygame.display.flip()
        clock.tick(3)
        

if __name__ == '__main__':
    main()
    
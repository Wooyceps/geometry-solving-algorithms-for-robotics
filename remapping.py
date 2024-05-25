import numpy as np

WIDTH = 100
HEIGHT = 50

TARGET_WIDTH = 10
TARGET_HEIGHT = 5

w_ratio = WIDTH // TARGET_WIDTH  # 10
h_ratio = HEIGHT // TARGET_HEIGHT  # 10


# def populate(i,j):

def map_to_smaller(input_grid, target_width, target_height):
    w_ratio = WIDTH // target_width  # 10
    h_ratio = HEIGHT // target_height  # 10
    output_grid = np.empty((target_width, target_height))
    for i in range(target_width):
        for j in range(target_height):
            info = []
            for k in range(i*w_ratio, (i+1)*w_ratio):
                for l in range(i*h_ratio, (i+1)*h_ratio):
                    info.append(1) if input_grid[k][l] else info.append(0)
            output_grid[i][j] = 1 if 1 in info else 0

    return output_grid


input_list = np.empty((WIDTH, HEIGHT))

for i in range(WIDTH):
    for j in range(HEIGHT):
        input_list[i][j] = np.random.choice([0, 1], p=[0.8, 0.2])

mapped_grid = map_to_smaller(input_list, TARGET_WIDTH, TARGET_HEIGHT)

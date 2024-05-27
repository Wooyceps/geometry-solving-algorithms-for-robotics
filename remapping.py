import numpy as np


def map_to_smaller(input_grid, target_height, target_width):
    h_ratio, w_ratio = input_grid.shape[0] // target_height, input_grid.shape[1] // target_width
    output_grid = np.zeros((target_height, target_width))
    for i in range(target_height):
        for j in range(target_width):
            output_grid[i, j] = np.any(input_grid[i*h_ratio:(i+1)*h_ratio, j*w_ratio:(j+1)*w_ratio])
    return output_grid


array = np.random.choice([0, 1], size=(50, 100), p=[0.99, 0.01])
print("Original array:\n", array)

smaller_array = map_to_smaller(array, 5, 10)
print("Smaller array:\n", smaller_array)
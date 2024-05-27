import numpy as np

ROWS, COLS = 50, 100

TARG_ROWS, TARG_COLS = 5, 10


def map_to_smaller(input_grid, target_height, target_width):
    # Calculate the width and height ratios
    height, width = input_grid.shape
    w_ratio = width // target_width
    h_ratio = height // target_height

    # Initialize the output grid
    output_grid = np.zeros((target_height, target_width))

    # Loop over the cells in the output grid
    for i in range(target_height):
        for j in range(target_width):
            # Calculate the corresponding square in the input grid
            start_i = i * h_ratio
            end_i = (i + 1) * h_ratio
            start_j = j * w_ratio
            end_j = (j + 1) * w_ratio

            # If there is at least one 1 in the square, set the output cell to 1
            if np.any(input_grid[start_i:end_i, start_j:end_j] == 1):
                output_grid[i, j] = 1

    return output_grid


array = np.random.choice([0, 1], size=(ROWS, COLS), p=[0.99, 0.01])
print(array)

smaller_array = map_to_smaller(array, TARG_ROWS, TARG_COLS)
print(smaller_array)
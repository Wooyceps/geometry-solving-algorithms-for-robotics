import numpy as np

def map_to_smaller(input_grid, target_height, target_width):
    """
    This function takes a larger 2D numpy array and a target width and height for a smaller grid.
    It then creates a smaller grid where each cell is 1 if there is at least one 1 in the corresponding larger square of the input grid, and 0 otherwise.

    Parameters:
    input_grid (numpy.ndarray): The larger 2D numpy array.
    target_height (int): The height of the smaller grid.
    target_width (int): The width of the smaller grid.

    Returns:
    numpy.ndarray: The smaller 2D numpy array.
    """
    h_ratio, w_ratio = input_grid.shape[0] // target_height, input_grid.shape[1] // target_width
    output_grid = np.zeros((target_height, target_width))
    for i in range(target_height):
        for j in range(target_width):
            output_grid[i, j] = np.any(input_grid[i*h_ratio:(i+1)*h_ratio, j*w_ratio:(j+1)*w_ratio])
    return output_grid

# Create a 2D numpy array with a 1% chance of 1 and a 99% chance of 0
array = np.random.choice([0, 1], size=(50, 100), p=[0.99, 0.01])
print("Original array:\n", array)

# Map the larger array to a smaller array with the specified target height and width
smaller_array = map_to_smaller(array, 5, 10)
print("Smaller array:\n", smaller_array)
import numpy as np
import heapq

class Cell:
    """
    A class to represent a cell in a grid for A* pathfinding.

    Attributes
    ----------
    parent_i : int
        row index of the parent cell
    parent_j : int
        column index of the parent cell
    f : float
        total cost of the cell (g + h)
    g : float
        cost from start to this cell
    h : float
        heuristic cost from this cell to destination
    """
    def __init__(self):
        self.parent_i = 0
        self.parent_j = 0
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0

def is_valid(row, col, ROW, COL):
    """
    Check if a cell is valid (within the grid)

    Parameters
    ----------
    row : int
        row index of the cell
    col : int
        column index of the cell

    Returns
    -------
    bool
        True if the cell is within the grid, False otherwise
    """
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

def is_unblocked(grid, row, col):
    """
    Check if a cell is unblocked

    Parameters
    ----------
    grid : numpy.ndarray
        2D numpy array representing the grid
    row : int
        row index of the cell
    col : int
        column index of the cell

    Returns
    -------
    bool
        True if the cell is unblocked, False otherwise
    """
    return grid[row][col] == 0

def is_destination(row, col, dest):
    """
    Check if a cell is the destination

    Parameters
    ----------
    row : int
        row index of the cell
    col : int
        column index of the cell
    dest : tuple
        coordinates of the destination cell

    Returns
    -------
    bool
        True if the cell is the destination, False otherwise
    """
    return row == dest[0] and col == dest[1]

def calculate_h_value(row, col, dest):
    """
    Calculate the heuristic value of a cell (Euclidean distance to destination)

    Parameters
    ----------
    row : int
        row index of the cell
    col : int
        column index of the cell
    dest : tuple
        coordinates of the destination cell

    Returns
    -------
    float
        heuristic value of the cell
    """
    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5

def trace_path(cell_details, dest):
    """
    Trace the path from source to destination

    Parameters
    ----------
    cell_details : list
        2D list of Cell objects representing the grid
    dest : tuple
        coordinates of the destination cell

    Returns
    -------
    list
        List of tuples representing the path from source to destination
    """
    path = []
    row = dest[0]
    col = dest[1]

    # Trace the path from destination to source using parent cells
    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col

    # Add the source cell to the path
    path.append((row, col))
    # Reverse the path to get the path from source to destination
    path.reverse()

    return path

def a_star_search(grid, src, dest):
    """
    Implement the A* search algorithm

    Parameters
    ----------
    grid : numpy.ndarray
        2D numpy array representing the grid
    src : tuple
        coordinates of the source cell
    dest : tuple
        coordinates of the destination cell

    Returns
    -------
    list
        List of tuples representing the path from source to destination
    """
    ROW, COL = grid.shape

    # Check if the source and destination are valid
    if not is_valid(src[0], src[1], ROW, COL) or not is_valid(dest[0], dest[1], ROW, COL):
        print("Source or destination is invalid")
        return []

    # Check if the source and destination are unblocked
    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
        print("Source or the destination is blocked")
        return []

    # Check if we are already at the destination
    if is_destination(src[0], src[1], dest):
        print("We are already at the destination")
        return [(src[0], src[1])]

    # Initialize the closed list (visited cells)
    closed_list = np.zeros((ROW, COL), dtype=bool)
    # Initialize the details of each cell
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    # Initialize the start cell details
    i = src[0]
    j = src[1]
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j

    # Initialize the open list (cells to be visited) with the start cell
    open_list = []
    heapq.heappush(open_list, (0.0, i, j))

    # Initialize the flag for whether destination is found
    found_dest = False

    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)

        # Mark the cell as visited
        i = p[1]
        j = p[2]
        closed_list[i][j] = True

        # For each direction, check the successors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            # If the successor is valid, unblocked, and not visited
            if is_valid(new_i, new_j, ROW, COL) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:
                # If the successor is the destination
                if is_destination(new_i, new_j, dest):
                    # Set the parent of the destination cell
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j
                    print("The destination cell is found")
                    # Trace and return the path from source to destination
                    return trace_path(cell_details, dest)
                else:
                    # Calculate the new f, g, and h values
                    g_new = cell_details[i][j].g + 1.0
                    h_new = calculate_h_value(new_i, new_j, dest)
                    f_new = g_new + h_new

                    # If the cell is not in the open list or the new f value is smaller
                    if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                        # Add the cell to the open list
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        # Update the cell details
                        cell_details[new_i][new_j].f = f_new
                        cell_details[new_i][new_j].g = g_new
                        cell_details[new_i][new_j].h = h_new
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j

    # If the destination is not found after visiting all cells
    if not found_dest:
        print("Failed to find the destination cell")
        return []

# Define the grid (1 for unblocked, 0 for blocked)
grid = np.array([
    [0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 0]
])

# Run the A* search algorithm
path = a_star_search(grid, (0, 0), (8, 9))
print("Path from source to destination:")
print(path)
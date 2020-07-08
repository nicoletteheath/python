def add_column(grid):
    """Adds a new column to a grid. For each row, if there is an even
    number of X characters, a O is added to the row, otherwise a X is added
    to the row.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.
    
    Returns:
        The same grid, with a new column added.
    """
    pass

def add_row(grid):
    """Adds a new row to a grid. For each column, if there is an even
    number of X characters, a O is added to the column, otherwise a X is added
    to the column.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.
    
    Returns:
        The same grid, with a new row added.
    """
    pass

def increase_grid_size(grid):
    """Adds a new column and row to a grid.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.
    
    Returns:
        The same grid, with a new row and column added.
    """
    pass

def flip_card(x_pos, y_pos, grid):
    """Prompts the user to choose a cell to swap from X to O (or vice versa).

    Arguments:
        x_pos: An integer representing the x coordinate of the cell.
        y_pos: An integer representing the y coordinate of the cell.
        grid: A list of lists, where each sublist represents a row in a grid.
    
    Returns:
        The same grid, with a cell switched.
    """
    pass

def find_flipped_card(grid):
    """Prompts the user to choose a cell to swap from X to O (or vice versa).

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.
    
    Returns:
        A list containing the coordinates of the cell with the flipped card.
        In the following grid:
            a b
            c d
        These are the coordinates of each letter:
            a = (0, 1)
            b = (1, 1)
            c = (0, 0)
            d = (1, 0)
    """
    pass

if __name__ == "__main__":
    grid = [
        ["X","O","X","X","X"],
        ["X","X","O","O","O"],
        ["X","O","X","O","X"],
        ["O","X","X","X","X"],
        ["X","O","O","X","X"]
    ]
    print(increase_grid_size(grid))
    print("Pick a cell to flip")
    x_pos = int(input("Cell x pos: "))
    y_pos = int(input("Cell y pos: "))

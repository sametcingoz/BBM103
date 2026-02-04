
def check_neighbors(grid, i, j):
    neighbors = [
        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),(i, j - 1), (i, j + 1),(i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
    ]
    """"
    dict_one = {
        grid[i][j + 1]: 1,
        grid[i][j - 1]: 1,
        grid[i - 1][j]: 1,
        grid[i + 1][j]: 1,
        grid[i + 1][j + 1]: 1,
        grid[i + 1][j - 1]: 1,
        grid[i - 1][j + 1]: 1,
        grid[i - 1][j - 1]: 1,
    }
    number = grid[user_choice[1]][user_choice[0]] in dict_one
    """
    count = 0
    for x, y in neighbors:
        if (0 <= x < len(grid)
                and 0 <= y < len(grid[0])
                    and grid[x][y] == "O"):
            count += 1
    return count

def update_grid(grid):

    while True:

        new_grid = [[0 for _ in range(len(grid[0]))]
                    for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = check_neighbors(grid, i, j)
                if grid[i][j] == "O":
                    if count < 2 or count > 3:
                        new_grid[i][j] = "_"
                    else:
                        new_grid[i][j] = "O"
                else:
                    if count == 3:
                        new_grid[i][j] = "O"
        return new_grid


def main(grid):
    grid = """
       0  1  2  3  4 | 5  6  7  8  9 |10 11 12 13 14 |15 16 17 18 19 |20 21 22 23 24 |25 26 27 28 29|
     0  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
     1  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
     2  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
     3  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
     4  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _

     5  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
     6  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
     7  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
     8  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
     9  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _

    10  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    11  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    12  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    13  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    14  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _

    15  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    16  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    17  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    18  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    19  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _

    20  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    21  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    22  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    23  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    24  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _

    25  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    26  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    27  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    28  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    29  _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _   _  _  _  _  _
    """
    while True:
        for row in grid:
            print(" ".join(map(str, row)))

        row_input = int(input("Row: "))
        column_input = int(input("Column: "))

        unique_counts = check_neighbors(grid, row_input, column_input)

        if grid[row_input][column_input] == "O":
            if unique_counts < 2 or unique_counts > 3:
                grid[row_input][column_input] = "_"
        else:
            if unique_counts == 3:
                grid[row_input][column_input] = "O"
        grid = update_grid(grid)


if __name__ == '__main__':

    print(f"Welcome to Conway's Game of Life!\n1.Select initial pattern\n2.Control simulation speed\n3.Start Game\n4.Quit Game")
    user_selection = int(input("Your selection:\n"))
    print("Conway's Game of Life!")
    main(grid=True)

"""
1. Toggle cell state (to change)
2. Continue the next generation(s)
3. Quit Game
Your selection:1
Enter the row, column indices separated by a comma to be converted into the opposite value. There will be no whitespaces. Type 'r' for returning the game without any change:29,29

Conway's Game of Life!
"""
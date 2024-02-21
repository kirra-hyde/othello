def legal_move(game_board: list[list[int]], player: int, coordinates: tuple[int, int]) -> bool:

    legal_game_board(game_board)
    legal_player(player)
    width = len(game_board[0])
    height = len(game_board)
    legal_coordinates(coordinates, width, height)

    x, y = coordinates

    if game_board[y][x] != 0:
        return False

    opponent = 2 if (player == 1) else 1

    for dx, dy in [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]:
        curr_x, curr_y = x + dx, y + dy
        if 0 <= curr_x < len(game_board[0]) and 0 <= curr_y < len(game_board):
            if game_board[curr_y][curr_x] == opponent:
                # Check if a flanking piece exists in this direction
                while 0 <= curr_x < len(game_board[0]) and 0 <= curr_y < len(game_board):
                    if game_board[curr_y][curr_x] == player:
                        return True
                    if game_board[curr_y][curr_x] == 0:  # Empty cell
                        break
                    curr_x += dx
                    curr_y += dy

    return False


def legal_game_board(game_board: list[list[int]]) -> None:

    if type(game_board) != list:
        raise TypeError("game_board must be a list of lists of integers")

    if type(game_board[0]) != list:
        raise TypeError("game_board must be a list of lists of integers")

    num_cols = len(game_board[0])

    for row in game_board:
        if type(row) != list:
            raise TypeError("game_board must be a list of lists of integers")

        if len(row) != num_cols:
            raise ValueError("game_board must have rectangular dimensions")

        for cell in row:
            if type(cell) != int:
                raise TypeError("game_board must be a list of lists of integers")
            if not (cell == 0 or cell == 1 or cell == 2):
                raise ValueError("All cells must be 0, 1, or 2")

    if len(game_board) < 4:
        raise ValueError("game_board dimension must be at least 4 by 4")

    if num_cols < 4:
        raise ValueError("game_board dimension must be at least 4 by 4")


def legal_player(player: int) -> None:
    if type(player) != int:
        raise TypeError("player must be an integer")

    if not (player == 1 or player == 2):
        raise ValueError("player must be 1 or 2")


def legal_coordinates(coordinates: tuple[int, int], width: int, height: int) -> None:
    if type(coordinates) != tuple:
        raise TypeError("coordinates must be a tuple of 2 integers")

    if len(coordinates) != 2:
        raise TypeError("coordinates must be a tuple of 2 integers")

    if type(coordinates[0]) != int or type(coordinates[1]) != int:
        raise TypeError("coordinates must be a tuple of 2 integers")

    if coordinates[0] < 0 or coordinates[0] >= width:
        raise ValueError("x coordinate is outside board dimensions")

    if coordinates[1] < 0 or coordinates[1] >= height:
        raise ValueError("y coordinate is outside board dimensions")
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

BOARD_SIZES = [5, 8]
SHIP_SIZES = {
    5: [2, 3, 3],
    8: [2, 3, 3, 4, 5]
}
ROW_RANGES = {
    5: range(1, 6),
    8: range(1, 9)
}
COL_RANGES = {
    5: ['A', 'B', 'C', 'D', 'E'],
    8: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
}
AMMO = {
    5: 10,
    8: 20
}


def welcome_screen():
    """
    This function displays a welcome message to the user.
    """
    print(Back.BLUE + "\nWelcome to BattleShip!\n")
    print(Back.BLUE + "The goal of the game is to sink all enemy ships.\n")


instructions = """
1. Select a board size either:
   i. 5 (5x5) - 3 ships (sizes 2, 3, 3).
   ii. 8 (8x8) - 5 ships (sizes 2, 3, 3, 4, 5).
2. Position your ships on the board:
   i. Ships cannot overlap.
   ii. Ships can be horizontal or vertical, not diagonal.
   iii. Enter the starting row and column for each ship.
3. Let the battle begin:
   i. Enter the row and column to fire at.
   ii. Hit - "x", Miss - "-".
4. The game ends when all ships are sunk, ammo runs out, or you type "exit".
"""

welcome_screen()
print(instructions)


class BattleShipBoard:
    def __init__(self, boards):
        try:
            pass
        except ValueError as e:
            raise ValueError(f"{e}")
        except Exception:
            boards = int(boards)
            if boards not in [5, 8]:
                raise ValueError(Fore.YELLOW +
                                 "The board must be 5 or 8. Please try again.")

        self.boards = boards
        self.board = [[' '] * boards for _ in range(boards)]
        self.ships = []

    def print_board(self):
        """
        This function prints the board with row and column
        labels to the terminal.
        """
        print(Fore.WHITE + "   " + " ".join
              (chr(ord('A') + i) for i in range(self.boards)))

        for i, row in enumerate(self.board):
            print(f"{i + 1:2d} {' '.join(str(cell) for cell in row)}")

    def place_ships_on_board(self, ships):
        """
        This function places ships on the board initially.
        """
        for ship in ships:
            row, col = ship
            self.board[row - 1][col] = Fore.GREEN + 's'

    def are_all_ships_sunk(self):
        """
        This function checks if all the ships on the board are sunk.
        """
        for row in self.board:
            for cell in row:
                if cell == Fore.GREEN + "s":
                    return False
        return True


def exit_game():
    """
    This function allows the user to exit the game.
    """
    print(Fore.BLUE + "Exiting the game.")
    exit()


def fire_ammo(board, ammo_count):
    for _ in range(ammo_count):
        try:
            target = input(Fore.CYAN + "Enter the row and "
                           "column to fire at:").upper()

            if target.lower() == 'exit':
                exit_game()

            row, col_text = int(target[:-1]), target[-1]

            col_range = [chr(ord('A') + i) for i in range(board.boards)]

            if (row not in range(1, board.boards + 1)
                    or col_text not in col_range):
                raise ValueError(
                    Fore.YELLOW +
                    f"Invalid row: {row}."
                    "Row should be between 1 and {board.boards}."
                    f"Invalid column: {col_text}."
                    "Column should be one of {col_range}."
                )

            print(f"Firing at {target}...")

            col_index = col_range.index(col_text)
            if (row, col_index) in board.ships:
                print("Direct Hit!")
                board.board[row - 1][col_index] = Fore.RED + "x"
            else:
                print("You Missed!")
                board.board[row - 1][col_index] = Fore.BLUE + "-"

            board.print_board()

            # Check if all ships are sunk after each shot
            if board.are_all_ships_sunk():
                print(Fore.BLUE
                      + "Congratulations! You have sunk all the "
                        "enemy ships. Game Over!")
                return

        except ValueError as e:
            print(Fore.YELLOW + f"Invalid input: {e}")

    """
    if the loop completes without returning, it means the player
    ran out of ammo
    """

    print(Fore.BLUE + "You are out of ammo! Game Over.")


"""
Get the board size from the user input.
"""
while True:
    try:
        boards = input(Fore.CYAN + "Enter the board size you wish to use,"
                       f"5 or 8: \n")

        if boards.lower() == 'exit':
            exit_game()

        if not boards.isdigit():
            raise ValueError(Fore.YELLOW
                             + "No text or symbols allowed. "
                               "Please try again.")
        x = BattleShipBoard(boards)
        break
    except ValueError as e:
        print(Fore.YELLOW + f"Invalid input: {e}\n")

x.print_board()


def get_user_ship_coordinates(board_size, ship_size, row_range, col_range):
    print(Fore.CYAN + "\nEnter the location coordinates"
          f" for the ship size - {ship_size}\n")

    while True:
        try:
            orientation = input(Fore.CYAN
                                + "Enter the orientation of the ship."
                                f" H for horizontal or V for
                                f" vertical: ").upper()

            if orientation.lower() == 'exit':
                exit_game()

            if orientation not in ['H', 'V']:
                raise ValueError(Fore.YELLOW + "Please enter H for Horizontal
                                 f" or V for Vertical.")

            # Input format: "row, column"
            input_coordinates = input(Fore.CYAN + "Enter starting row and
                                      f" column for the ship you want
                                      f" to position: ").upper()

            if input_coordinates.lower() == 'exit':
                exit_game()

            # Validate coordinates
            if len(input_coordinates) !=
            2 or not input_coordinates[0].isalnum()
            or not input_coordinates[1].isalnum():
                raise ValueError(Fore.YELLOW + f"Please enter a row and
                                 f" column. No symbols allowed." +
                                 Style.RESET_ALL)

            start_row, start_col = input_coordinates[0], input_coordinates[1]

            if start_row.isalpha():
                start_row = row_range.index(start_row.upper()) + 1
            elif start_row.isdigit():
                start_row = int(start_row)
            else:
                raise ValueError(Fore.YELLOW + "Invalid row value.")

            if start_col.isalpha():
                start_col = col_range.index(start_col.upper())

            if orientation == 'H':
                if start_col + ship_size > board_size:
                    raise ValueError(Fore.YELLOW + f"Ship cannot fit
                                     f" horizontally in the selected
                                     f" position.")
                return [(start_row, col_range.index(chr(ord('A') + i)))
                        for i in range(start_col, start_col + ship_size)]

            elif orientation == 'V':
                if start_row + ship_size - 1 > board_size:
                    raise ValueError(Fore.YELLOW + f"Ship cannot fit vertically
                                     f" in the selected position.")
                return [(start_row + i, start_col) for i in range(ship_size)]

        except ValueError as e:
            print(Fore.YELLOW + f"Invalid input: {e}")


def create_ships(board_size):
    """
    This function generates ships based on the board size.
    """
    if board_size == 5:
        ship_sizes = [2, 3, 3]
        row_range = range(1, 6)
        col_range = ['A', 'B', 'C', 'D', 'E']
    elif board_size == 8:
        ship_sizes = [2, 3, 3, 4, 5]
        row_range = range(1, 9)
        col_range = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    else:
        raise ValueError(Fore.YELLOW + "Invalid board size.")

    ships = []
    board = [[' '] * board_size for _ in range(board_size)]

    def print_board_with_headers(board):
        # Print the column headers
        print(Fore.WHITE + "   " + " ".join(col_range))
        for i, row in enumerate(board):
            print(f"{i + 1:2d} {' '.join(str(cell) for cell in row)}")

    for size in ship_sizes:
        while True:
            ship =
            get_user_ship_coordinates(board_size, size, row_range, col_range)
            if not any(cell in ships for cell in ship):
                break
            print(Fore.YELLOW + f"Ships cannot overlap. Please enter a new
                  f"row and column for the ship.\n")
        ships.extend(ship)

        # Update the board with 's' at ship positions
        for ship_cell in ship:
            row, col = ship_cell
            board[row - 1][col] = Fore.GREEN + 's'

        print(Fore.BLUE + "Updated board after placing a ship:\n")
        print_board_with_headers(board)

    print(Fore.BLUE + "All ships are now positioned on the board:\n")
    print_board_with_headers(board)

    return ships


ships = create_ships(x.boards)
x.ships = ships
x.place_ships_on_board(ships)
fire_ammo(x, 10 if x.boards == 5 else 20)

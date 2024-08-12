import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

BOARD_SIZES = [5, 8]
SHIP_NAMES_AND_SIZES = {
    5: {'Scout': 2, 'Frigate': 3, 'Corvette': 3},
    8: {'Scout': 2, 'Frigate': 3, 'Corvette': 3, 'Destroyer': 4, 'Battleship': 5}
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
   i. 5 (5x5) - 3 ships: Scout (2), Frigate (3), Corvette (3).
   ii. 8 (8x8) - 5 ships: Scout (2), Frigate (3), Corvette (3), Destroyer (4), Battleship (5).
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
        if not isinstance(boards, int):
            raise ValueError(Fore.YELLOW + "The board must be an integer. Please try again.")
        if boards not in [5, 8]:
            raise ValueError(Fore.YELLOW + "The board must be 5 or 8. Please try again.")

        self.boards = boards
        self.board = [[' '] * boards for _ in range(boards)]
        self.ships = {}

    def print_board(self):
        """
        This function prints the board with row and column
        labels to the terminal.
        """
        print(Fore.WHITE + "   " + " ".join
              (chr(ord('A') + i) for i in range(self.boards)))

        reveal_ships = True

        for i, row in enumerate(self.board):
            if reveal_ships:
                print(f"{i + 1:2d} {' '.join(str(cell) for cell in row)}")
            else:
                print(f"{i + 1:2d} {' '.join(str(cell) if cell not in [Fore.GREEN + 'S', Fore.GREEN + 'F', Fore.GREEN + 'C', Fore.GREEN + 'D', Fore.GREEN + 'B'] else ' ' for cell in row)}")

    def place_ships_on_board(self, ships):
        for ship_name, ship_coords in ships.items():
            for row, col in ship_coords:
                self.board[row - 1][col] = Fore.GREEN + ship_name[0]

    def are_all_ships_sunk(self):
        """
        This function checks if all the ships on the board are sunk.
        """
        for row in self.board:
            for cell in row:
                if cell.startswith(Fore.GREEN):
                    return False
        return True


def exit_game():
    """
    This function allows the user to exit the game.
    """
    print(Fore.BLUE + "Exiting the game.")
    exit()


def fire_ammo(board, target_board, player_name):
    while True:
        try:
            if player_name == "Computer":
                row = random.randint(1, board.boards)
                col_text = random.choice(COL_RANGES[board.boards])
            else:
                target = input(Fore.CYAN + f"{player_name}, enter the row and column to fire at: ").upper()

                if target.lower() == 'exit':
                    exit_game()

                row, col_text = int(target[:-1]), target[-1]

            col_range = [chr(ord('A') + i) for i in range(board.boards)]

            if row not in range(1, board.boards + 1) or col_text not in col_range:
                raise ValueError(
                    Fore.YELLOW +
                    f"Invalid row: {row}."
                    "Row should be between 1 and {board.boards}."
                    f"Invalid column: {col_text}."
                    "Column should be one of {col_range}."
                )

            print(f"{player_name} firing at {row}{col_text}...")

            col_index = col_range.index(col_text)
            if any((row, col_index) in coords for coords in target_board.ships.values()):
                print(Fore.RED + f"{player_name}, Direct Hit!")
                target_board.board[row - 1][col_index] = Fore.RED + "x"
            else:
                print(Fore.BLUE + f"{player_name}, Missed!")
                target_board.board[row - 1][col_index] = Fore.BLUE + "-"

            target_board.print_board()
            # Check if all ships are sunk
            if target_board.are_all_ships_sunk():
                print(Fore.BLUE + f"Congratulations! {player_name} has sunk all the enemy ships. Game Over!")
                return True

            break

        except ValueError as e:
            if player_name != "Computer":
                print(Fore.YELLOW + f"Invalid input: {e}")

    return False


while True:
    try:
        boards = input(Fore.CYAN + "Enter the board size you wish to use, "
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


def get_user_ship_coordinates(ship_name, ship_size, board_size, row_range, col_range):
    print(Fore.CYAN + f"\nEnter the location coordinates for the {ship_name} (size {ship_size})\n")

    while True:
        try:
            orientation = input(Fore.CYAN
                                + "Enter the orientation of the ship."
                                f" H for horizontal or V for"
                                f" vertical: ").upper()

            if orientation.lower() == 'exit':
                exit_game()

            if orientation not in ['H', 'V']:
                raise ValueError(Fore.YELLOW + "Please enter H for Horizontal"
                                 f" or V for Vertical.")

            input_coordinates = input(Fore.CYAN + "Enter starting row and column for the ship: ").upper()

            if input_coordinates.lower() == 'exit':
                exit_game()

            if len(input_coordinates) < 2 or not input_coordinates[:-1].isdigit() or not input_coordinates[-1].isalpha():
                raise ValueError(Fore.YELLOW + "Please enter a valid row number and column letter (e.g., 3C).")

            start_row, start_col = int(input_coordinates[:-1]), input_coordinates[-1]

            if start_row not in row_range or start_col not in col_range:
                raise ValueError(Fore.YELLOW + "Starting coordinates are out of range.")

            start_col_index = col_range.index(start_col)

            if orientation == 'H':
                if start_col_index + ship_size > board_size:
                    raise ValueError(Fore.YELLOW + "Ship cannot fit horizontally in the selected position.")
                return [(start_row, start_col_index + i) for i in range(ship_size)]

            elif orientation == 'V':
                if start_row + ship_size - 1 > board_size:
                    raise ValueError(Fore.YELLOW + "Ship cannot fit vertically in the selected position.")
                return [(start_row + i, start_col_index) for i in range(ship_size)]

        except ValueError as e:
            print(Fore.YELLOW + f"Invalid input: {e}")


def create_ships(board_size, is_computer=False):
    if board_size not in SHIP_NAMES_AND_SIZES:
        raise ValueError(Fore.YELLOW + "Invalid board size.")

    ship_dict = SHIP_NAMES_AND_SIZES[board_size]
    row_range = ROW_RANGES[board_size]
    col_range = COL_RANGES[board_size]

    ships = {}
    board = [[' '] * board_size for _ in range(board_size)]

    def print_board_with_headers(board):
        print(Fore.WHITE + "   " + " ".join(col_range))
        for i, row in enumerate(board):
            print(f"{i + 1:2d} {' '.join(str(cell) for cell in row)}")

    for ship_name, ship_size in ship_dict.items():
        while True:
            if is_computer:
                orientation = random.choice(['H', 'V'])
                start_row = random.choice(row_range)
                start_col = random.choice(col_range)
                start_col_index = col_range.index(start_col)
                if orientation == 'H':
                    if start_col_index + ship_size <= board_size:
                        ship_coords = [(start_row, start_col_index + i) for i in range(ship_size)]
                    else:
                        continue
                else:
                    if start_row + ship_size - 1 <= board_size:
                        ship_coords = [(start_row + i, start_col_index) for i in range(ship_size)]
                    else:
                        continue
            else:
                ship_coords = get_user_ship_coordinates(ship_name, ship_size, board_size, row_range, col_range)

            if not any(cell in ships.values() for ship in ships.values() for cell in ship_coords):
                ships[ship_name] = ship_coords
                break

            if not is_computer:
                print(Fore.YELLOW + "Ships cannot overlap. Please enter a new row and column for the ship.\n")

        for ship_cell in ship_coords:
            row, col = ship_cell
            board[row - 1][col] = Fore.GREEN + ship_name[0]

        if not is_computer:
            print(Fore.BLUE + "Updated board after placing a ship:\n")
            print_board_with_headers(board)

    if not is_computer:
        print(Fore.BLUE + "All ships are now positioned on the board:\n")
        print_board_with_headers(board)

    return ships


player_board = BattleShipBoard(boards)
player_ships = create_ships(player_board.boards)
computer_board = BattleShipBoard(boards)
computer_ships = create_ships(computer_board.boards, is_computer=True)

player_board.ships = player_ships
computer_board.ships = computer_ships

player_board.place_ships_on_board(player_ships)
computer_board.place_ships_on_board(computer_ships)

player_turn = True
while True:
    if player_turn:
        if fire_ammo(player_board, computer_board, "Player"):
            break
    else:
        if fire_ammo(computer_board, player_board, "Computer"):
            break
    player_turn = not player_turn

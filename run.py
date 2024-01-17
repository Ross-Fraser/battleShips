import random

BOARD_SIZES = [5, 8]
SHIP_SIZES_5 = [2, 3, 3]
ROW_RANGE_5 = range(1, 6)
COL_RANGE_5 = ['A', 'B', 'C', 'D', 'E']
SHIP_SIZES_8 = [2, 3, 3, 4, 5]
ROW_RANGE_8 = range(1, 9)
COL_RANGE_8 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
AMMO_5 = 10
AMMO_8 = 20


def welcome_screen():
    """
    This function displays a welcome message to the user.
    """
    print("Welcome to BattleShip!\n")
    print("The goal of the game is to sink all enemy ships.\n")


instructions = """ 
 1. Select a board size either:
    i.      5 (5x5). which has 3 ships, the sizes are 2, 3 and 3.
    ii.     The original 8 (8x8). which has 5 ships, the sizes are 2, 3, 3, 4 and 5.
 2. Position your ships on the board.
    i.      Depending on the board you choose, you will have to position 3 or 5 ships (the ships cannot overlap)
    ii.     You can choose to position your ships either horizontal or vertical, but not diagonal.
    iii.    You then select the row and column where you want your ship to start from.
 3. Let the battle begin!
    i.      Enter the row and column of the position you want to bomb.
    ii.     If you hit a ship, you will see an X on the board, otherwise you will see a *.
 5. The game ends when all of 1 navies ships are sunk.
    """

welcome_screen()
print(instructions)


class BattleShipBoard:
    """
    This class creates a board for the game.
    """
    def __init__(self, boards):
        """
        This function sets the size of the board.
        """
        try:
            boards = int(boards)
            if boards not in [5, 8]:
                raise ValueError("The board must be 5 or 8, please try again.")
        except ValueError as e:
            raise ValueError(f"{e}")

        self.boards = boards
        self.board = [[0] * boards for _ in range(boards)]

    def print_board(self):
        """
        This function prints the board with row and column labels to the terminal.
        """
        print("   " + " ".join(chr(ord('A') + i) for i in range(self.boards)))

        for i, row in enumerate(self.board):
            print(f"{i + 1:2d} {' '.join(str(cell) for cell in row)}")


"""
Get the board size from the user input.
"""
while True:
    try:
        boards = input("Enter board size 5 or 8: ")
        if not boards.isdigit():
            raise ValueError("no text or symbols allowed, please try again.")
        x = BattleShipBoard(boards)
        break
    except ValueError as e:
        print(f"Invalid input: {e}\n")

x.print_board()


def get_user_ship_coordinates(board_size, ship_size, row_range, col_range):
    """
    This function prompts the user to input the row and column of a ship.
    """
            
    print(f"Enter the details for a ship location of size {ship_size}\n")
    
    while True:
        try:
            orientation = input("Enter orientation [H]orizontal or [V]ertical): ").upper()
            if orientation not in ['H', 'V']:
                raise ValueError("Please enter 'H' or 'V'.")
            
             # Input format: "row, column"
            input_coordinates = input(f"Enter starting row and column: ").upper()
            
            if len(input_coordinates) != 2 or not input_coordinates.isalnum():
                raise ValueError("Please enter a valid 2-character alphanumeric coordinate without symbols.")

            start_row, start_col = input_coordinates[0], input_coordinates[1]
            
             # Handle both cases where the first character is a letter or a number
            if start_row.isalpha():
                start_row = row_range.index(start_row.upper()) + 1
            elif start_row.isdigit():
                start_row = int(start_row)
            else:
                raise ValueError("Invalid row value.")

            if start_col not in col_range:
                raise ValueError("Invalid column value.")
            
            if board_size == 5:
                ship = [(int(start_row), col) for col in range(col_range.index(start_col), col_range.index(start_col) + ship_size)]
            elif board_size == 8:
                ship = [(row, col_range.index(start_col)) for row in range(int(start_row), int(start_row) + ship_size)]
            else:
                raise ValueError("Invalid board size.")

            if orientation == 'H':
                ship = [(int(start_row), col) for col in range(col_range.index(start_col), col_range.index(start_col) + ship_size)]
            else:
                ship = [(row, col_range.index(start_col)) for row in range(int(start_row), int(start_row) + ship_size)]

            return ship
        
        except ValueError as e:
            print(f"Invalid input: {e}\n")
            
def create_ships(board_size):
    """
    This function generates ships based on the board size.
    """
    if board_size == 5:
        ship_sizes = SHIP_SIZES_5
        row_range = ROW_RANGE_5
        col_range = COL_RANGE_5
    elif board_size == 8:
        ship_sizes = SHIP_SIZES_8
        row_range = ROW_RANGE_8
        col_range = COL_RANGE_8
    else:
        raise ValueError("Invalid board size.")

    ships = []
    for size in ship_sizes:
        ship = get_user_ship_coordinates(board_size, size, row_range, col_range)
        while any(cell in ships for cell in ship):
            print("Ships cannot overlap. Please re-enter the row and column for the ship.\n")
            ship = get_user_ship_coordinates(board_size, size, row_range, col_range)
        ships.extend(ship)

    return ships

def fire_ammo(board, ammo_count):
    """
    This function allows the player to fire a specified number of shots on the board.
    """
    for _ in range(ammo_count):
        try:
            target = input("Enter the row and column to fire:").upper()
            row, col_text = int(target[:-1]), target[-1]

            col_range = [chr(ord('A') + i) for i in range(board.boards)]

            if row not in range(1, board.boards + 1) or col_text not in col_range:
                raise ValueError(f"Invalid row and or column. Please try again. "
                                 f"Row should be between 1 and {board.boards}, "
                                 f"Column should be one of {col_range}.")

            print(f"Firing at {target}...")

            # Check if the shot hits a ship
            col_index = col_range.index(col_text)
            if (row, col_index) in board.ships:
                print("Direct Hit!")
                board.board[row - 1][col_index] = "X"
            else:
                print("You Miss!")
                board.board[row - 1][col_index] = "*"

            # Print the updated board
            board.print_board()

        except ValueError as e:
            print(f"Invalid input: {e}")
            
ships = create_ships(x.boards)
x.ships = ships
fire_ammo(x, AMMO_5)
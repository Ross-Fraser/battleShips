import random

BOARD_SIZES = [5, 8]
SHIP_SIZES_5 = [2, 3, 3]
ROW_RANGE_5 = range(1, 6)
COL_RANGE_5 = ['A', 'B', 'C', 'D', 'E']
SHIP_SIZES_8 = [2, 3, 3, 4, 5]
ROW_RANGE_8 = range(1, 9)
COL_RANGE_8 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def welcome_screen():
    """
    This function displays a welcome message to the user.
    """
    print("Welcome to BattleShip!\n")
    print("The goal of the game is to sink all of the ships.\n")


instructions = """ 
 1. Select a board size either:
    i.      5 (5x5). which has 3 ships, the sizes are 2, 3 and 3.
    ii.     The original 8 (8x8). which has 5 ships, the sizes are 2, 3, 3, 4 and 5.
 2. Position your ships on the board.
    i.      Depending on the board you choose, you will have to position 3 or 5 ships (the ships cannot overlap)
    ii.     You can choose to position your ships either horizontal or vertical, but not diagonal.
    iii.    Enter the row where you want your ship to start.
    iv.     Enter the column where you want your ship to start.  
 3. Enter the coordinates of the position you want to attack, using the row and column labels e.g 2C or 7G.
 4. If you hit a ship, you will be notified. If you miss, you will
    be notified.
 5. The game ends when all of the ships are sunk.
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


def get_user_ship_input(board_size, ship_size, row_range, col_range):
    """
    This function prompts the user to input the location of a ship.
    """
            
    print(f"Enter the details for a ship location of size {ship_size}:\n")
    
    while True:
        try:
            orientation = input("Enter orientation (horizontal or vertical): ").lower()
            if orientation not in ['horizontal', 'vertical']:
                raise ValueError("Please enter 'horizontal' or 'vertical'.")
            
            start_row = int(input(f"Enter starting row ({min(row_range)} to {max(row_range)}): "))
            start_col = input(f"Enter starting column ({min(col_range)} to {max(col_range)}): ").upper()

            if start_row not in row_range:
                raise ValueError(f"Please enter a valid row value.")
            if start_col not in col_range:
                raise ValueError(f"Please enter a valid column value.")

            if board_size == 5:
                ship = [(start_row, col) for col in range(col_range.index(start_col), col_range.index(start_col) + ship_size)]
            elif board_size == 8:
                ship = [(row, col_range.index(start_col)) for row in range(start_row, start_row + ship_size)]
            else:
                raise ValueError("Invalid board size.")

            if orientation == 'horizontal':
                ship = [(start_row, col) for col in range(col_range.index(start_col), col_range.index(start_col) + ship_size)]
            else:
                ship = [(row, col_range.index(start_col)) for row in range(start_row, start_row + ship_size)]

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
        ship = get_user_ship_input(board_size, size, row_range, col_range)
        while any(cell in ships for cell in ship):
            print("Ships cannot overlap. Please re-enter the ship coordinates.\n")
            ship = get_user_ship_input(board_size, size, row_range, col_range)
        ships.extend(ship)

    return ships
            
ships = create_ships(x.boards)
print(ships)
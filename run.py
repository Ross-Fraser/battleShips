def welcome_screen():
    """
    This function displays a welcome message to the user.
    """
    print("Welcome to BattleShip!")
    print("The goal of the game is to sink all of the ships.\n")


instructions = """ 1. Select a board size either 5x5 or the original 8x8.
 2. Position your ships on the board. You can choose to position
    your ships either horizontally or vertically, but not diagonal.
 3. Enter the coordinates of the position you want to attack.
 4. If you hit a ship, you will be notified. If you miss, you will
    be notified as well.
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
        This function prints the board to the terminal.
        """
        for row in self.board:
            print(row)


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

print(boards)
x.print_board()

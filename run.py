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

class battleShipBoard:
    """
    This class creates a board for the game.
    """
    def __init__(self, board_size):
      """
      This function sets the size of the board.
      """
      self.board_size = board_size
      self.board = [[0] * board_size for _ in range(board_size)]

    def print_board(self):
      """
      This function prints the board.
      """
      for row in self.board:
         print(row)
              
board_size = 5
x = battleShipBoard(board_size)
x.print_board()
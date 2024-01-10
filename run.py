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

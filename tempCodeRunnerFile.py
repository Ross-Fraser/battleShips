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